# https://www.jnu.ac.in/faculty-profile4/d


import pandas as pd
import requests
from bs4 import BeautifulSoup

    
for char in range(ord('a'), ord('z')+1):
    url = "https://www.jnu.ac.in/faculty-profile4/" + chr(char)
    request=requests.get(url)
    # print(request)

    soup = BeautifulSoup(request.content, 'html.parser')
    # print(soup)   
    temp1=soup.find_all("div",class_='faculty_name')
    Name = [element.text.strip() for element in temp1]


    temp2=soup.find_all("div",class_='faculty_designation')
    designation = [element.text.strip() for element in temp2]


    temp3=soup.find_all("div",class_='faculty_email')
    mails = [element.text.strip() for element in temp3]

    temp4=soup.find_all("div",class_='faculty_school')
    School = [element.text.strip() for element in temp4]


    min_length = min(len(Name), len(designation), len(mails), len(School))

    # Print the information in tabular form using iteration
    for i in range(min_length):
        print("Name:", Name[i])
        print("Designation:", designation[i])
        print("Email:", mails[i])
        print("School:", School[i])
        print("------")