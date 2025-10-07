from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import requests

# Get LambdaTest credentials from environment variables
USERNAME = os.getenv("LT_USERNAME")
ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

# LambdaTest Grid URL
grid_url = f"https://{USERNAME}:{ACCESS_KEY}@hub.lambdatest.com/wd/hub"

# Desired capabilities inside LT:Options
lt_options = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "platformName": "Windows 11",
    "tunnel": True,
    "tunnelName": "auto-tunnel",  # Must match your GitHub Actions tunnel name
    "build": "Locally Hosted Tunnel",
    "name": "Localhost Site Test",
}

# Create ChromeOptions and set LambdaTest options
options = webdriver.ChromeOptions()
options.set_capability("LT:Options", lt_options)

# Wait until the local server is up
local_url = "http://127.0.0.1:5500/index.html"
for i in range(10):
    try:
        requests.get(local_url)
        print("✅ Local server is ready!")
        break
    except requests.exceptions.ConnectionError:
        print("Waiting for local server to start...")
        time.sleep(2)
else:
    print("❌ Local server did not start in time.")
    exit(1)

# Initialize Remote WebDriver
driver = webdriver.Remote(
    command_executor=grid_url,
    options=options
)

try:
    # Open local website
    driver.get(local_url)
    
    # Print page title
    print("Page title:", driver.title)
    
    # Locate and print heading text
    heading = driver.find_element(By.TAG_NAME, "h1").text
    print("Heading text:", heading)
    
    time.sleep(5)  # Pause to see the page
finally:
    driver.quit()
    print("✅ Test completed and driver closed.")
