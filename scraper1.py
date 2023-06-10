from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("C:/Users/Dell/Desktop/pro 12/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():

    soup = BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table = soup.find("table",attrs={'class','wikitable_sortable'}) 
    
   
    temp_list = []
    rows = bright_star_table.find_all('tr')

    for row in rows :
        cols = row.find_all('td')
        temp_list = []

        for col in cols :
            data = col.text.rstrip()
            temp_list.append(data)


    scraped_data.append(temp_list)

  

        
# Calling Method    
scrape()
stars_data = []

for i in range (0,len(scraped_data)):
    stars_data.append([scraped_data[i][0],scraped_data[i][5],scraped_data[i][7],scraped_data[i][8]])

# Define Header
headers = ['Star_name','Distance','Mass','Radius']
df = pd.DataFrame(stars_data,columns=headers)
df.to_csv('dwarf_data.csv',index=True,index_label='id')