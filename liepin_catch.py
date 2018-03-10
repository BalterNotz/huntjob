#!/usr/bin/env python
# Python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

liepinurl = "https://www.liepin.com/"

try:
    brower_options = webdriver.FirefoxOptions()
    # brower_options.set_headless()
    brower = webdriver.Firefox(firefox_options=brower_options)
    brower.get(liepinurl)
    change_city = brower.find_element_by_xpath("//a[@class = 'change-city']/b")
    if "深圳" != change_city.text:
        change_city.click()
        more_city = brower.find_element_by_xpath("//a[@href = 'https://www.liepin.com/citylist/']")
        more_city.click()
        sz_city = brower.find_element_by_xpath("//a[@href = '/sz/']")
        sz_city.click()

    seach_key = brower.find_element_by_xpath("//input[@name = 'key']")
    seach_key.send_keys("Python")
    seach_btn = brower.find_element_by_xpath("//button[@class = 'search-btn float-right' and @type = 'submit']")
    seach_btn.click()
    while True:
        if input() == "b":
            break
        next_page = brower.find_element_by_xpath("//div[@class = 'pager']/div[@class = 'pagerbar']/a[text() = '下一页']")
        print(next_page)
        next_page.click()
    input("Press any key to continue...")
except Exception as e:
    print(e)
finally:
    brower.close()
