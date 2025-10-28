from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# LambdaTest credentials from environment variables
USERNAME = os.getenv("LT_USERNAME")
ACCESS_KEY = os.getenv("LT_ACCESS_KEY")

# LambdaTest Grid URL
grid_url = f"https://{USERNAME}:{ACCESS_KEY}@hub.lambdatest.com/wd/hub"

lt_options = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "platformName": "Windows 11",
    "tunnel": True,
    "tunnelName": "6f849d94-abb2-4db3-b770-5c6d2c7e8e34",
    "build": "Local Tunnel Test",
    "name": "Localhost Site Test",
}

options = webdriver.ChromeOptions()
options.set_capability("LT:Options", lt_options)

driver = webdriver.Remote(
    command_executor=grid_url,
    options=options
)

try:
    driver.get("http://127.0.0.1:5500/index.html")
    print("Page title:", driver.title)
    heading = driver.find_element(By.TAG_NAME, "h1").text
    print("Heading text:", heading)
    time.sleep(5)
finally:
    driver.quit()
