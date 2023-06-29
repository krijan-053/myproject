from django.db import models

# Create your models here.



class ClassRoom(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    profile_picture = models.FileField(upload_to="profile_pictures",null=True,blank=True)
    age = models.IntegerField()
    department = models.CharField(max_length=20)
    classroom = models.ForeignKey(ClassRoom, on_delete= models.CASCADE,
                                  related_name='classroom_students', null=True, blank=True)


    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    address = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=14)
    email = models.EmailField()


class Publication(models.Model):
    title = models.CharField(max_length=20)

class Article(models.Model):
    headline = models.CharField(max_length=50)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline
