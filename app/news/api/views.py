from news.models import News, Categories
from django.http import JsonResponse

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

def getAllNews(request, page):
    news = News.objects.filter().order_by('-published_at')
    page_size = 10
    page_start = page_size * (page - 1)
    page_end = page_size * page
    news = news[page_start:page_end]

    data = []

    for article in news:
        data.append({
            'id': article.id,
            'author': article.author,
            'title': article.title,
            'category': article.category,
            'description': article.description,
            'url': article.url,
            'source_id': article.source_id,
            'source_name': article.source_name,
            'published_at': article.published_at,
            'content': article.content,
            'image_url': article.image_url,
        })

    return JsonResponse(data, safe=False)

def getCategories(request):
    categories = Categories.objects.filter()
    
    data = []

    for category in categories:
        data.append({
            'id': category.id,
            'name': category.name,
            'slug': category.slug,
            'value': category.value,
        })

    return JsonResponse(data, safe=False)