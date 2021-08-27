"""mainproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
# from choiceapp import views as cvapp
# from pageapp import views as pgapp


urlpatterns = [
    path('',include('pdf.urls')),
    # path('login/',pgapp.login,name='login'),
    # path('pdf/',include('pdf.urls')),
    # path('notes/',include('to_do_project.urls')),
    # path('choice/',cvapp.index,name='choice'),
    path('admin/', admin.site.urls),
]
