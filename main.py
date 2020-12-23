import time
import pandas as pd
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions

with open("countries", "r") as f:
    countries = f.read().splitlines()

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


country_allowance_rates = dict()
for country in countries:
    search_country(country)
    time.sleep(6)
    if country in ("South Africa", "China", "Madagascar"):
        dfs = get_allowance_rates("//table[@class='roaming-charges-table']")

        country_allowance_rates[country] = \
            dfs.values[0][1].replace("\xa0", " "), \
            dfs.values[2][1].replace("\xa0", " "), \
            dfs.values[4][1].replace("\xa0", " "), \
            dfs.values[6][1].replace("\xa0", " ")
    else:
        dfs = get_allowance_rates("//div[@class='roaming-charges']/table")

        country_allowance_rates[country] = \
            dfs.values[0][2].replace("\xa0", " "), \
            dfs.values[2][2].replace("\xa0", " "), \
            dfs.values[5][1].replace("\xa0", " "), \
            dfs.values[6][1].replace("\xa0", " ")

print(country_allowance_rates)
