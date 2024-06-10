from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_Academy_Award%E2%80%93winning_films"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find("table")
cell = table.find_all("td")

cell_list = [i.text.strip() for i in cell]
film_name = [name for i,name in enumerate(cell_list) if i % 4 == 0]
film_year = [year for i,year in enumerate(cell_list) if i % 4 == 1]
film_awards = [award for i,award in enumerate(cell_list) if i % 4 == 2]
film_nomination = [nom for i,nom in enumerate(cell_list) if i % 4 == 3]

data = {
    "Film": film_name,
    "Year": film_year,
    "Awards": film_awards,
    "Nominations": film_nomination
}

df = pd.DataFrame(data)
print(df)