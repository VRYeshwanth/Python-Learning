from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from datetime import date

#These are date formats used to check the announcements
def format_1():
    d = date.today()
    fd = d.strftime("%d-%m")
    return fd
def format_2():
    d = date.today()
    fd = d.strftime("%d/%m/%Y")
    return fd

url = "https://cetonline.karnataka.gov.in/kea/"
browser = webdriver.Chrome()
browser.get(url)
browser.maximize_window()
sleep(2)
btn = browser.find_element(By.XPATH, '//*[@id="ddlLanguage"]/option[2]').click()
sleep(2)
browser.execute_script("window.scrollBy(0,880)", "")
table = browser.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_Gridlatestannoc"]')

#This part of the code scrapes the announcements of the current date and prints them
todays_announcements = []
tr_tags = table.find_elements(By.TAG_NAME, 'tr')
for tr in tr_tags:
    text = tr.text.strip()
    if format_1() in text or format_2() in text:
        todays_announcements.append(text)

if(len(todays_announcements) == 0):
    print("No new announcements at present")
    exit(0)
print("Today's Announcements")
for i, announcement in enumerate(todays_announcements):
    print(f"{i+1}) {announcement}")
sleep(5)