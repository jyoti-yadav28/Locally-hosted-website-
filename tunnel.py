from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# LambdaTest credentials
USERNAME = "jyotiyadav"
ACCESS_KEY = "LT_QADsSrkYtrtgR0gOQKfoxZuVqQTm1DXlbHy0Vo9JkOzJwpe"

# LambdaTest Grid URL
grid_url = f"https://jyotiyadav:LT_QADsSrkYtrtgR0gOQKfoxZuVqQTm1DXlbHy0Vo9JkOzJwpe@hub.lambdatest.com/wd/hub"

# Desired capabilities inside LT:Options
lt_options = {
    "browserName": "Chrome",
    "browserVersion": "latest",
    "platformName": "Windows 11",
    "tunnel": True,
    "tunnelName": "6f849d94-abb2-4db3-b770-5c6d2c7e8e34",  # Must match your tunnel
    "build": "locally tunnel",
    "name": "Localhost Site Test",
}

# Create ChromeOptions and set LambdaTest options
options = webdriver.ChromeOptions()
options.set_capability("LT:Options", lt_options)

# Initialize Remote WebDriver
driver = webdriver.Remote(
    command_executor=grid_url,
    options=options
)

try:
    # Open local website (served via localhost or 127.0.0.1)
    driver.get("http://127.0.0.1:5500/index.html")
    
    # Print page title
    print("Page title:", driver.title)
    
    # Locate and print heading text
    heading = driver.find_element(By.TAG_NAME, "h1").text
    print("Heading text:", heading)
    
    time.sleep(5)  # Wait to see the page
finally:
    driver.quit()
