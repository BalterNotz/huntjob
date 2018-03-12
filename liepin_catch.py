#!/usr/bin/env python
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
    seach_key.send_keys("Python")
    seach_btn = brower.find_element_by_xpath(
        "//button[@class = 'search-btn float-right' and @type = 'submit']")
    seach_btn.click()
    while True:
        jobs = WebDriverWait(brower, 5, 0.1).until(EC.presence_of_all_elements_located((
            By.XPATH, "//div[@class = 'job-content']/div[@class = 'sojob-result ']/ul[@class = 'sojob-list']/li")))
        # jobs = brower.find_element_by_xpath(
        #     "//div[@class = 'job-content']/div[@class = 'sojob-result ']/ul[@class = 'sojob-list']")
        # jobs = jobs.find_elements_by_tag_name("li")
        for job in jobs:
            assert isinstance(job, WebElement)
            print(job.text)
        next_page = WebDriverWait(brower, 5, 0.1).until(EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'pager']/div[@class = 'pagerbar']/a[text() = '下一页']")))
        # next_page = brower.find_element_by_xpath(
            # "//div[@class = 'pager']/div[@class = 'pagerbar']/a[text() = '下一页']")
        # brower.execute_script("document.getElementsByClassName('comment-user')[0].click()")
        # next_page.click()
        counter = counter + 1
        if input() == "b":
            break
        brower.execute_script("arguments[0].click();", next_page)
    input("Press any key to continue...")
except Exception as e:
    print(e)
finally:
    print("counter: %d" % counter)
    brower.close()
