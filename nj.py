from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='C:/Users/Logan/Desktop/chromedriver.exe')
driver.get('https://njhealth.maps.arcgis.com/apps/dashboards/2ec0d7d96a18451bb60acfed3e76e563')
time.sleep(10)

#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[2]/div/div/div/margin-container/full-container/div[10]/margin-container/full-container/div/div/div/div[2]/svg/g[2]/text")))
data = driver.find_elements_by_tag_name("text")
for e in data:
    print(str(e.get_attribute("innerHTML").strip()))
driver.quit()
