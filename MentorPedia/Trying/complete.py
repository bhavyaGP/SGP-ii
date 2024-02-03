import os
import requests
from bs4 import BeautifulSoup
import json

# Specify the directory path where you want to save the JSON files
output_directory = r"C:\Users\91878\Documents\22CE103\SGP-2\MentorPedia\Trying\jsonfiles"

url = "https://www.iith.ac.in/people/faculty/"
request = requests.get(url)

soup = BeautifulSoup(request.content, "html.parser")
faculty_cards = soup.find_all("div", class_="facultycard")

for idx, card in enumerate(faculty_cards):
    nextlink = card.find("a")
    subpage = "https://www.iith.ac.in/" + nextlink['href']
    
    request1 = requests.get(subpage)
    subpagesoup = BeautifulSoup(request1.content, "html.parser")

    site_content_div = subpagesoup.find("div", class_="site-content")
    test_text = site_content_div.find("div", class_="col-sm-9 article-post").get_text().split('\n')
    scraped_text = list(filter(None, list(map(str.strip, test_text))))

    info = {}
    info['name'] = scraped_text[0]
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

    # Generate a unique filename for each faculty member
    filename = f"faculty_info_{idx + 1}.json"
    
    # Specify the full path for the JSON file
    file_path = os.path.join(output_directory, filename)
    
    # Save info to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(info, json_file, indent=4)

    print(f"Data for faculty member {idx + 1} has been saved to {file_path}.")
