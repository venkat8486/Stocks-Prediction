import pandas as pd
from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os 
import time


path = 'E:\\SoftwareLife\\webscraping\\Downloads\\'#ticker file path
# df = pd.read_csv(path+'NSE50.csv')
df = pd.read_excel('NIFTY50.xlsx')
tickers = df['Symbol'].unique()
print(tickers)
def home(driver, ticker):
    driver.get("https://www.moneycontrol.com/")

    symbol = driver.find_element_by_id('search_str')
    symbol.send_keys(ticker, Keys.ENTER)
    url = driver.current_url
    titles = ['Balance sheet', 'Profit & Loss', 'Cash Flows', 'Ratios']#rofit &amp; Loss
    r = requests.get(url)
    data = r.content
    soup = BeautifulSoup(data, "html.parser")
    # print(driver.page_source)
    links = dict()
    for title in titles:
        for i in soup.find_all('a',{'title':title}):
            if i is None:
                continue
            links[title] = i['href']
            break
    # print(links, 'links')
    for title, link in links.items():
        df = pd.read_html(link, attrs={'class':'mctable1'})[0]
        title = title.replace(' ','').replace('&','')
        df.head()
        df.to_csv(ticker +'_'+ title +'.txt', index=False, quoting=1)
    

for ticker in tickers:
    chrome_options = webdriver.ChromeOptions()
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
        raise 
    finally:
            
        time.sleep(10)

        driver.close()
    