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
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)
time.sleep(1.0)

###############################################################################################################################

schoolParent = driver.find_element(By.CLASS_NAME, "Select-input")
schoolInput = schoolParent.find_elements(By.XPATH, "*")[0]
schoolInput.send_keys("HTBLA Mössingerstr.")
time.sleep(0.6)
schoolInput.send_keys(Keys.RETURN)
time.sleep(1.0)
userInputs = driver.find_elements(By.CLASS_NAME, "un-input-group__input")
for element in userInputs:
    if element.get_attribute("type") == "text":
        element.send_keys("22651649")
    elif element.get_attribute("type") == "password":
        element.send_keys("htlMeinzh3f!")
        element.send_keys(Keys.RETURN)
time.sleep(1.0)
buttons = driver.find_elements(By.CLASS_NAME, "item-container")
time.sleep(0.5)
for element in buttons:
    if element.text == "Mein Stundenplan":
        element.click()
time.sleep(1.5)
thisWeek = bs(driver.page_source, "html.parser")
# time.sleep(5.0)
# buttons = driver.find_elements(By.CSS_SELECTOR, "button[type=button]")
# for element in buttons:
#     print(element.get_attribute("class"))                                     come back later...
#     if element.get_attribute("class") == "btn btn-default":
#         print("should work...")
time.sleep(6.0)

###############################################################################################################################

#print(thisWeek.prettify())
