from bs4 import BeautifulSoup

html_code = """
<div class="col-sm-9 article-post">
    <h3 style="color: #d1402a;">Aalok Dinkar Khandekar</h3>
    <h6><strong>Position: </strong>Assistant Professor</h6>
    <h6><strong>Department(s): </strong></h6>
    <div style="margin:auto; padding:0 1vw;">
        <ul style="padding-left:0;">
            <li class="text-left" style="font-size:14px; margin:0">
                Liberal Arts
            </li>
            <li class="text-left" style="font-size:14px; margin:0">
                Climate Change
            </li>
        </ul>
    </div>
    <h6><strong>Ph.D: </strong>Rensselaer Polytechnic Institute</h6>
</div>
"""

# Parse the HTML content
soup = BeautifulSoup(html_code, 'html.parser')

# Extract information
name = soup.h3.text.strip()
position = soup.find('h6').text.strip()
departments = [department.text.strip() for department in soup.find_all('li', class_='text-left')]

# Create a summary (scrap)
summary = f"{name},{position},{','.join(departments)}"

print("Scraped Information:", summary)
