import time
import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

COUNTRIES = ["South Africa", "Brazil", "South Africa", "Portugal", "Chile", "Iceland", "China", "Madagascar"]
# FIREFOXDRIVER_PATH = "/usr/bin/"

# Selenium Configs
options = FirefoxOptions()
options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = Firefox(options=options)


def search_country(country):
    driver.get("http://www.three.co.uk/Support/Roaming_and_international/Roaming_abroad")
    search_bar = driver.find_element_by_xpath("//input[@id='input-append-demo']")

    search_bar.clear()
    search_bar.send_keys(country)
    search_bar.send_keys(Keys.RETURN)


def get_allowance_rates(path):
    """
    :param path: xpath
    :return: list of table values
    """
    table_ele = driver.find_element_by_xpath(path)

    table_data = table_ele.get_attribute("outerHTML")
    df = pd.read_html(table_data)

    return pd.concat(df)


# TODO
#  - save country allowance rates into dictionary
#  - move out prints from loop
#  - add logger
for i, country in enumerate(COUNTRIES):
    search_country(COUNTRIES[i])
    time.sleep(4)

    if COUNTRIES[i] in ("South Africa", "China", "Madagascar"):
        dfs = get_allowance_rates("/html/body/div[1]/div/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div/div/div/div["
                                  "3]/section[2]/article[1]/section[2]/table")

        print(f"Out of allowance rates for {country}: \n"
              f"Calling back to the UK: {dfs.values[0][1]} \n"
              f"Texting back to the UK: {dfs.values[2][1]} \n"
              f"Receiving a call: {dfs.values[4][1]} \n"
              f"Using internet data: {dfs.values[6][1]}\
            ")
    else:
        dfs = get_allowance_rates("//div[1]/section[2]/div[2]/div/table")

        print(f"Out of allowance rates for {country}: \n"
              f"Calling back to the UK: {dfs.values[0][2]} \n"
              f"Texting back to the UK: {dfs.values[2][2]} \n"
              f"Receiving a call: {dfs.values[5][1]} \n"
              f"Using internet data: {dfs.values[6][1]}\
            ")
