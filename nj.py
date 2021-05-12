from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.get('https://njhealth.maps.arcgis.com/apps/MapSeries/index.html?appid=50c2c6af93364b4da9c0bf6327c04b45&folderid=e5d6362c0f1f4f9684dc650f00741b24')

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div[1]/ul/li[2]/button")))
print("Here")
driver.find_elements_by_xpath("/html/body/div[3]/div/div[1]/ul/li[2]/button").click()
casespath = "/html/body/div/div/div/div[2]/div/div/div/margin-container/full-container/div[9]/margin-container/full-container/div/div/div/div[2]/svg/g[2]/text"
cases = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, casespath)))
print(cases)
