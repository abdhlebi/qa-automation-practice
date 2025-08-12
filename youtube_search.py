from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def youtube_search():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.youtube.com")

    time.sleep(10)  # Wait for page load

    # Locate the search box by NAME
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("QA Automation with Python")
    search_box.send_keys(Keys.ENTER)

    time.sleep(10)  # Wait for results

    # Verify page title
    youtube_search()