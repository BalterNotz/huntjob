#!/usr/bin/env python
# Python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

liepinurl = "https://www.liepin.com/"

with open(".liepinpasswd") as loginfile:
    account = loginfile.readline().split(
        "=")[1].strip().lstrip("\"").rstrip("\"")
    passwd = loginfile.readline().split(
        "=")[1].strip().lstrip("\"").rstrip("\"")
print(account)
print(passwd)

try:
    brower_options = webdriver.FirefoxOptions()
    # brower_options.set_headless()
    brower = webdriver.Firefox(firefox_options=brower_options)
    brower.get(liepinurl)

    gotologin = brower.find_element_by_xpath(
        u"//a[@title = '登录猎聘网' and @data-selector = 'switchLogin']")
    print(gotologin)
    ActionChains(brower).click(gotologin).perform()
    account_input = brower.find_element_by_xpath("//input[@name = 'user_login']")
    passwd_input = brower.find_element_by_xpath(
        "//input[@data-nick = 'login_pwd']")
    login_button = brower.find_element_by_xpath("//input[@value = '登 录' and @type = 'submit']")
    print(account_input)
    print(passwd_input)
    ActionChains(brower).move_to_element(account_input).click().perform()
    account_input.clear()
    ActionChains(brower).send_keys(account).perform()

    ActionChains(brower).move_to_element(passwd_input).click().perform()
    passwd_input.clear()
    ActionChains(brower).send_keys(passwd).perform()
    # account_input.send_keys(account)
    # passwd_input.send_keys(passwd)
    # login_button.click()
    ActionChains(brower).click(login_button).perform()
    input("Press any key to continue...")
except Exception as e:
    print(e)
finally:
    brower.close()
