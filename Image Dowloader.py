import requests
from bs4 import BeautifulSoup
import os

from requests.api import request

url = 'http://www.epath3d.com/templates.php'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
images = soup.find('div', class_='col-md-12 row templates_list')
images2 = images.find_all('a')
for img in images2:
    link = img['href']
    name = img['title']
    with open(link.replace('templates', '').replace(' ', '_').replace('/',''), 'wb') as f:
        out = requests.get('http://www.epath3d.com/' + link)
        f.write(out.content)
        print('Writing: ', name)