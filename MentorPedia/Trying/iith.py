import requests
from bs4 import BeautifulSoup

url = "https://www.iith.ac.in/people/faculty/"
request = requests.get(url)
print(request)
soup = BeautifulSoup(request.content, "html.parser")
tap = soup.find("div", class_="facultycard")
nextlink = tap.find("a")
subpage = "https://www.iith.ac.in/" + nextlink['href']
request1 = requests.get(subpage)
subpagesoup = BeautifulSoup(request1.content, "html.parser")
# Find the site-content div
site_content_div = subpagesoup.find("div", class_="site-content")
# Find the inner div with class col-sm-9 article-post
inner_div = site_content_div.find("div", class_="col-sm-9 article-post")
# Extract information into separate variables
name = inner_div.find('h3').text.strip()
# print(name)
position = inner_div.find("h6").text.strip()
# print(position)
# Corrected selector for departments
departments = [department.text.strip() for department in inner_div.find_all('li', class_='text-left')]
# print(departments)
# phd = inner_div.find('h6', string='Ph.D:').find_next('strong').text.strip()
# print(phd)
# Corrected selector for research interests
research_interests = [interest.text.strip() for interest in inner_div.select('h6:contains("Research Interests:") + div ul li')]
# print(research_interests)
# # Extract email using the correct tag
# email = inner_div.find('a', string='Contact me')['href'].split(':')[1].strip()
# print(email)
# office_address = inner_div.find('h6', string='Office Address:').find_next('div').text.strip()
# office_phone = inner_div.find('h6', string='Office Phone:').find_next('strong').text.strip()
# homepage = inner_div.find('h6', string='Homepage:').find_next('a')['href'].strip()
# print(homepage)
# # Print or use the variables as needed
print("Name:", name)
print("Position:", position)
print("Departments:", departments)
# print("Ph.D:", phd)
# print("Research Interests:", research_interests)
# print("Office Address:", office_address)
# print("Email:", email)
# print("Office Phone:", office_phone)
# print("Homepage:", homepage)
