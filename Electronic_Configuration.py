# This script helps me extract the electronic configurations of all the elements of the periodic table

from bs4 import BeautifulSoup
import requests
import json
import os
import time
try:
    url_1 = "https://en.wikipedia.org/wiki/Electron_configurations_of_the_elements_(data_page)"
    page_1 = requests.get(url_1)
    soup_1 = BeautifulSoup(page_1.text, "html.parser")

    url_2 = "https://en.wikipedia.org/wiki/List_of_chemical_elements"
    page_2 = requests.get(url_2)
    soup_2 = BeautifulSoup(page_2.text, "html.parser")

    table_1 = soup_1.find("table", class_ = "wikitable")
    tr_division = table_1.find_all("tr")[2:]
    tr_division = [tag for i,tag in enumerate(tr_division) if i % 3 == 1]

    td_list = [i.text for i in tr_division]
    #Code for cleaning the list
    for j in range(2,8):
        var1 = f'\n{j}'
        var2 = f' {j}'
        td_list = [i.replace(var1, var2) for i in td_list]
    for j in range(4,8):
        var1 = f'\n {j}'
        var2 = f' {j}'
        td_list = [i.replace(var1, var2) for i in td_list]
    td_list = [i.replace('\n1', '1') for i in td_list]
    td_list = [i.replace('\n', '') for i in td_list]

    table_2 = soup_2.find("table")
    cell = table_2.find_all("td")
    all_cells = [i.text.strip() for i in cell]
    symbol = []
    for i,ele in enumerate(all_cells):
        if i % 16 == 1:
            symbol.append(ele)
    
    print("Data fetched Succesfully")
except Exception as e:
    print(f"ERROR: {e}")
    exit(0)

time.sleep(1)
data = {}
file_dir = os.path.dirname(__name__)
file_path = os.path.join(file_dir, f"Electronic_Configuration.json")
for i in range(118):
    sym = symbol[i]
    config = td_list[i]
    data[sym] = config
txt = "Exporting data to JSON file"
for i in range(4):
    print('\r' + txt + '.' * i, end='', flush=True)
    time.sleep(2)
with open(file_path, "w") as f:
    json.dump(data, f, indent=4)
print("\nExport Successful")