#!/usr/bin/env python
# Python3

'''

'''

import time
from selenium import webdriver

url = "https://www.baidu.com/"

try:
    fireFoxOptions = webdriver.FirefoxOptions()
    # fireFoxOptions.set_headless()
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)

    # webdriver.FirefoxOptions
    driver.get(url)
    # seach = driver.find_element_by_id("kw")
    seach = driver.find_element_by_name("wd")
    print(str(seach))
    seach.send_keys("Python")
    seach.submit()
    # button = driver.find_element_by_class_name("search-btn float-right")
    # print(str(button))
    input("Press any key to continue...")
except Exception as e:
    print(e)
finally:
    try:
        driver.close()
    except:
        pass



