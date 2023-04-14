from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cwid = models.CharField(max_length=9)
    is_tutor = models.BooleanField('Is Tutor', default=False)
    is_student = models.BooleanField('Is Student', default=False)
    is_mentor = models.BooleanField('Is Mentor', default=False)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class TutorsCourse(models.Model):
    Tid= models.CharField(max_length = 10,blank = True, default='')
    course_id = models.CharField(max_length=10)
    cname = models.CharField(max_length = 20)

class Tutor(models.Model):
    Tid = models.ForeignKey(TutorsCourse,on_delete=models.CASCADE,default="",editable = True)
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 100)

class Mentor(models.Model):
    Mid = models.CharField(max_length = 10)
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 100)

class Student(models.Model):
    A_number = models.CharField(max_length = 9)
    Student_Name = models.CharField(max_length = 20)
    Student_email = models.EmailField()
    Major = models.CharField(max_length = 20)


class Assignments(models.Model):
    A_number = models.ForeignKey(Student, on_delete = models.CASCADE)
    Tid= models.ForeignKey(TutorsCourse, on_delete = models.CASCADE, related_name= 'Tutor_id')
    Assignment_Name = models.CharField(max_length= 10)
    Description = models.CharField(max_length = 20)
    Attach = models.CharField(max_length = 10)
    Subject_Status = models.CharField(max_length = 20)


class Events(models.Model):
    event_id = models.CharField(max_length = 10)
    event_name = models.CharField(max_length = 20)
    event_date = models.DateTimeField(auto_now_add=True)


class Has_Events(models.Model):
    A_number = models.ForeignKey(Student,on_delete = models.CASCADE,related_name = 'Student_number')
    event_id = models.ForeignKey(Events, on_delete = models.CASCADE, related_name = 'Eid')
    event_name = models.ForeignKey(Events, on_delete = models.CASCADE,related_name = 'Ename')
    event_date = models.ForeignKey(Events,on_delete = models.CASCADE,related_name = 'Edate')

class course_registered(models.Model):
    A_number = models.ForeignKey(Student,on_delete = models.CASCADE, related_name = 'CWID')
    Course_id = models.CharField(max_length = 10)
    Course_Name = models.CharField(max_length = 20)

# class User_register(models.Model):
#     User_Email = models.EmailField()
#     Password = models.CharField(max_length = 10)
#     Account_Type = models.CharField(max_length = 10)
#     last_login = models.DateTimeField(blank=True, null=True)

# class User(AbstractUser):
#     CWID = models.CharField(max_length = 9)
#     is_tutor = models.BooleanField('Is Tutor', default=False)
#     is_student = models.BooleanField('Is Student', default=False)
#     is_mentor = models.BooleanField('Is Mentor', default=False)