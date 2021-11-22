"""Projeto URL Configuration
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
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='publications'), name="logout"),
    path("register/", views.register_request, name="register"),
    path("publications/", views.publications, name="publications"),
    path("insertPublication/", views.insert_pub, name="insert_pub"),
    path("publication/<int:pub_id>/", views.publication, name="publication"),
    path("my_publications/", views.my_publications, name="my_publications"),
    path("pendent_publications/", views.pendent_publications, name="pendent_publications"),
    path("publicationsArquivadas/", views.publicationsArquivadas, name="publicationsArquivadas"),
    path("manage_users/", views.manage_users, name="manage_users"),
    path("favoritos/",views.favoritos, name="favoritos")

]