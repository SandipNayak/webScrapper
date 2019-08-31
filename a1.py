import requests
from bs4 import BeautifulSoup

headers={"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
text=requests.get('https://www.amazon.in/s?k=mobile&ref=nb_sb_noss_2', headers=headers)

soup = BeautifulSoup(text.content, 'html.parser')
tittle = soup.findAll("span" , {"class" : 'a-size-medium a-color-base a-text-normal'})
price = soup.findAll("span" , {"class" : 'a-price-whole'})

num = len(tittle)

for i in range(num):
        print("-----------------------Item----------------------")
        print(tittle[i].text.strip())
        print("-----------------------Price---------------------")
        print(price[i].text)
