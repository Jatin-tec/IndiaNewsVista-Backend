import requests
from news.models import News, Categories

# Init
api_key='f08aee49b1674761a4bc07bb93ca6cbc'
country = "in"
variants = ['top-headlines', 'everything', 'sources']

def fetch_news(variant, country, category):
    if category == "all":
        url = f'https://newsapi.org/v2/{variant}?country={country}&apiKey={api_key}'
    else: 
        url = f'https://newsapi.org/v2/{variant}?country={country}&category={category}&apiKey={api_key}'
    
    x = requests.get(url)
    return x.json()

# categories = Categories.objects.all()

def populate_news_headlines():
    headlines = fetch_news(variants[0], country, None)
    print(headlines)

    for headline in headlines['articles']:
        News.objects.create(
            author = headline['author'],
            title = headline['title'],
            description = headline['description'],
            url = headline['url'],
            source_id = headline['source']['id'],
            source_name = headline['source']['name'],
            published_at = headline['publishedAt'],
            content = headline['content'],
            image = headline['urlToImage'],
        )

# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# # /v2/top-headlines/sources
# sources = newsapi.get_sources()