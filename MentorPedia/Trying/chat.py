# https://www.jnu.ac.in/faculty-profile4/a


import requests
from bs4 import BeautifulSoup
session = requests.Session()
# for char in range(ord('a'), ord('z')+1):
main_url = f"https://www.jnu.ac.in/faculty-profile4/a"    #{chr(char)}
main_request = session.get(main_url)
main_soup = BeautifulSoup(main_request.content, "html.parser")
faculty_image_div = main_soup.find("div", class_="faculty_image")
if faculty_image_div:
    link = faculty_image_div.find("a")
    if link:
        subpage_url = "https://www.jnu.ac.in" + link['href'] 
        # On the subpage
        subpage_request = session.get(subpage_url)
        subpage_soup = BeautifulSoup(subpage_request.content, "html.parser")
        temp = subpage_soup.find_all("div", class_='field__item')
        
        
        print(temp)
        # for item in temp:
        #     content = item.get_text(strip=True)
        #     print("--------------------------------------------------------")
        #     print(content)
        #     print("--------------------------------------------------------")
