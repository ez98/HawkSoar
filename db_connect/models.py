from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager 
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     cwid = models.CharField(max_length=9)
#     is_tutor = models.BooleanField('Is Tutor', default=False)
#     is_student = models.BooleanField('Is Student', default=False)
#     is_mentor = models.BooleanField('Is Mentor', default=False)

#     def __str__(self):
#         return self.user.username
    
# @receiver(post_save, sender=User)
# def create_user(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


# Extending the base User manager that Django uses for its original UserManager.
# Defining the same 3 methods that the original Django UserManager has.
# Not using username in either of those methods.
# Validating that email is provided when creating a User.
# Assigning the new Manager to the User model.
class UserManager(BaseUserManager):
    #Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        #Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        #Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        #Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    ROLES = (
        ('', 'Select Your Role'),
        ('student', 'Student'),
        ('tutor', 'Tutor'),
        ('mentor', 'Mentor'),
    )
    
    username = None
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.CharField(max_length=10, choices=ROLES, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    Tid = models.CharField(max_length = 9)
    email = models.CharField(max_length = 100)

class TutorsCourse(models.Model):
    Tid = models.ForeignKey(Tutor,on_delete=models.CASCADE,default="",editable = True)
    course_id = models.CharField(max_length=10)
    cname = models.CharField(max_length = 20)

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default="")
    Mid = models.CharField(max_length = 9)
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 100)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    A_number = models.CharField(max_length = 9)
    Student_Name = models.CharField(max_length = 20)
    Student_email = models.EmailField()
    Major = models.CharField(max_length = 50)

class Assignments(models.Model):
    A_number = models.ForeignKey(Student, on_delete = models.CASCADE)
    Tid = models.ForeignKey(Tutor, on_delete = models.CASCADE, related_name= 'Tutor_id')
    Assignment_Name = models.CharField(max_length= 10)
    # from datetime import date
    # from myapp.models import MyModel

    # my_date = date(2022, 5, 15)
    # my_instance = MyModel(Due_Date=my_date)
    Due_Date = models.DateField(null=True)
    Description = models.CharField(max_length = 20)
    Attach = models.CharField(max_length = 10)
    Submit_Status = models.CharField(max_length = 20, default="Not Submitted")

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