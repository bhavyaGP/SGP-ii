import requests
from bs4 import BeautifulSoup

url = "https://www.iith.ac.in/people/faculty/"
request = requests.get(url)
soup = BeautifulSoup(request.content, "html.parser")
tap = soup.find_all("div", class_="facultycard")
# nextlink= tap.find_all("a")
print(tap)
# tap = soup.find("div", class_="facultycard")