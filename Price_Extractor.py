from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
import time

Names = []
Prices = []
Ratings = []

for i in range(1,21):
    url = f"https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    main_div = soup.find("div", class_ = "DOjaWF gdgoEp")
    data_div = main_div.find_all("div", class_ = "yKfJKb row")
    for i in data_div:
            name_div = i.find("div", class_ = "KzDlHZ")
            rating_div = i.find("div", class_ = "XQDdHH")
            price_div = i.find("div", class_ = "Nx9bqj _4b5DiR")

            Names.append(name_div.text.strip() if name_div else None)
            Prices.append(price_div.text.strip() if price_div else None)
            Ratings.append(rating_div.text.strip() if rating_div else None)
    
    time.sleep(2)

data = {
    "Name of Product": Names,
    "Price": Prices,
    "Rating": Ratings
}

df = pd.DataFrame(data)
print(df)
df.to_excel("Laptop_Prices.xlsx")