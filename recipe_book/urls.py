"""recipe_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .pages.create_recipe_page import CreateRecipePage
from . import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.home, name='home'),
  path('welcome/', CreateRecipePage.as_view(), name='welcome'),
  path('callback', views.callback, name='callback'),
  path('signin', views.sign_in, name='signin'),
  path('signout', views.sign_out, name='signout'),
]