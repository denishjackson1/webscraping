import requests
import re
from bs4 import BeautifulSoup

# Read the list of companies from a text file
with open("companies.txt", "r") as f:
    companies = f.read().splitlines()

# print(companies)

# Function to perform a Google search for a given query
def google_search(query):
    response = requests.get(f"https://www.google.com/search?q={query}")
    soup = BeautifulSoup(response.text, "html.parser")
    return [a["href"] for a in soup.find_all("a") if a.has_attr("href")]
# print(google_search(companies))

# Function to find the Twitter URL for a given company
def find_twitter_url(company, search_results):
    for url in search_results:
        if "twitter.com" in url:
            return url
    return None


#Loop through function to search and find_twitter_url
for company in companies:
    search_results = google_search(company)
    twitter_url = find_twitter_url(company, search_results)    
    print(f"{company}: {twitter_url}")