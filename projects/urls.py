from django.urls import path, include
from . import views
from accounts.views import logout_and_clear

urlpatterns = [
    path('', views.projects_view, name='projects'),
    path('logout/', logout_and_clear, name='logout'),
    # path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
]
