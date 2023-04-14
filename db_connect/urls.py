from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.user_registation, name='user_registation'),
    path('', views.user_signup, name='user_signup'),
    path('login/', views.login_view, name='login_view'),
    path('role_manager/', views.role_manager, name='role_manager'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/', views.events, name='events'),
    path('events/signup/', views.event_signup, name='event_signup'),
]
urlpatterns += staticfiles_urlpatterns()
