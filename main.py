import requests
from bs4 import BeautifulSoup

website_url = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)').text

soup = BeautifulSoup(website_url,'lxml')

all_content = soup.find("div", class_="reflist")

for i in range(0, 184):
    my_line = all_content.find_all("li")[i].text
    print(i+1, my_line)