import pandas as pd 
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

df1 = pd.read_csv("users.csv")
print(df1)

starting_point = 0
for index, row in df1.iterrows():
    if index > starting_point and pd.notnull(row["drive_id"]) is False:
        try:
            print(row["mail_address"])
            driver = webdriver.Firefox()

            url = 'https://accounts.google.com/ServiceLogin?hl=en&passive=true&$
            time.sleep(5)
            driver.get(url)

            driver.find_element_by_id("identifierId").send_keys(row["mail_addre$
            driver.find_element_by_id("identifierNext").click()
            time.sleep(5)
            driver.find_element_by_name("password").send_keys(row["keypass"])
            driver.find_element_by_id("passwordNext").click()
            print('Please proceed to verify')
            time.sleep(30)

            driver.get('https://colab.research.google.com/notebook#create=true&$
            time.sleep(30)
            hash_drive_id = driver.current_url.rsplit('/', 1)[-1]
            print(hash_drive_id)
            df1.loc[index, "drive_id"] = "{}".format(hash_drive_id)
            print("Adjusting for user '{}'".format(row["mail_address"]))
            df1.to_csv('newUser.csv', encoding='utf-8', index=False)
            driver.quit()
        except Exception as e:
            print(e)
    else:
        pass
