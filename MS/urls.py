from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='accounts/login.html'
    
    ), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('success/', views.success, name='success'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),  
    path('register/', views.register, name='register'),
    path('UG_update/', views.ug_Update, name='UG_update'),
    path('biodataupdate/', views.biodateupdate, name='biodataupdate'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('e_activation/', views.e_activation, name='e_activation'),




    
]