#!/usr/bin/python
import pandas as pd
 
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import time

df1 = pd.read_csv("/home/<name>/<name>/users.csv")
print(df1)

starting_index = 0
ending_index = 120
for index, row in df1.iterrows():
    if index >= starting_index and index <= ending_index:
        try:
            driver = webdriver.Firefox()

            url = 'https://accounts.google.com/ServiceLogin?hl=en&passive=true&$
            time.sleep(5)
            print(row["mail_address"])
            driver.get(url)
            driver.find_element_by_id("identifierId").send_keys(row["mail_addre$
            driver.find_element_by_id("identifierNext").click()
            time.sleep(6)
            driver.find_element_by_name("password").send_keys(row["keypass"])
            driver.find_element_by_id("passwordNext").click()
            time.sleep(2)

            # To run Google Colab on set account
            url_google_colab = 'https://colab.research.google.com/drive/%s' % r$
            driver.get(url_google_colab)
            print('Resting...')
            time.sleep(10)
            driver.find_element_by_id('runtime-menu-button').click()
            time.sleep(1)
            driver.find_element_by_id(':1s').click()
            ########################################
            time.sleep(15)
            driver.quit()
        except Exception as e:
            print(e)
            driver.quit()
    else:
        pass
