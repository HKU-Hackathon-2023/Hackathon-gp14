"""
URL configuration for GenAI_Hackathon project.

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
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('classroom', views.classroom, name='classroom'),
    path('note', views.note, name='note'),
    path('bookmark', views.bookmark, name='bookmark'),
    path('dailychallenge', views.dailychallenge, name='dailychallenge'),
    path('courses/<str:course>/<str:topic>/', views.courses, name='courses'),

    path('chat', views.chat, name='chat'),
    path('chat/<str:classroom>', views.chat, name='chat'),
    path('crearCourse', views.crearCourse, name='crearCourse'),    
    path('setting', views.setting, name='setting'),

    path('voice_to_text', views.voice_to_text, name='voice_to_text')
]