from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def google_search():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")

    time.sleep(15)  # wait for page to load

    # ✅ Use XPath for the search box
    search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

    # Enter text
    search_box.send_keys("QA Automation with Python")

    # Submit the form
    search_box.submit()

    time.sleep(15)  # wait to see the result

    driver.quit()

google_search()
