import requests
from bs4 import BeautifulSoup as Soup
from collections import Counter


def funck(soup):
    tags = soup.find_all(['div', 'h2', 'p', 'ul', 'li', 'a'])
    flag = False
    for tag in tags:
        if " ".join(tag.text.split()) == 'Следующая страница':
            flag = True
            continue
        if flag:
            list = tag.text.split('\n')
            return Counter(s[0] for s in list[1:])


contents = requests.get('https://cutt.ly/vxqt34w').text
soup = Soup(contents, 'lxml')
dict_letters = funck(soup)

flag = True
while flag:
    allLinks = soup.find(id="bodyContent").find_all(['li', 'a'])
    link = "https://ru.wikipedia.org" + allLinks[-7]['href']
    contents = requests.get(link).text
    soup = Soup(contents, 'lxml')
    new_dict = funck(soup)
    for key, value in new_dict.items():
        if key == 'A':
            flag = False
        elif key in dict_letters:
            dict_letters[key] += value
        else:
            dict_letters[key] = value

for key in sorted(dict_letters.keys()):
    print(key, ':', dict_letters[key])