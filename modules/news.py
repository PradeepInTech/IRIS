# Import required libraries for web scraping and parsing
import requests
from bs4 import BeautifulSoup
#from core import speak, listen

def fetch_website(url:str,headers:dict[str,str]):
    # Fetch HTML content from a website using the provided URL and headers
    try:
        response = requests.get(url, headers)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"The Error:{e}")
        return None

def parse_headlines(html)-> list:
    # Extract news headlines from HTML using BeautifulSoup
    soup = BeautifulSoup(html,'html.parser') 
    # Find all <a> tags with class 'JtKRv' which contain the headlines
    return [a.get_text(strip = True) for a in soup.find_all('a', class_ = 'JtKRv')]

def display_news_headlines(headlines:list):
    # Display headlines in batches of 10 and ask user if they want to see more
    index = 0
    print("="*50)
    print("\tToday's Headlines are as follows:")
    print("="*50)
    while index < len(headlines):
        # Display next 10 headlines
        for i in range(index, index+10):
            print(f"{i+1}. {headlines[i]}")

        index += 10

        # Ask user if they want to see more headlines
        if index < len(headlines):
            choice = input("\nWould you like to hear more? yes or no:").lower()
            if choice != 'yes':
                print("\nSource: Google News")
                break
           
        print("\n")
        print("="*50)


def headlines():
    # Main function to fetch and display news headlines from Google News
    url = "https://news.google.com/search?pz=1&cf=all&hl=en-IN&q=india&gl=IN&ceid=IN:en"
    # Headers to mimic browser request
    headers = {"User-Agent": "Mozilla/5.0"}
    html = fetch_website(url, headers)
    if html:
        headlines = parse_headlines(html)
        display_news_headlines(headlines)

if __name__ == "__main__":
    headlines()