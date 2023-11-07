import requests
from news.models import News, Categories

# Init
api_key='f08aee49b1674761a4bc07bb93ca6cbc'
country = "in"
variants = ['top-headlines', 'everything', 'sources']
categories = Categories.objects.all()
language="hn"

def fetch_news(variant, country, category):
    if category == "all":
        url = f'https://newsapi.org/v2/{variant}?country={country}&apiKey={api_key}&language={language}'
    else: 
        url = f'https://newsapi.org/v2/{variant}?country={country}&category={category}&apiKey={api_key}&&language={language}'
    
    x = requests.get(url)
    return x.json()

# categories = Categories.objects.all()

def populate_news_headlines():

    for category in categories:
        if category.value:
            headlines = fetch_news(variants[0], country, category.value)
            for headline in headlines['articles']:
                News.objects.create(
                    author = headline['author'] if headline['author'] else "Unknown",
                    title = headline['title'] if headline['title'] else "Unknown",
                    category = category.name,
                    description = headline['description'] if headline['description'] else "Unknown",
                    url = headline['url'] if headline['url'] else "Unknown",
                    source_id = headline['source']['id'] if headline['source']['id'] else "Unknown",
                    source_name = headline['source']['name'] if headline['source']['name'] else "Unknown",
                    published_at = headline['publishedAt'] if headline['publishedAt'] else "Unknown",
                    content = headline['content'] if headline['content'] else "Unknown",
                    image_url = headline['urlToImage'] if headline['urlToImage'] else "Unknown",
                )
            print(headlines)


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