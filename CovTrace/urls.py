"""CovTrace URL Configuration

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
from django.urls import path, include

from tracer.views import Register,Signup,ViewHome,ViewReport,ViewTracingForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ViewHome,name='home'),
    path('home/',ViewHome,name='home'),
    path('administration/report',ViewReport,name='report'),
    path('administration/update',ViewTracingForm,name='update'),
    # path('adminlogin/',ViewAdminLogin,name='adminlogin'),
    # path('studentlogin/',ViewStudentLogin,name='studentlogin'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/register',Register, name='register'),
    path('accounts/signup/',Signup, name='signup'),
]