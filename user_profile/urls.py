from django.urls import path
from .import views

urlpatterns = [
    path('login_user/', views.login_user, name="login_user"),
    path('singup/',views.singup, name="singup" ),
    path('logout_user/',views.logout_user, name="logout_user" ),
    path('forgot_password/', views.forgot_password, name="forgot_password"),
    path("user_profile/", views.user_profile, name="user_profile"),
    path("change_prfile_picture/", views.change_profile_picture, name="change_prfile_picture"),
    path("change_banner/", views.change_banner, name="change_banner"),
    path("Store/<str:username>/", views.Store, name="Store"),
    path('follow_or_unfollow/<int:user_id>/', views.follow_or_unfollow_user, name = "follow_or_unfollow_user"),
    path('user_notifications/', views.user_notifications, name = "user_notifications"),

    path('Adress/', views.Adress, name="Adress"),
    path('DeleteAddress/<int:id>/', views.DeleteAddress, name="DeleteAddress"),
    path('EditAddress/<int:id>/', views.EditAddress, name="EditAddress"), 

    
]