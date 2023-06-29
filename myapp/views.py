from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,JsonResponse

from myapp.models import Student,ClassRoom,StudentProfile


# Create your views here.

def test(request):
    #response = HttpResponse()
    html_content = """
    <html>
    <head>
        <title>Django Project</title>
    </head>
    <body>
    <h1>Django is a web framework.</h1>
    </body>
    </home> 
        
    """
    #response.content = html_content
    return HttpResponse(html_content)


def home(request):
    #return render(request,"myapp/home.html")
    return render(request,"myapp/portfolio.html")





def index(request):
    #context = {"id": 1,"name":"Arya","age": 24,"title":"student"}
    # context = {"students" : [
    #     {"id": 1, "name": "ken", "age": 25, "is_active": True},
    #     {"id": 2, "name": "ram", "age": 21, "is_active": False },
    #     {"id": 3, "name": "hari", "age": 23, "is_active": True},
    #     {"id": 4, "name": "jon", "age": 24, "is_active": False},
    #     ], "title": "Student"}
    context = {"students" : Student.objects.all(),"title": "Student"}

    return render(request, template_name="myapp/index.html",context=context)

def view_name_Jon(request):
    return render(request, "myapp/jon.html")



def view_name_Jane(request):
    return render(request, "myapp/jane.html")

def view_name(request,name):
    last_name = request.GET.get('last_name')

    if name.lower() == 'ram':
        full_name = "Ram Bahadur"
    elif name.lower() == 'harry':
        full_name = "Harry Krishna"
    elif name.lower() == 'jon':
        full_name = "Jon Prasad"
    else:
        #return HttpResponse("<h1>Name not found</h1>")
        return HttpResponseNotFound("<h1>Name not found</h1>")

    context = {
        "name": full_name,
              }


    if last_name:
        context.update(last_name=last_name)
    return render(request, "myapp/name.html", context=context)



def json_view(request):
    response = {"id":1,"name":"ken","age": 25}
    students = [
        {"id": 1, "name": "ken", "age": 25},
        {"id": 2, "name": "ram", "age": 21},
        {"id": 3, "name": "hari", "age": 23},
        {"id": 4, "name": "jon", "age": 24},
    ]

    return JsonResponse(students,safe=False)

def students(request):
    context = {"title": "Students",
               "classrooms": ClassRoom.objects.all(),
               "students": Student.objects.all(),
               "student_profiles": StudentProfile.objects.all()
               }

    return render(request, template_name="myapp/students.html",context=context)

def page1(request):
    return render(request,template_name="myapp/page1.html")
def page2(request):
    return render(request,template_name="myapp/page2pyth.html")

def student_detail(request, id):
    context = {
        "student" : Student.objects.get(id=id),
        "title" : "Student Detail"
    }
    return render(request, "myapp/student_detail.html",context=context)



# def home(request):
#     # response = HttpResponse()
#     html_content = """
#     <html>
#     <head>
#         <title>Django Project</title>
#     </head>
#     <body>
#     <h1>Django is a web framework.</h1>
#     </body>
#     </home>
#
#     """
#     # response.content = html_content
#     return HttpResponse(html_content)