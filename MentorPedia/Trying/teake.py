from bs4 import BeautifulSoup
import requests
# Your HTML code
url = "https://www.iith.ac.in/people/faculty/"
request = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(request.content, 'html.parser')

# Find all div elements with class "facultycard"
faculty_cards = soup.find_all('div', class_='facultycard')
# print(faculty_cards)
# Loop through each faculty card and extract information
for card in faculty_cards:
    # Extracting image source
    img_src = card.find('img')['src']
    
    # Extracting faculty name
    faculty_name = card.find('h5').text.strip()
    
    # Extracting position (e.g., Assistant Professor)
    position = card.find('strong').text.strip()
    
    # Extracting education (e.g., Ph.D: IIT Madras)
    education = card.find('h6').text.strip()
    
    # Extracting research interests (e.g., Environmental Engineering, Catalysis, Climate Change)
    research_interests = [li.text.strip() for li in card.find_all('li')]
    
    # Print or use the extracted information as needed
    print(f"Faculty Name: {faculty_name}")
    print(f"Position: {position}")
    print(f"Education: {education}")
    print(f"Research Interests: {', '.join(research_interests)}")
    print(f"Image Source: {img_src}")
    print("\n")
