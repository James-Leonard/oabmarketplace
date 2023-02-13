from django.contrib.auth import views as auth_views
from django.urls import path


from . import views
from .forms import LoginForm

app_name = 'home'


urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('contact/', views.contact, name='contact'),
    path('signup1/', views.signup1, name="signup1"),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html', authentication_form=LoginForm), name='login'),
]
