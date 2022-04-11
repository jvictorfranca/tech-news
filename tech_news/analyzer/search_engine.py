from ..database import find_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    all_news = find_news()
    filtered_news = [
        (new["title"], new["url"])
        for new in all_news if title.lower() in new["title"].lower()
    ]
    return filtered_news


# Requisito 7'
def search_by_date(date):
    """Seu código deve vir aqui"""
    all_news = find_news()
    date_array = date.split("-")
    if int(date_array[1]) > 12 or int(date_array[2]) > 31:
        raise(ValueError("Data inválida"))
    if int(date_array[1]) == 2 and int(date_array[2]) > 28:
        raise(ValueError("Data inválida"))
    filtered_news = [
        (new["title"], new["url"])
        for new in all_news if new["timestamp"].split("T")[0] == date
    ]

    return filtered_news


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""
    all_news = find_news()
    filtered_news = [
        (new["title"], new["url"])
        for new in all_news if source.lower() in [
            source.lower() for source in new["sources"]
            ]
    ]
    return filtered_news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    all_news = find_news()
    filtered_news = [
        (new["title"], new["url"])
        for new in all_news if category.lower() in [
            category.lower() for category in new["categories"]]
    ]
    return filtered_news
