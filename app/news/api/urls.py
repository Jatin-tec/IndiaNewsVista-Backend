from django.urls import path
from news.api import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),

    path('get-all-news/<int:page>', views.getAllNews, name='get-all-news'),
    path('get-categories/', views.getCategories, name='get-categories'),
]
