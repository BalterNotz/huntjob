#!/usr/bin/env python
# coding=utf-8
# Python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

liepinurl = "https://www.liepin.com/"
seach_str = u"Python"
counter = 0

with open(".liepinpasswd") as loginfile:
    account = loginfile.readline().split(
        "=")[1].strip().lstrip("\"").rstrip("\"")
    passwd = loginfile.readline().split(
        "=")[1].strip().lstrip("\"").rstrip("\"")

try:
    brower_options = webdriver.FirefoxOptions()
    # brower_options.set_headless()
    brower = webdriver.Firefox(firefox_options=brower_options)
    brower.get(liepinurl)
    brower.find_element_by_xpath(
        u"//a[@title = '登录猎聘网' and @data-selector = 'switchLogin']").click()
    account_input = brower.find_element_by_xpath(
        "//input[@name = 'user_login']")
    passwd_input = brower.find_element_by_xpath(
        "//input[@data-nick = 'login_pwd']")
    login_button = brower.find_element_by_xpath(
        "//input[@value = '登 录' and @type = 'submit']")
    account_input.clear()
    account_input.send_keys(account)
    passwd_input.clear()
    passwd_input.send_keys(passwd)
    login_button.click()

    seach_key = brower.find_element_by_xpath("//input[@data-selector = 'key']")
    seach_key.send_keys(seach_str)

    print(brower.current_url)
    print(brower.current_window_handle)
    print(brower.window_handles)

    seach_btn = seach_key.find_element_by_xpath("../button")
    brower.execute_script("arguments[0].click();", seach_btn)
    brower.switch_to_window(brower.window_handles[1])

    print(brower.current_url)
    print(brower.current_window_handle)
    print(brower.window_handles)

    change_city = WebDriverWait(brower, 5, 0.1).until(EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'search-bar']//div[@class = 'show-text']")))
    print(change_city.text)
    if "深圳" != change_city.text:
        change_city = change_city.find_element_by_xpath("../span/em")
        change_city.click()
        sz_city = brower.find_element_by_xpath("//a[@data-code = '050090']")
        sz_city.click()
        city_ok_btn = brower.find_element_by_xpath("//a[@data-name = 'ok']")
        city_ok_btn.click()

    while True:
        jobs = WebDriverWait(brower, 5, 0.1).until(EC.presence_of_all_elements_located((
            By.XPATH, "//div[@class = 'job-content']//ul[@class = 'sojob-list']/li")))
        current_page = WebDriverWait(brower, 5, 0.1).until(EC.presence_of_element_located((
            By.XPATH, "//div[@class = 'pager']/div[@class = 'pagerbar']/a[@class = 'current']")))
        print("current_page is: %s" % current_page.text)
        counter = counter + 1
        # 处理招聘信息详情
        for job in jobs:
            assert isinstance(job, WebElement)
            try:
                print(job.find_element_by_tag_name("a").text)
                job_url = job.find_element_by_tag_name(
                    "a").get_attribute("href")
                print(job_url)
            except NoSuchElementException as e:
                print(e)

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
