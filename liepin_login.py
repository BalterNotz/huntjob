#!/usr/bin/env python
# Python3

import PIL
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
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
    print("输入的密码为：" + passwd_input.get_attribute("value"))
    login_button.click()
    if EC.title_is("我的首页_猎聘网:Liepin.com")(brower):
        pass
    else:
        verify_code_input = brower.find_element_by_xpath(
        "//input[@name = 'verifycode']")
        verify_image = brower.find_element_by_xpath("//img[@class = 'very-image']")
        if verify_code_input.is_displayed():
            print("verify code input is displayed")
            verify_code_input.send_keys("abcd")
            login_button.click()
            verify_png = open("verify.png", "wb")
            verify_png.write(verify_image.screenshot_as_png)
    
        # <span class="error-content">验证码不正确</span>
    
    input("Press any key to continue...")
except Exception as e:
    print(e)
finally:
    brower.close()
