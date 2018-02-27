#!/usr/bin/env python
# Python3

'''

'''

import time
from selenium import webdriver

liepinurl = "http://www.liepin.com/"
liepinzhaopinurl = "https://www.liepin.com/zhaopin"

try:
    fireFoxOptions = webdriver.FirefoxOptions()
    # fireFoxOptions.set_headless()
    driver = webdriver.Firefox(firefox_options=fireFoxOptions)

    # webdriver.FirefoxOptions
    driver.get(liepinzhaopinurl)
    select_city = driver.find_element_by_xpath("/html/body/div[1]/form/div[1]/div/div/ul/li[1]/span/em")
    select_city.click()
    shenzhen_city = driver.find_element_by_xpath("/html/body/div[9]/div[2]/div[2]/div/div[3]/div/div[1]/ul/li[4]/a")
    shenzhen_city.click()
    confirm_shenzhen = driver.find_element_by_xpath("//div[@class = 'vd-footer vd-footer-ltr']/a[@data-name = 'ok' and text() = '确定']")
    confirm_shenzhen.click()
    seach = driver.find_element_by_name("key")
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
