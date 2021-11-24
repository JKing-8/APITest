"""APITest URL Configuration

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
from django.urls import path, re_path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout, name='logout'),
    path('feedback/', views.feedback, name='feedback'),
    path('help/', views.help_doc, name='feedback'),
    re_path(r"^child/(?P<eid>.+)/(?P<oid>.*)/(?P<ooid>.*)/$", views.child),
    path('prolist/',views.project_list,name='project_list'),
    path('delpro/<int:id>/',views.del_project,name='del_project'),
    path('addpro/',views.add_project,name='add_project'),
    path('apis/<int:id>',views.apis,name='apis')

]
