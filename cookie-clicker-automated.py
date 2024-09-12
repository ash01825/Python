from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def product_available(driver):
    try:
        product=driver.find_element(By.CSS_SELECTOR,".product.unlocked.enabled")
        return True
    except:
         return False
def crate_upgrade(driver):
    try:
        create=driver.find_element(By.CSS_SELECTOR,".crate.upgrade.enabled")
        return True
    except:
         return False



driver = webdriver.Safari()
driver.get("https://orteil.dashnet.org/cookieclicker/")

eng_lang = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "langSelectButton")))
eng_lang.click()
count=0

while True:
    try:
        big_cookie = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))
        
        driver.execute_script("arguments[0].click();", big_cookie)
        time.sleep(0.1)
        # print(num_of_cookies(driver))
        if product_available(driver):
            product=driver.find_element(By.CSS_SELECTOR,".product.unlocked.enabled")
            driver.execute_script("arguments[0].click();", product)

        if crate_upgrade(driver):
             upgrade=driver.find_element(By.CSS_SELECTOR,".crate.upgrade.enabled")
             driver.execute_script("arguments[0].click();", upgrade)


        
    except Exception as e:
        print(e)
        break

input("Press Enter to exit...")
