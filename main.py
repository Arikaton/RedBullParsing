from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

driver = webdriver.Chrome('C:\\Users\\User\\chromedriver')

def find_number(link):
    driver.get(link)
    time.sleep(3)
    num = driver.page_source
    nums = BeautifulSoup(num, "html.parser")
    final_number = nums.find(class_="votes-total-team").em.text

    return final_number

url = "https://flugtag.redbull.com/ru/ru/news/"
main_page = requests.get(url)

soup = BeautifulSoup(main_page.text, "html.parser")

container = soup.find(class_="swiper-container")

link = container.find_all(class_="text")

all_links = []

i = 1
for l in link:
    numer = find_number(l['href'])
    all_links.append((l.div.h4.text, numer))
    print(str(i), l.div.h4.text, numer, end='\n')
    i += 1

f = open('balls.txt', 'w')

for l in all_links:
    f.write(l[0]+" " +l[1] + '\n')
f.close()

