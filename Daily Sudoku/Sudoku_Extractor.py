import requests
from bs4 import BeautifulSoup
import os
url = "https://www.7sudoku.com/"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

img_html = soup.find("img")
img_src = "https://7sudoku.com{}".format(img_html["src"])
img_name = img_html["src"].split("puzzles/")[1]
flag = requests.get(img_src)

current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, img_name)

with open(file_path, "wb") as f:
    f.write(flag.content)