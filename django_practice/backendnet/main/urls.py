from django.urls import path
from . import views
# from django.http import HttpResponse


urlpatterns = [
    path('', views.home, name="home"),
    path('article/<str:pk>/', views.article, name='article')
] 