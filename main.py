import time
import PySimpleGUI as pg
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

listTestsThisWeek = []
listTestsNextWeek = []
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
time.sleep(1.0)
schoolInput.send_keys(Keys.RETURN)
time.sleep(0.8)

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
        time.sleep(1.0)

WebDriverWait(driver, 60).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"embedded-webuntis")))
time.sleep(0.5)
legend = driver.find_elements(By.CLASS_NAME, "un-timetable-legend__cell")
for element in legend:
    if element.text == "Prüfung":
        testColor = element.value_of_css_property("background-color")[:16]
lessons = driver.find_elements(By.CLASS_NAME, "renderedEntry")
for element in lessons:
    if element.value_of_css_property("background-color")[:16] == testColor:
        listTestsThisWeek.append(element.find_element(By.XPATH, "./div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/span").get_attribute("innerHTML"))
buttons = driver.find_elements(By.CSS_SELECTOR, "button[type=button]")
for element in buttons:                                  
    if element.get_attribute("class") == "btn btn-default":
        if element.find_element(By.XPATH, "./*").get_attribute("class") == "un-icon fa fa-arrow-right":
            element.click()
time.sleep(1.5)
lessons = driver.find_elements(By.CLASS_NAME, "renderedEntry")
for element in lessons:
    if element.value_of_css_property("background-color")[:16] == testColor:
        listTestsNextWeek.append(element.find_element(By.XPATH, "./div/table/tbody/tr[2]/td/table/tbody/tr[2]/td[1]/span").get_attribute("innerHTML"))

testsThisWeek = ""
for element in listTestsThisWeek:
    testsThisWeek = testsThisWeek + element + ", "
testsThisWeek = testsThisWeek[:-2]

testsNextWeek = ""
for element in listTestsNextWeek:
    testsNextWeek = testsNextWeek + element + ", "
testsNextWeek = testsNextWeek[:-2]

pg.theme("DarkBlue14")

layout = [
    [pg.Text("Tests in dieser Woche:")],
    [pg.Text(str(testsThisWeek))],
    [pg.Text("Tests in der nächsten Woche:")],
    [pg.Text(str(testsNextWeek))],
    [pg.Button("exit", size=(20, 2))]
]

window = pg.Window("pop-up", layout, size=(250, int(layout.__len__()) * 35), element_justification="l")
while True:
    event , values = window.read()
    match event:
        case "exit":
            window.close()
            break