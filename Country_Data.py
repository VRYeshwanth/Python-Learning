from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.scrapethissite.com/pages/simple/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

countries = []
capitals = []
population = []
area = []

country_list = soup.find_all("h3", class_="country-name")
country_capital = soup.find_all("span", class_="country-capital")
country_population = soup.find_all("span", class_="country-population")
country_area = soup.find_all("span", class_="country-area")

for i in country_list:
    countries.append(i.text.strip())
for i in country_capital:
    capitals.append(i.text.strip())
for i in country_population:
    population.append(i.text.strip())
for i in country_area:
    area.append(i.text.strip())

data = {
    "Country": countries,
    "Capital": capitals,
    "Population": population,
    "Area (in sq.km)": area
}

df = pd.DataFrame(data) #Displays data in tabular form
pd.set_option("display.max_rows", None) #Allows to print all rows
print(df)