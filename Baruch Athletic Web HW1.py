import requests
from bs4 import BeautifulSoup
URL = "https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster"
page = requests.get(URL)

# to check the status of your request type page into the cell and press enter page
soup = BeautifulSoup(page.content,'html.parser')

page.content
print(soup.prettify())