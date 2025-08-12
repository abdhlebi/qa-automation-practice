import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_youtube_search(driver):
    driver.get("https://www.youtube.com")
    time.sleep(5)  # Let the page load

    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("SDET Automation Tutorial" + Keys.ENTER)

    time.sleep(5)  # Wait for results

    assert "youtube" in driver.title.lower(), "Expected 'youtube' to be in the page title"
