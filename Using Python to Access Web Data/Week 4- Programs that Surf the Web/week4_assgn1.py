from urllib.request import urlopen
from bs4 import BeautifulSoup

#url = input('Enter - ')
url = "http://py4e-data.dr-chuck.net/comments_37086.html"
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

numbers = []
tags = soup('span')
for tag in tags:
    numbers.append(int(tag.string))
print(sum(numbers))
