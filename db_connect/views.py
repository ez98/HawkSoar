from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseBadRequest
from db_connect.forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def user_signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            userType = request.POST.get('user_type')
            cwid = request.POST.get('cwid')
            form.save() #user instance is posted to db
            id = form.instance.id #get id of that user instance
            user_profile_instance = UserProfile.objects.get(user_id=id) #get that user created in userprofile table
            
            if userType not in ['student', 'tutor', 'mentor']:
                return HttpResponseBadRequest("Invalid user type")
            else:
                user_profile_instance.__dict__[f"is_{userType}"] = True

            user_profile_instance.save()
            
            return redirect('login_view')
    else:
        form = UserSignUpForm()
    return render(request, 'user_signup.html', {'form': form})    

def role_manager(request):
    user_type = UserProfile.objects.get(user=request.user)
    print("THIS IS THE USER TYPE!!:", user_type)
    if user_type.is_student:
        return render(request, 'student_profile.html', {'user_profile': user_type})
    elif user_type.is_tutor:
        return render(request, 'tutor_profile.html', {'user_profile': user_type})
    elif user_type.is_mentor:
        return render(request, 'mentor_profile.html', {'user_profile': user_type})
    else:
        return HttpResponseBadRequest("Invalid user type")


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #get the email from the login html form
        password = request.POST.get('password') #get the pw from the login html form
        user = authenticate(request, username=username, password=password) #authenticate the user by checking the credentials in the user_register table
        print("USER IS", user)
        if user is not None:
            print("GOT USER,", user.username)
            login(request, user) #if they exists create a new session and log them in
    #         return redirect('events_list') #redirect them to the events they've signed up for
    #     else:
    #         messages.error(request, 'Invalid email or password. Please Try Again')
    # print("Showing Form")
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def events(request):
    events = Events.objects.all()
    return render(request, 'events.html', {'events': events})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events')
    else:
        form = EventForm()
    return render(request, 'event_create.html', {'form': form})

def event_signup(request):
    events = Events.objects.all()
    if request.method == 'POST':
        event_id = request.POST.get('event')
        cwid = request.POST.get('id')
        event = Events.objects.get(pk=event_id)
        student = get_object_or_404(Student, A_number=cwid)
        has_events = Has_Events(A_number=student, event_id=event, event_name=event, event_date=event)
        has_events.save()
        return redirect('events')
    return render(request, 'event_signup.html', {'events': events})

# def user_registation(request):
#     if request.method == 'POST':
#         form = User_register_Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login_view')
#     else:
#         form = User_register_Form()
#     return render(request, 'user_registration.html', {'form': form})


# Create your views here.
# def index(request):
#     return HttpResponse("Welcome to HawkSoar Application")


