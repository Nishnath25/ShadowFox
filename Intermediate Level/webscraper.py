import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://kpmg.com/au/en.html"

# Send request
response = requests.get(url)

# Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all quote blocks
headings = soup.find_all("h2")

print("Extracted Headings:")

# Print headings
for i, headings in enumerate(headings, start=1):
    print(f"{i}. {headings.text}")