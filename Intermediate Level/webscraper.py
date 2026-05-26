import requests
from bs4 import BeautifulSoup

url = "https://kpmg.com/au/en.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
headings = soup.find_all("h2")
print("Extracted Headings:")

for i, headings in enumerate(headings, start=1):
    print(f"{i}. {headings.text}")
