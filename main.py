from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_drive_path = "/Users/HPP/Desktop/Programming/chromedriver"

service = Service(chrome_drive_path)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3623302747&f_AL=true&geoId=103263110&keywords=junior%20python%20developer&location=Krak%C3%B3w%2C%20Woj.%20Ma%C5%82opolskie%2C%20Polska&refresh=true&sortBy=R")

account_email = "jakubloboda96@gmail.com"
account_password = ""

login_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
login_button.click()
time.sleep(2)
insert_email = driver.find_element(By.NAME, "session_key")
insert_email.send_keys(account_email)
insert_password = driver.find_element(By.NAME, "session_password")
insert_password.send_keys(account_password)
log_in = driver.find_element(By.CLASS_NAME, "btn__primary--large")
log_in.click()
time.sleep(20)
main_window = driver.current_window_handle

job_offers = driver.find_elements(By.CLASS_NAME, "job-card-container")
# for job in job_offers[1]:
job = job_offers[3]
job.click()
time.sleep(2)
right_side_page = driver.find_element(By.CLASS_NAME, "jobs-search__job-details--container")
apply_button = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
apply_button.click()
time.sleep(2)
next_button_1 = driver.find_element(By.CLASS_NAME, "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
next_button_1.click()
time.sleep(2)
next_button_2 = driver.find_element(By.CLASS_NAME, "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
next_button_2.click()
time.sleep(45)
next_button_3 = driver.find_element(By.CLASS_NAME, "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
next_button_3.click()
time.sleep(2)
next_button_4 = driver.find_element(By.CLASS_NAME, "artdeco-button.artdeco-button--2.artdeco-button--primary.ember-view")
next_button_4.click()
