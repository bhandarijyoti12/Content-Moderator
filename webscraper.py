# pip install selenium beautifulsoup4
# imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
from selenium.common.exceptions import NoSuchElementException
 
path="/Users/Abiral/Downloads/"
chromedriver_path = path+'chromedriver.exe'
service = Service(path+'chromedriver.exe')
options = Options()
options.add_argument("--headless")
 
# function
def scrape_page_text(url:str):
    # create driver
    driver = webdriver.Chrome(executable_path=path+'chromedriver',
     options=options)
    # launch driver
    driver.get(url)
    sleep(3)
   
    # get soup from driver page
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
   
    # scrape all the text from page
    text = soup.get_text()
    text = text.replace("\n", "")
   
    return(text)
