from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_chemical_elements"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

table = soup.find("table")
cell = table.find_all("td")
all_cells = [i.text.strip() for i in cell]

z = []
symbol = []
name = []
block = []
for i,ele in enumerate(all_cells):
    if i % 16 == 0:
        z.append(ele)
    elif i % 16 == 1:
        symbol.append(ele)
    elif i % 16 == 2:
        name.append(ele)
    elif i % 16 == 6:
        block.append(ele)

data = {
     "Atomic No": z,
     "Symbol": symbol,
     "Name": name,
     "Block": block
}

df = pd.DataFrame(data)
pd.set_option("display.max_rows", None)
print(df)