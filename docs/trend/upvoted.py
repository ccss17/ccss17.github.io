from requests import Session
from bs4 import BeautifulSoup
from getpass import getpass

s = Session()
s.post('https://news.ycombinator.com/login', data = {'acct' : 'chansol0505', 'pw' : getpass()})

UPVOTED  = 'https://news.ycombinator.com/upvoted?id=chansol0505'
html = s.get(UPVOTED).text
soup = BeautifulSoup(html, 'html.parser')

titles = soup.findAll('a', {'class' : 'storylink'})
dates = soup.findAll('span', {'class' : 'age'})

items = {}
for title, date in zip(titles, dates):
    items[date['title']] = (title.text, title['href'])

from pprint import pprint
pprint(items)