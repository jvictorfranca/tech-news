from parsel import Selector
import requests
import time


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


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
