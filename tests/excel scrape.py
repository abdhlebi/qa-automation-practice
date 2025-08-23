import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach", True)               #

driver = webdriver.Chrome(options=opt)                                #

driver.get("https://www.orangehrm.com/en/pricing")


WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/section/section/form/dl[1]/dd/input"))).send_keys('atif@gmail.com')
info = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/section[1]/div/div/div[1]/h1').text


data = {'Website': 'OrangeHRM', 'Information': info}
excel_file = 'output.xlsx'


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

write_to_excel(data, excel_file)