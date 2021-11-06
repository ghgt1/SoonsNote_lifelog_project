"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls.conf import re_path
from . import views #현재디렉토리내에있는 views를 가져와라

urlpatterns = [
    path('', views.index),
    path('profiles', views.index),
    re_path(r'^profiles/$', views.detail),
    path('profiles/<int:pk>/', views.life_env),
    path('profiles/<int:pk>/ai_talk', views.ai_talk),
    path('profiles/<int:pk>/health_anal', views.health_anal),
]