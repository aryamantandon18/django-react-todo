from django.urls import path
from . import views

# Define your URL patterns here
urlpatterns = [
    path('getUser/', views.UserViews.getUser, name='getUser'),
    path('signup/', views.UserViews.signup, name="signup"),
    path('login/',views.UserViews.login, name="login"),
    path('verify/',views.UserViews.verify_otp, name="verifyOtp"),
    path('getTasks/<str:user_id>/',views.TaskViews.getTasks, name="getTasks"),
    path('updateTask/<str:task_id>/',views.TaskViews.updateTask),
    path('createTask/',views.TaskViews.createTask),
    path('deleteTask/<str:task_id>/',views.TaskViews.deleteTask)
    # path('new/', views.UserCreateView.as_view(), name='Register'),
]

