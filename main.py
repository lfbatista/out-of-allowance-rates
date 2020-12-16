import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait

FIREFOXDRIVER_PATH = "/usr/bin/"
options = FirefoxOptions()
options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = Firefox(options=options)
driver.get("http://www.three.co.uk/Support/Roaming_and_international/Roaming_abroad")

elem = driver.find_element_by_xpath("//input[@id='input-append-demo']")

elem.clear()
elem.send_keys("portugal")
elem.send_keys(Keys.RETURN)

# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "input.input-append-demo"))).send_keys("portugal")
# # driver.find_element_by_css_selector("a.desktop-submit").click()
# elem.send_keys(Keys.RETURN)
# # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.title-title")))
# print(driver.current_url)


print(elem.text, elem)
time.sleep(2)
elem2 = driver.find_element_by_xpath("//h1[@class='margin-top1']")
print(elem2.text)

driver.close()
