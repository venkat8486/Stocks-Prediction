import pandas as pd
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os 
import time

path = 'E:\\SoftwareLife\\webscraping\\Downloads\\'#ticker file path
df = pd.read_excel('NIFTY50.xlsx')
tickers = []
for tic in df['Company Name'].unique():
    tic = tic.replace('é','e').replace("'",'').replace(".",'')
    tickers.append(tic)
print(tickers)
def home(driver, ticker):
    driver.get("https://www.moneycontrol.com/stocks/histstock.php")

    symbol = driver.find_element_by_id('mycomp')
    symbol.send_keys(ticker, Keys.ENTER)
    time.sleep(2)

    ele = driver.find_element_by_link_text(ticker)
    ele.click()

    ele = driver.find_element_by_name('frm_yrly_yr') 
    ele.send_keys(2000)
    count = 0
    for ele in driver.find_elements_by_tag_name('input'):
        if 'go_btn.gif' in ele.get_attribute('src'):
            count += 1
            if count == 3:
                ele.click()
                break
    if count != 3:
        print(ticker, "no third src")
        return
    data = driver.page_source
    df = pd.read_html(data, attrs={'class':'tblchart'})[0]
    df.to_csv(ticker +'_history.txt', index=False, quoting=1)

for ticker in tickers:
    download_path = os.path.join(r'C:\Users\venka\OneDrive\Desktop\Data Science - HarvardX\Stocks Prediction - Project\Script_Output',str(ticker))#download path
    if not os.path.exists(download_path):
        os.mkdir(download_path)
    # options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    #  'options.binary_location':r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    prefs = {'download.default_directory' : download_path,}#options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        
    options = Options()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"    #chrome binary location specified here
    options.add_argument("--start-maximized") #open Browser in maximized mode
    options.add_argument("--no-sandbox") #bypass OS security model
    options.add_argument("--disable-dev-shm-usage") #overcome limited resource problems
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\venka\AppData\Local\Temp\chromedriver_win32\chromedriver.exe')
    # options = webdriver.ChromeOptions()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--ignore-ssl-errors')
    # driver = webdriver.Chrome(chrome_options=options)

    try:
        home(driver, ticker)
    except :
        print(ticker, " Error at this level") 
    finally:
        driver.close()
    