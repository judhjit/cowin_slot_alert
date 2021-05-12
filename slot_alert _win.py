from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from playsound import playsound
import ctypes 


def load_refresh():
    #search button
    search_btn = driver.find_element_by_css_selector('.pin-search-btn')
    search_btn.click()

    #18+ btn - enable to look for vacc centers for 18+
    #eighteen_btn = driver.find_element_by_css_selector('div.form-check:nth-child(1) > label:nth-child(2)')
    #eighteen_btn.click()

    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    div_tag = soup.find_all("div", class_= "vaccine-box vaccine-box1 vaccine-padding")

    a_tag_elements = []
    for i in div_tag:
        a_tag_elements.append(i.a.text)
    
    x=0
    y=0
    for i in a_tag_elements:
        if i == " NA " or i == " Booked ":
            x+=1
        else:
            y+=1   
    if y>0:
        # for playing note.mp3 file
        playsound('resources/alert.wav')
        ctypes.windll.user32.MessageBoxW(0, "Apply now, before it goes!", "Slot Available", 2)        
    time.sleep(10)
    
# create object for firefox options
options = Options()

base_url = 'https://www.cowin.gov.in/home'
    
#invoke the webdriver - PLEASE ADD THE PATH HERE
driver = webdriver.Chrome(executable_path = r'<YOUR PATH HERE>/cowin_slot_alert/resources/firefox-win/geckodriver.exe',
                          options = options)
driver.get(base_url)

osiButton = driver.find_element_by_css_selector('.custom-checkbox label div.status-switch')
osiButton.click()

#Click State Button
state_btn = driver.find_element_by_css_selector('div.ng-tns-c64-1:nth-child(2) > div:nth-child(1)')
state_btn.click()

#select State KARNATAKA (option 16)
driver.execute_script("click_event = new CustomEvent('click');" + "btn_element = document.querySelector('#mat-option-16');" + "btn_element.dispatchEvent(click_event);")
time.sleep(1)


#click district button
dis_btn = driver.find_element_by_css_selector('div.ng-tns-c64-3:nth-child(2) > div:nth-child(1)')
dis_btn.click()
time.sleep(1)
#select District BENGALURU URBAN (Option 39)
driver.execute_script("click_event = new CustomEvent('click');" + "btn_element = document.querySelector('#mat-option-39');" + "btn_element.dispatchEvent(click_event);")

while True:
    load_refresh()