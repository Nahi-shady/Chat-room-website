from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginPage, name='login'),

    path('', views.home, name='home'),
    path('room/<int:pk>/', views.room, name='room'),
    path('user-profile/<int:pk>/', views.user_profile, name='user-profile'),
    path('create-room/', views.createRoom, name='create-room'),
    path('update-room/<int:pk>/', views.update_room, name='update-room'),
    path('delete-room/<int:pk>/', views.delete_room, name='delete-room'),
    path('delete-message/<int:pk>/', views.delete_message, name='delete-message'),
    path('topics/', views.home, name='topics'),
    path('update-user/', views.update_user, name='update-user'),
    path('topic/', views.topicPage, name='topic'),
    path('activity/', views.activityPage, name='activity'),
]
