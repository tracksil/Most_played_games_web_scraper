from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import time


URL = 'https://steamdb.info/graph/'
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"


def render_page(url):
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(url)
    time.sleep(3)
    render = driver.page_source
    driver.quit()
    return render


r = render_page(URL)
soup = BeautifulSoup(r, "html.parser")
games = soup.find_all(class_='app')

header = ['ID', 'Name', 'Current', '24h Peak', 'All-Time Peak']

with open("Most_played_now.csv", "w", encoding='UTF8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for game in games:
        g = game.text.split('\n')
        g_list = [g[1], g[3], int(g[4].replace(',', '')), int(g[5].replace(',', '')), int(g[6].replace(',', ''))]

        writer.writerow(g_list)
