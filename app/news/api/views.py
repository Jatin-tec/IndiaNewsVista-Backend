from django.shortcuts import render
from rest_framework.response import JsonResponse

def getRoutes(request):
    routes = [
        'api/news/',
        'api/news/create/',
        'api/news/upload/',
        'api/news/<str:pk>/reviews/',
        'api/news/top/',
        'api/news/<str:pk>/',
        'api/news/delete/<str:pk>/',
        'api/news/update/<str:pk>/',
    ]
    return JsonResponse(routes, safe=False)