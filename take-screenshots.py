# quick python script to take screenshots of urls
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
import os

# Path to the file containing the URLs, one per line
URLS_FILE = "/home/kali/bounty/subdomain-enum/live_hosts.txt"

# Directory to save the screenshots
OUTPUT_DIRECTORY = "/tmp/screenshots"

# Function to take a screenshot of a URL
def take_screenshot(url, output_file):
    options = Options()
    options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    driver.save_screenshot(output_file)
    driver.quit()

if __name__ == "__main__":
    # Create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    with open(URLS_FILE, "r") as f:
        urls = f.readlines()

    for i, url in enumerate(urls):
        output_file = os.path.join(OUTPUT_DIRECTORY, f"screenshot_{i+1}.png")
        take_screenshot(url, output_file)
        print(f"Screenshot taken for URL {url} and saved as {output_file}")
