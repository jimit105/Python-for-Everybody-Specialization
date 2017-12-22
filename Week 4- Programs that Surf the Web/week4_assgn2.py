# Following Links in HTML Using BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter URL: ')
html = urlopen(url).read()
count = int(input('Enter count: '))
position = int(input('Enter position: '))

seq_names = []

while count >= 0:
    print("Retrieving: " + url)
    next_page = urlopen(url).read()
    soup = BeautifulSoup(next_page, "html.parser")
    tags = soup('a')
    next_name = tags[position-1].string
    seq_names.append(next_name)
    url = tags[position-1]['href']
    count = count - 1
