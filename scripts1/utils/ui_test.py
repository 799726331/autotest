'''
-*- coding: utf-8 -*-
@Time    : 2021/6/3 9:44
@Author  : Luzixuan
@File    : ui_test.py
@contest    : 
'''
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import win32gui,win32con
# 启动谷歌浏览器,开启与浏览器之间的会话
driver = webdriver.Chrome(service_log_path=r"F:\autotest\scripts1\utils\chromedriver_service.log")
driver.implicitly_wait(10)
driver.get("http://www.taobao.com")
driver.maximize_window()
# ele = driver.find_element_by_id("kw")
# ele2 = driver.find_element_by_link_text("新闻")
# ele2 = driver.find_element_by_partial_link_text("新闻")
# driver.find_element_by_xpath('//div/a[text()="新闻"]').click()
# time.sleep(10)
# print(ele)
# print(ele.get_attribute("class"))
# print(ele2.get_attribute("class"))
# WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("xx"))
# ele = driver.find_element_by_xpath('//div[@id="u1"]/span[@id="s-usersetting-top"]')
# ActionChains(driver).move_to_element(ele).perform()
# ele.click()
# ActionChains(driver).click(ele)

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//html')))
element = driver.find_element_by_xpath('//html')
driver.execute_script("arguments[0].scrollIntoView(false);",element)


time.sleep(10)
driver.quit()

dialog = win32gui.FindWindow("#32770","打开")
win32gui.FlashWindowEx(dialog,0,"")