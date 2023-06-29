from django import forms
from myapp.models import Student, ClassRoom


class ClassRoomForm(forms.Form):
    name = forms.CharField(max_length=20)


class ClassRoomModelForm(forms.ModelForm):
    class Meta:
        model =  ClassRoom
        fields = ["name"]


class StudentForm(forms.Form):
    name = forms.CharField(max_length=20)
    age = forms.IntegerField()
    department = forms.CharField(max_length=20)


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "age", "department"]
