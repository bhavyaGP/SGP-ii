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
print(inner_div)