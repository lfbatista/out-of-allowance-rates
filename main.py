import time

import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

FIREFOXDRIVER_PATH = "/usr/bin/"
options = FirefoxOptions()
options.add_argument('--headless')
# options.add_argument('--disable-gpu')

driver = Firefox(options=options)
driver.get("http://www.three.co.uk/Support/Roaming_and_international/Roaming_abroad")

elem = driver.find_element_by_xpath("//input[@id='input-append-demo']")

countries = ["Brazil", "South Africa", "Portugal", "Chile", "Iceland", "China", "Madagascar"]
country = countries[1]

elem.clear()
elem.send_keys(country)
elem.send_keys(Keys.RETURN)

time.sleep(4)

if country == "South Africa":
    elem2 = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div/div/div[3]/section[2]/article[1]/section[2]/table")
    data = elem2.get_attribute("outerHTML")

    df = pd.read_html(data)
    dfs = pd.concat(df)

    print(f"Out of allowance rates for {country}:")
    print(f"Calling back to the UK: {dfs.values[0][1]}")
    print(f"Texting back to the UK: {dfs.values[2][1]}")
    print(f"Receiving a call: {dfs.values[4][1]}")
    print(f"Using internet data: {dfs.values[6][1]}")

else:
    elem2 = driver.find_element_by_xpath("//div[1]/section[2]/div[2]/div/table")
    data = elem2.get_attribute("outerHTML")

    df = pd.read_html(data)
    dfs = pd.concat(df)
    print(dfs.values[0][1])

    print(f"Out of allowance rates for {country}:")
    print(f"Calling back to the UK: {dfs.values[0][2]}")
    print(f"Texting back to the UK: {dfs.values[2][2]}")
    print(f"Receiving a call: {dfs.values[5][2]}")
    print(f"Using internet data: {dfs.values[6][2]}")
