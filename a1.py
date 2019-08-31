import requests
from bs4 import BeautifulSoup

URL= 'https://www.amazon.in/s?k=keyword&ref=nb_sb_noss_2'

headers={"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}


keyword = input("Enter the item the you want to search: ")
keyword=keyword.strip().replace(" ","+")
URL=URL.replace("keyword" , keyword)

text=requests.get(URL, headers=headers)
soup = BeautifulSoup(text.content, 'html.parser')

tittle = soup.findAll("a" , {"class" : 'a-link-normal a-text-normal'})
price = soup.findAll("span" , {"class" : 'a-offscreen'})

num=1
for item_links in tittle:
        print("-----------------------Item----------------------")
        item_name = item_links.span
        print(item_name.text)
        print("-----------------------Price---------------------")
        print(price[num].text)
        num = num+1
