from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from selenium import webdriver

Names = []
Prices = []
Ratings = []

for i in range(10):
    sleep(2)
    url = f"https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i+1}"
    browser = webdriver.Chrome()
    browser.get(url)
    sleep(2)
    browser.maximize_window()
    soup = BeautifulSoup(browser.page_source, "html.parser")
    sleep(2)
    table = soup.find("div", class_ = "DOjaWF gdgoEp")
    rows = table.find_all("div", class_ = "cPHDOP col-12-12")
    if i == 0:
        l = len(rows)-2
    else:
        l = len(rows)-1
    rows = rows[:l]
    sleep(2)
    for row in rows:
        name = row.find("div", class_ = "KzDlHZ")
        price = row.find("div", class_ = "Nx9bqj _4b5DiR")
        rating = row.find("div", class_ = "XQDdHH")
        if name == None:
            continue
        else:
            Names.append(name.text.strip() if name else "None")
            Prices.append(price.text.strip() if price else "None")
            Ratings.append(rating.text.strip() if rating else "None")
    print(f"Page {i+1} scraped")
    browser.quit()

data = {
    "Name of Product": Names,
    "Price": Prices,
    "Rating": Ratings
}
df = pd.DataFrame(data)
print(df)
df.to_excel("Laptop Prices.xlsx", index=False)