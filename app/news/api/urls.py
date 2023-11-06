from django.urls import path
from news.api import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),

    path('get-all-news/', views.getAllNews, name='get-all-news'),
]
