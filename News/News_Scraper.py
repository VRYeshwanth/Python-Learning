import os
import requests
from bs4 import BeautifulSoup
import json
from datetime import date

def formatted_date():
    d = date.today()
    fd = d.strftime("%d-%m-%Y")
    return fd

if __name__ == "__main__":
    #Scrape world news
    wp = requests.get("https://www.indiatoday.in/world")
    wp_soup = BeautifulSoup(wp.text, "html.parser")
    wp_grid = wp_soup.find("div", class_ = "story__grid")
    world_news_list = wp_grid.find_all("h2")
    world_news = [ele.text.strip() for ele in world_news_list]
    world_news = list(set(world_news))

    #Scrape national news
    np = requests.get("https://www.indiatoday.in/india")
    np_soup = BeautifulSoup(np.text, "html.parser")
    np_grid = np_soup.find("div", class_ = "story__grid")
    national_news_list = np_grid.find_all("h2")
    national_news = [ele.text.strip() for ele in national_news_list]
    national_news = list(set(national_news))

    #Scrape sports news
    sp = requests.get("https://www.indiatoday.in/sports")
    sp_soup = BeautifulSoup(sp.text, "html.parser")
    sp_grid = sp_soup.find_all("div", class_ = "B1S3_content__thumbnail__wrap__iPgcS")
    sports_news = [i.find("a").text for i in sp_grid]
    sports_news = list(set(sports_news))

    #Scrape tech news
    tp = requests.get("https://www.indiatoday.in/technology")
    tp_soup = BeautifulSoup(tp.text, "html.parser")
    tp_grid = tp_soup.find_all("div", class_ = "B1S3_content__wrap__9mSB6")
    tech_news = [i.find("a").text for i in tp_grid]
    tech_news = list(set(tech_news))

    news = {
        "World News": world_news,
        "National News": national_news,
        "Sports News": sports_news,
        "Tech News": tech_news
    }

    # Get the directory of the currently executing script
    script_dir = os.path.dirname(__file__)

    # Construct the full file path for the JSON file
    json_file_path = os.path.join(script_dir, f"{formatted_date()}.json")

    # Write data to the JSON file
    with open(json_file_path , "w") as f:
        json.dump(news, f, indent=4)
