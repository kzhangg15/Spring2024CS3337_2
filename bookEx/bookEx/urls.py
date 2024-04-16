from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from django.urls import path
from django.contrib import admin
from django.urls import include

from django.views.generic.base import TemplateView
from bookMng.views import Register

urlpatterns = [
    path('', views.index, name='index'),
    path('postbook', views.postbook, name='postbook'),
    path('register/success', TemplateView.as_view(
        template_name='registration/register_success.html'),
         name='register success'),
    path('register', Register.as_view(), name='register'),
]


