
import requests
from bs4 import BeautifulSoup
import pandas as pd


def typical_scrape(urls):
    print(urls)
    url_datas = list()
    for url in urls:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        print(soup.prettify().split('meta content'))
        #print(text)
        #data = pd.DataFrame(text)
        #url_datas.append(data)
    return url_datas

def alter_dict():
    pass


if __name__ == "__main__":
    string = input()
    words = string.split(' ')
    URLS = ["https://www.dictionary.com/browse/pirate","https://www.thesaurus.com/browse/pirate"]
    database = typical_scrape(URLS)
    print(database)
