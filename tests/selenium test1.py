import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")
opt.add_experimental_option("detach", True)               #if there is any error the browser stay open or time.sleep()

driver = webdriver.Chrome(options=opt)                                #

driver.get("https://www.orangehrm.com/en/pricing")

def fill_data():                              #
    WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="Form_getForm_FullName"]'))).send_keys('Atif Naveed')
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="Form_getForm_Contact"]'))).send_keys('12345678')
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="Form_getForm_Email"]'))).send_keys('atif@gmail.com')
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="Form_getForm_CompanyName"]'))).send_keys('abdul company')
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="Form_getForm_Country"]/option[4]'))).click()
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="Form_getForm_NoOfEmployees"]/option[3]'))).click()
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]'))).click()
    WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="Form_getForm_action_submitForm"]'))).click()


fill_data()










