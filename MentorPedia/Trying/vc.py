import requests
from bs4 import BeautifulSoup

url = "https://www.iith.ac.in/people/faculty/"
request = requests.get(url)
# print(request)

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
test_text=site_content_div.find("div", class_="col-sm-9 article-post").get_text().split('\n')
scraped_text = list(filter(None,list(map(str.strip, test_text))))

info = {}
info['name']=scraped_text[0]
current_key = None

for line in scraped_text:
    if line.startswith('Room:'):
        continue

    if ':' in line:
        current_key, *current_value = line.split(':')
        current_key = current_key.strip()
        current_value = ":".join(current_value).strip()

        if current_key == 'Department(s)' or current_key == 'Research Interests' or current_key == 'Office Address':
            info[current_key.lower()] = []
        else:
            info[current_key.lower()] = current_value
    elif current_key in ['Department(s)', 'Research Interests', 'Office Address']:
        if line.strip():
            info[current_key.lower()].append(line.strip())

print(info)