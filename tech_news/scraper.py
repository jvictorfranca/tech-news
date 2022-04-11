from parsel import Selector
import requests
import time
from .database import create_news


# Requisito 1 bora comecar
def fetch(url):
    try:
        """Seu código deve vir aqui"""
        time.sleep(1)
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return response.text
        elif response.status_code != 200:
            return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    site_URLs = selector.css(
        "h3.tec--card__title .tec--card__title__link::attr(href)"
        ).getall()

    return site_URLs


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    buttonURL = selector.css(
        "div.tec--list--lg a.tec--btn::attr(href)"
        ).get()
    if buttonURL:
        return buttonURL
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)

    title = selector.css("h1.tec--article__header__title::text").get()

    share_count_raw = selector.css(
        "nav.tec--toolbar div.tec--toolbar__item::text"
        ).get()

    share_count_string = "0"
    if share_count_raw is not None:
        share_count_string = share_count_raw.split(sep=" ")[1]

    share_count = int(share_count_string)

    coments_count_string = selector.css(
        "#js-comments-btn::text"
        ).getall()[1].split(sep=" ")[1]
    coments_count = int(coments_count_string)

    categories = [
        category[1:len(category)-1]
        for category in selector.css(
            "#js-categories a.tec--badge::text").getall()
        ]

    sources = [
        source[1:len(source)-1]
        for source in selector.css("div.z--mb-16 a.tec--badge::text").getall()
      ]

    writer_raw = selector.css(
        ".z--font-bold *::text"
        ).get()

    writer = None

    if writer_raw is not None:
        writer = writer_raw
        if writer_raw[0] == " " and writer_raw[-1] == " ":
            writer = writer_raw[1:-1]

    timestamp = selector.css("#js-article-date::attr(datetime)").get()

    summary = ''.join(
        selector.css(
            "div.tec--article__body > p:nth-of-type(1) *::text"
        ).getall()
    )

    url = selector.css("head link:nth-child(26)::attr(href)").get()

    dictToReturn = {
        "title": title,
        "shares_count": share_count,
        "comments_count": coments_count,
        "categories": categories,
        "sources": sources,
        "writer": writer,
        "timestamp": timestamp,
        "summary": summary,
        "url": url
    }
    return dictToReturn


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    curr_html = fetch("https://www.tecmundo.com.br/novidades")
    news_list = scrape_novidades(curr_html)
    while len(news_list) < amount:
        next_page_url = scrape_next_page_link(curr_html)
        curr_html = fetch(next_page_url)
        more_news_urls = scrape_novidades(curr_html)
        news_list = news_list + more_news_urls
    news_list_limited = news_list[:amount]
    news_list_to_return = []
    for new_url in news_list_limited:
        new_html = fetch(new_url)
        new_obj = scrape_noticia(new_html)
        news_list_to_return.append(new_obj)
    create_news(news_list_to_return)
    return news_list_to_return
