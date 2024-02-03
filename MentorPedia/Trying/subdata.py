import requests
from bs4 import BeautifulSoup

# # Main page URL
for char in range(ord('a'), ord('z')+1):

    main_url = "https://www.jnu.ac.in/faculty-profile4/"+chr(char)
    main_request = requests.get(main_url)
    main_soup = BeautifulSoup(main_request.content, "html.parser")
    faculty_image_div = main_soup.find("div", class_="faculty_image")
    link = faculty_image_div.find("a")
    subpage_url = "https://www.jnu.ac.in" + link['href']  # Getting subpage link
    # print(subpage_url)

    # On the subpage
    # subpage_url="https://www.jnu.ac.in/content/akmohapatra"
    subpage_request = requests.get(subpage_url)
    subpage_soup = BeautifulSoup(subpage_request.content, "html.parser")

    # Check if the elements exist before trying to extract them
    temp = subpage_soup.find_all("div", class_='field__item')
    temp1=subpage_soup.find("p",class_='field__label')
    # subpage_title = subpage_soup.title.text.strip()
    # print("Subpage Title:", subpage_title)
    print("Printing Content of Website")
    print("----------------------------------------------------")
    for i in temp:
            content = i.get_text(strip=True)
            print(content)

# print(temp)
# Loop through the elements to get contact numbers
# contact_numbers = [element.text.strip() for element in temp ]

# Assuming you want to print all contact numbers found on the page
# print("Contact Numbers:", contact_numbers)

