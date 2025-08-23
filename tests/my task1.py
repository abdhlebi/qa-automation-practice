import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Chrome Webdriver
opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)


def login():
    print("Process Started !!")
    driver.get("https://www.orangehrm.com/en/pricing")


    # # First we need to switch on Iframe
    # iframe_element = driver.find_element(By.NAME, "__uspapiLocator")
    # driver.switch_to.frame(iframe_element)

    driver.find_element(By.XPATH, "//select[@name='NoOfEmployees']/option[3]").click()
    # Scrape info
    info = driver.find_element(By.XPATH, "//div[@class='col-md-5  left-panel d-flex flex-column']").text
    print("Info Text: ", info)

    def write_to_excel(data, excel_file):
        if not os.path.isfile(excel_file):
            # If the file doesn't exist, create a new one with headers
            df = pd.DataFrame([data])  # Wrap data in a list
            df.to_excel(excel_file, index=False)
        else:
            # If the file exists, load the existing data and append new data
            df_existing = pd.read_excel(excel_file)
            df_new = pd.DataFrame([data])  # Wrap data in a list
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
            df_combined.to_excel(excel_file, index=False)

    # Example data
    data = {'Website': 'OrangeHRM', 'Information': info}
    # File path
    excel_file = 'output.xlsx'
    # Write data to Excel
    write_to_excel(data, excel_file)

    breakpoint()

    # username
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/section/section/form/dl[1]/dd/input"))).send_keys('atif@gmail.com')
    # password
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/section/section/form/dl[2]/dd/input"))).send_keys('1234567')
    # Radio button
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/section/section/form/dl[1]/dd/input"))).click()



login()

