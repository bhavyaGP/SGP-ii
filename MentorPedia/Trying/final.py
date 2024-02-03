from bs4 import BeautifulSoup
import requests
# Your HTML code
url = "https://www.iith.ac.in/people/faculty/"
request = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(request.content, 'html.parser')

# Find all div elements with class "facultycard"
faculty_cards = soup.find_all('div', class_='facultycard')

# Initialize a list to store information dictionaries for each faculty
faculty_info_list = []

# Loop through each faculty card and extract information
for card in faculty_cards:
    info = {}    
    # Extracting faculty name
    faculty_name = card.find('h3').text.strip()
    info['name'] = faculty_name
    
    # Extracting position (e.g., Assistant Professor)
    position =card. find("h6").text.strip()
    info['position'] = position
    
    # Extracting education (e.g., Ph.D: IIT Madras)
    education = card.find_all('h6').text.strip()  # Adjust the index based on your HTML structure
    info['education'] = education
    
    # Extracting research interests (e.g., Environmental Engineering, Catalysis, Climate Change)
    research_interests = [li.text.strip() for li in card.find_all('li')]
    info['research_interests'] = research_interests

    # Append the faculty information to the list
    faculty_info_list.append(info)

# Process the extracted faculty information using your provided code
for faculty_info in faculty_info_list:
    test_text = faculty_info['name']  # Adjust this line based on the key used for the faculty name
    scraped_text = list(filter(None, list(map(str.strip, test_text))))

    faculty_details = {}
    faculty_details['name'] = scraped_text[0]
    current_key = None

    for line in scraped_text:
        if line.startswith('Room:'):
            continue

        if ':' in line:
            current_key, *current_value = line.split(':')
            current_key = current_key.strip()
            current_value = ":".join(current_value).strip()

            if current_key in ['Department(s)', 'Research Interests', 'Office Address']:
                faculty_details[current_key.lower()] = []
            else:
                faculty_details[current_key.lower()] = current_value
        elif current_key in ['Department(s)', 'Research Interests', 'Office Address']:
            if line.strip():
                faculty_details[current_key.lower()].append(line.strip())

    # Print or use the processed faculty details as needed
    print(faculty_details)

