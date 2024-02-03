# https://www.flipkart.com/search?q=headphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off

import pandas as pd
import requests
from bs4 import BeautifulSoup

Name=[]
Price=[]
Information=[]
Rating=[]
# for i in range(2,10):
    # Request
url="https://www.flipkart.com/search?q=headphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
request=requests.get(url)
# print(request)
# soup=BeautifulSoup(request.text,"html.parser")
soup=BeautifulSoup(request.content,"html.parser")
# print(soup)
elements1 = soup.find_all("a", attrs={'class': 's1Q9rs'})
Name = [element.text.strip() for element in elements1]
# print(names[0])
# print(Name[0])
# templink=names[0].get('href')
# print(templink)
# finalLink='https://www.flipkart.com'+templink
# print(finalLink)
elements2=soup.find_all("div", attrs={'class': '_30jeq3'})
Price= [element.text.strip() for element in elements2]
# print(Price[0])
elements3=soup.find_all("div",attrs={'class':'_3LWZlK'})
Rating=[element.text.strip() for element in elements3]
# print(Rating[0])
for i in range(min(len(Name), len(Price), len(Rating))):
    print("Name:", Name[i],)
    print("Price:", Price[i])
    print("Rating:", Rating[i])
    print("------")
    
    

    
    

    # while True:
    # nextPage=soup.find("a",class_="_1LKTO3").get("href")
    # finalPage="https://www.flipkart.com/"+nextPage
    # print(finalPage)
    # url=finalPage
    # r=requests.get(url)
    # soup=BeautifulSoup(r.text,"lxml")
