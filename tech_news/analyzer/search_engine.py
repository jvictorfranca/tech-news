from ..database import find_news

# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    all_news = find_news()
    print(all_news)
    filtered_news = [
        (new["title"], new["url"])
        for new in all_news if title.lower() in new["title"].lower()
    ]
    return filtered_news


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
