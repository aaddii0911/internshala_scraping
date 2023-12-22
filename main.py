import requests
from bs4 import BeautifulSoup
import requests
import gspread
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
import selenium.webdriver as webdriver
import time
from datetime import datetime
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service

def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def close_popup(driver):
    try:
        close_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "close_popup"))
        )
        close_button.click()
    except:
        print('No popup')

def scrape(driver):
    data = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    jobs = soup.find_all('div', class_='container-fluid individual_internship visibilityTrackerItem')

    for job in jobs:
        job_details = scrape_details(job)
        data.append(job_details)

    return data

def scrape_details(job):
    details = {'Date': datetime.today().strftime('%Y-%b-%d')}

    try:
        details['Title'] = job.find('h3', class_='heading_4_5 profile').text.strip()
    except:
        details['Title'] = 'No Info'

    try:
        details['Company'] = job.find('h4', class_='heading_6 company_name').text.strip()
    except:
        details['Company'] = 'No Info'

    try:
        details['Location'] = job.find('a', class_='location_link view_detail_button').text.strip()
    except:
        details['Location'] = 'No Info'

    try:
        details['CTC Range'] = job.find('div', class_='item_body salary').text.strip()
    except:
        details['CTC Range'] = 'No Info'

    try:
        details['Experience'] = job.find('div', class_='item_body desktop-text').text.strip()
    except:
        details['Experience'] = 'No Info'

    try:
        details['Starts'] = job.find('div', class_='start-date-first').text.strip()
    except:
        details['Starts'] = 'No Info'

    details['Link'] = 'https://internshala.com' + job.find('div', class_='individual_internship_header').find('a', class_='view_detail_button').text.strip()

    return details

def navigate(driver, total_pages):
    all_jobs = []
    for page in range(total_pages):
        all_jobs.extend(scrape(driver))
        try:
            next_button = driver.find_element(By.ID, "next")
            next_button.click()
            time.sleep(3)
        except:
            break
    return all_jobs

driver = setup()
driver.get("https://internshala.com/fresher-jobs/")
time.sleep(3)
close_popup(driver)

url = 'https://internshala.com/fresher-jobs/analytics-jobs/'
driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
total_pages = int(soup.find('span', {'id': 'total_pages'}).text)

data = navigate(driver, total_pages)

df = pd.DataFrame(data)
df.to_csv('internshala_data.csv', index=False)
