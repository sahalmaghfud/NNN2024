from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import time

# Configure Edge WebDriver to run in headless mode
options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")  # Disable GPU acceleration

# Set up the path to the Edge WebDriver
service = Service("C:\\Users\\Sahal Maghfud\\Downloads\\edgedriver_win32\\msedgedriver.exe")

# Initialize the Edge WebDriver with the Service object and options
driver = webdriver.Edge(service=service, options=options)

def scrape_website(url):
    # Open the website in headless mode
    driver.get(url)
    
    # Wait for the page to load
    time.sleep(3)  # Adjust time as necessary

    # Get the full HTML of the page
    html = driver.page_source

    # Use BeautifulSoup to parse the HTML and extract text
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()  # Extract text without HTML tags

    # Close the driver after scraping
    driver.quit()

    # Write the extracted text to a .txt file
    with open("sd_text.txt", "w", encoding="utf-8") as file:
        file.write(text)

# Call the function with the URL you want to scrape
scrape_website("https://www.ihoki7.com/")
