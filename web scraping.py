import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website
response = requests.get('https://www.wikipedia.org/')

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Step 3: Extract the data
data = soup.find_all('h1')  # For example, getting all <h2> elements

# Step 4: Save the data
extracted_data = [item.get_text().strip() for item in data]
with open('web_scraping.txt', 'w') as file:
    for item in extracted_data:
        print(item)
        file.writelines(str(item)+'\n')

