from django.contrib import admin
from django.urls import path
from app import views
app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout, name='logout'),
    path('feedback/', views.feedback, name='feedback'),
    path('help/', views.help_doc, name='feedback'),
    path('prolist/', views.project_list, name='project_list'),
    path('delpro/<int:id>/', views.del_project, name='del_project'),
    path('addpro/', views.add_project, name='add_project'),
    path('apis/<int:id>', views.apis_detail, name='apis'),
    path('projectset/<int:id>', views.get_project_set, name='get_project_set'),
    path('projectsave/<int:id>',views.save_project_set,name='save_project_set'),
    path('cases/<int:id>',views.get_cases,name='get_cases'),
    path('addapi/<int:id>', views.add_api, name='add_api'),
    path('delapi/<int:id>',views.del_api,name='del_api')
]
