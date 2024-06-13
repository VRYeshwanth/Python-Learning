from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime

def date_format():
    months  = {
        "January": "1","February": "2","March": "3","April": "4","May": "5","June": "6","July": "7","August": "8","September": "9","October": "10",
        "November": "11","December": "12"
    }
    d = datetime.now()
    fd = d.strftime("%d, %Y")
    m = str(d.month)
    month = ""
    for i,j in months.items():
        if j == m:
            month = i
    
    fd = f"{month} {fd}"
    return fd

browser = webdriver.Chrome()
browser.get("https://www.isical.ac.in/~admission/")
browser.maximize_window()
sleep(1)
browser.execute_script("window.scrollBy(0,450)", "")
sleep(2)
table = browser.find_element(By.XPATH, '//*[@id="content"]/section/ul')
li_list = table.find_elements(By.TAG_NAME, 'li')
date = date_format()
print("-----------------------------------------------------------------------")
for tag in li_list:
    if date in tag.text.strip():
        print(tag.text.strip())
        exit(0)
print("No new announcements")
print("-----------------------------------------------------------------------")
browser.quit()