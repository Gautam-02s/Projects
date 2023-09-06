import requests
from bs4 import BeautifulSoup

url="https://www.flipkart.com/"
r=requests.get(url)
print(r)
soup=BeautifulSoup(r.content,"html.parser")
print(soup)
names=soup.find_all("div", {"class": "_1xHGtK _373qXS"})
for l in names:
    name = names.find("div", {"class": "_3wU53n"}).text
    price = names.find("div", {"class": "_1vC4OE _2rQ-NK"}).text

    # Print the name and price of the product
    print("Name:", name)
    print("Price:", price)