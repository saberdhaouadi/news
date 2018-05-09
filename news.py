#!/usr/local/bin/python3
from bs4 import BeautifulSoup
import requests
raw_data = requests.get('http://www.nytimes.com')
text_data = raw_data.text
soup_data = BeautifulSoup(text_data)

for line in soup_data.find_all('h3'):
    print(line.text)
