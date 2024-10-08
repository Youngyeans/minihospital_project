from django.urls import path
from authen.views import LoginView, LogoutView, RegisterView, ValidationView, TestView

app_name = 'authen'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('validation/', ValidationView.as_view(), name='validation'),
    path('test/', TestView.as_view(), name='test'),
]