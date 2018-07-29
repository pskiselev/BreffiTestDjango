from bs4 import BeautifulSoup
import requests


def get_worth():

    resp = requests.get('http://breffi.ru/ru/about')
    dom_text = resp.text
    soup = BeautifulSoup(dom_text, 'lxml')

    worth_divs = soup.find('div', {'class': 'content-section worth'})

    child = worth_divs.findChildren("div", recursive=False)[0]

    items = child.find_all("div", {'class': 'content-section__item'})

    for item in items:
        number = int(item.find('div', {'class': 'content-section__itemnumber'}).text)
        title = item.find('div', {'class': 'content-section__itemtitle'}).text
        text = item.find('div', {'class': 'content-section__itemtext'}).text

        yield {'number': number, 'title': title, 'text': text}

