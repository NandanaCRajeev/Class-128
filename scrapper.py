from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

START_URL="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("chromedriver_win32\chromedriver.exe")
browser.get(START_URL)
time.sleep(10)
headers=["name","light_years_from_earth","planet_mars","stellar_magnitude","discovery_date","hyperlink","planet_type","planet_radius","orbital_radius","orbital_period","eccentricity"]
planet_data=[]
new_planet_data=[]

def scrap():
    for i in range (0,428):
        while True:
            time.sleep(2)
            current_page_num=imt(soup.find_all("input",attrs={"class","page_num"})[0].get("value"))
            
            soup=BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul",attrs={"class","expo planets"}):
            li_tags=ul_tag.find_all ("li")
            temp_list=[]
            for index,li_tags in enumerate(li_tags):
                if index==0:
                    temp_list.append(li_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tags.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_Xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
        print(f"{i} page done 1")
def scrap_more_data(hyperlink):
    try:
        page=request.get(hyperlink)
        soup=BeautifulSoup(page.content,"html.parser")
        temp_list=[]
        for tr_tag in soup.find_all("tr",attrs={"class":"fact_row"}):
            td_tags=td_tags.find_all("td")
            for td_tags in td_tags:
                try:
                    temp_list.append(td_tags.find_all("div",attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_planet_data.append(temp_list)
    except:
        time.sleep(1)
        scrap_more_data(hyperlink)
scrap()
for index,data in enumerate(planet_data):
    scrap_more_data(data[5])
    print(f"{index+1} page done 2") 
final_planet_data=[]
for index,data in enumerate(planet_data):
    new_planet_data_element=new_planet_data[index]
    new_planet_data_element=[elem.replace("\n","") for elem in new_planet_data_element]    
    new_planet_data_element=new_planet_data_element[:7]
    final_planet_data.append(data+new_planet_data)

with open("scrapper.csv","w") as f:
    csvwritter=csv.writer(f)
    csvwritter.writerow(headers)
    csvwritter.writerows(planet_data)