from webbrowser import Chrome
import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://klio.webuntis.com"
path = "C:\Program Files (x86)/chromedriver.exe"
options = Options()
options.add_argument("headless")
#options = webdriver.ChromeOptions()
#options.add_argument("headless")
#options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#driver = webdriver.Chrome(path, options=options)
driver.get(url)
time.sleep(1.0)
print("after get url")

###############################################################################################################################

schoolParent = driver.find_element(By.CLASS_NAME, "Select-input")
schoolInput = schoolParent.find_elements(By.XPATH, "*")[0]
schoolInput.send_keys("HTBLA Mössingerstr.")
schoolInput.send_keys(Keys.RETURN)
print("after schoolInput")

###############################################################################################################################

#driver.get(url)
doc = bs(driver.page_source, "html.parser")
driver.close()
print(doc.prettify())
