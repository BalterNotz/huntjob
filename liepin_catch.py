#!/usr/bin/env python
#coding=utf-8
# Python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

liepinurl = "https://www.liepin.com/"
counter = 0

try:
    brower_options = webdriver.FirefoxOptions()
    # brower_options.set_headless()
    brower = webdriver.Firefox(firefox_options=brower_options)
    brower.get(liepinurl)
    change_city = brower.find_element_by_xpath("//a[@class = 'change-city']/b")
    if "深圳" != change_city.text:
        change_city.click()
        more_city = brower.find_element_by_xpath(
            "//a[@href = 'https://www.liepin.com/citylist/']")
        more_city.click()
        sz_city = brower.find_element_by_xpath("//a[@href = '/sz/']")
        sz_city.click()

    seach_key = brower.find_element_by_xpath("//input[@name = 'key']")
    seach_key.send_keys(u"爬虫")
    seach_btn = brower.find_element_by_xpath(
        "//button[@class = 'search-btn float-right' and @type = 'submit']")
    brower.execute_script("arguments[0].click();", seach_btn)
    # seach_btn.click()
    while True:
        jobs = WebDriverWait(brower, 5, 0.1).until(EC.presence_of_all_elements_located((
            By.XPATH, "//div[@class = 'job-content']/div[@class = 'sojob-result ']/ul[@class = 'sojob-list']/li")))
        current_page = WebDriverWait(brower, 5, 0.1).until(EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'pager']/div[@class = 'pagerbar']/a[@class = 'current']")))
        print("current_page is: %s" % current_page.text)
        counter = counter + 1

        next_page = WebDriverWait(brower, 5, 0.1).until(EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'pager']/div[@class = 'pagerbar']/a[text() = '下一页']")))
        if next_page.get_attribute("class") != "disabled":
            brower.execute_script("arguments[0].click();", next_page)
        else:
            break
        current_page = WebDriverWait(brower, 5, 0.1).until(EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'pager']/div[@class = 'pagerbar']/a[@class = 'current' and text() = '" + str(counter + 1) + "']")))
    input("Press any key to continue...")
except Exception as e:
    print(e)
finally:
    print("counter: %d" % counter)
    brower.quit()
