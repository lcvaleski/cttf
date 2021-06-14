from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://njhealth.maps.arcgis.com/apps/dashboards/2ec0d7d96a18451bb60acfed3e76e563')
time.sleep(10)

data = driver.find_elements_by_tag_name("text")
for e in data:
    if str(e.getCssValue("color") == '002673':
        print(str(e.get_attribute("innerHTML").strip()))
        break
driver.quit()
