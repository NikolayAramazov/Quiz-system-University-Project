from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('register/', views.register, name='register'),
    path('logout/', views.sign_out, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='profile_edit'),
]