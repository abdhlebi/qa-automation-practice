from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class YouTubeSearch:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def open_youtube(self):
        self.driver.get("https://www.youtube.com")
        time.sleep(5)

    def search_video(self, query):
        search_box = self.driver.find_element(By.NAME, "search_query")
        search_box.send_keys(query + Keys.ENTER)
        time.sleep(5)

    def verify_title(self, keyword):
        assert keyword.lower() in self.driver.title.lower(), f"'{keyword}' not found in page title"

    def close_browser(self):
        self.driver.quit()
