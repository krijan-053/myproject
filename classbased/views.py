from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from myapp.models import ClassRoom, Student
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import ClassRoomForm, StudentForm, StudentModelForm, ClassRoomModelForm


# Create your views here.
class FirstView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "classbased/first.html")

    def post(self, request, *args, **kwargs):
        pass


class ClassRoomView(View):
    def get(self, request, *args, **kwargs):
        context = {
            "title": "Classroom",
            "classrooms": ClassRoom.objects.all()
        }
        return render(request, "classbased/classroom.html", context=context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get("class_name")
        ClassRoom.objects.create(name=name)
        return redirect('classroom_view')


class ClassRoomTemplateView(TemplateView):
    template_name = "classbased/classroom.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Classroom",
            "classrooms": ClassRoom.objects.all()
        })
        return context


@method_decorator(login_required, name="dispatch")
class StudentListView(ListView):
    # model = Student
    template_name = "classbased/student.html"
    context_object_name = "students"
    queryset = Student.objects.all()
    # queryset = Student.objets.filter(name__istartwith="h")


class StudentDetailView(DetailView):
    model = Student
    template_name = "classbased/student_detail.html"


class ClassRoomFormView(CreateView):
    model = ClassRoom
    template_name = "classbased/classroom_form.html"
    form_class = ClassRoomModelForm
    success_url = reverse_lazy("classroom_django_form")


def classroom_form(request):
    if request.method == "POST":
        form = ClassRoomForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            name = form.cleaned_data.get("name")
            ClassRoom.objects.create(name=name)

        return redirect("classroom_form")
    context = {
        "title": "ClassRoom Form",
        "form": ClassRoomForm(),
        "classrooms": ClassRoom.objects.all()
    }
    return render(request, "classbased/classroom_form.html", context=context)


def student_form(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            name = form.cleaned_data.get("name")
            age = form.cleaned_data.get("age")
            department = form.cleaned_data.get("department")
            Student.objects.create(name=name, age=age, department=department)

        return redirect("student_form")
    context = {
        "title": "Add Student",
        "form": StudentForm(),
        "students": Student.objects.all()
    }
    return render(request, "classbased/student_form.html", context=context)


def student_model_form(request):
    if request.method == "POST":
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("student_model_form")
    context = {
        "title": "Add Student",
        "form": StudentModelForm(),
        "students": Student.objects.all()
    }
    return render(request, "classbased/student_model_form.html", context=context)
