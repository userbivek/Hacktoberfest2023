import requests
from bs4 import BeautifulSoup

# The URL of the website to scrape
url = "http://quotes.toscrape.com"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract and process data from the webpage
    quotes = soup.select(".text")
    authors = soup.select(".small")

    for quote, author in zip(quotes, authors):
        print(f"Quote: {quote.get_text()}\nAuthor: {author.get_text()}\n")
else:
    print("Failed to retrieve the web page.")

