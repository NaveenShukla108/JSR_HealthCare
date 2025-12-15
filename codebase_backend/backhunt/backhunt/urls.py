"""
URL configuration for backhunt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core.views import RegisterViewset, LoginViewset
from rest_framework.routers import DefaultRouter


router_v1 = DefaultRouter()

router_v1.register('register', RegisterViewset, basename="register")
router_v1.register('login', LoginViewset, basename="login")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(router_v1.urls), name="v1")
]
