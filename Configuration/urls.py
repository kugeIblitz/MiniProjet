from django.urls import path
from . import views
urlpatterns = [
    path('login_user',views.login_user,name="login"),
    path('logout_user',views.logout_user,name="logout"),
    path('config_user', views.index, name='config'),
    path('delete_certif/<event_id>', views.delete_certif, name='delete-certif'),
    path('delete_skill/<event_id>', views.delete_Skill, name='delete-skill'),
    path('delete_exp/<event_id>', views.delete_Exp, name='delete-exp'),
    path('update_exp/<event_id>', views.update_Exp, name='update-exp'),
    path('update_skill/<event_id>', views.update_Skill, name='update-skill'),
    path('update_certif/<event_id>', views.update_Certif, name='update-certif'),
    path('add_certif/', views.add_certif, name='Add-certif'),
    path('add_exp/', views.add_exp, name='Add-exp'),
    path('add_Skill/', views.add_Skill, name='Add-skill'),
]