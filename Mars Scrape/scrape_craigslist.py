from bs4 import BeautifulSoup
import requests
 
def scrape():
    listings = {}

    url = "https://raleigh.craigslist.org/search/hhh?max_price=1500&availabilityMode=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    listings["headline"] = soup.find("a", class_="result-title").get_text()
    listings["price"] = soup.find("span", class_="result-price").get_text()
    listings["hood"] = soup.find("span", class_="result-hood").get_text()

    return listings