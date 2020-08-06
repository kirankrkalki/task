import os
import time
import pytest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import wait
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.file_detector import UselessFileDetector

def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
    driver.get("https://skoolgo.pixelmindit.com:5000/")
    driver.maximize_window()
    driver.implicitly_wait(5)
test_setup()
def test_Login():
    driver.find_element_by_id("userName").send_keys("admin@pixel.com")
    driver.find_element_by_id("password").send_keys("sk12345")
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/form/div/div[6]/button').click()
test_Login()
def test_createmember():
    #driver.switch_to_frame(driver.find_element_by_name("__privateStripeMetricsController0"))
    driver.find_element_by_link_text("Members").click()
    driver.find_element_by_css_selector("#root > aside > ul > li:nth-child(2) > ul > li:nth-child(1) > a").click()
test_createmember()
def test_addmember():
    driver.find_element_by_id("fullName").send_keys("kiran")
    driver.find_element_by_id("email").send_keys("kushalkalki@gmail.com")
    driver.find_element_by_class_name("PhoneInputInput").send_keys("9445812465")
    element = Select(driver.find_element_by_xpath('//*[@id="root"]/main/div/div/form/div/div[2]/div/div[3]/div/div[1]/div/div/select'))
    element.select_by_value("IN")
    driver.find_element_by_id("personalId").send_keys("123")
   # driver.find_element_by_xpath('//*[@id="age"]').send_keys("23") #element disabled
    driver.find_element_by_xpath('//*[@id="root"]/main/div/div/form/div/div[2]/div/div[5]/div/div[1]/div/input').click()
    driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[1]/button[1]/span[1]/h6").click()
    driver.find_element_by_css_selector("body > div.MuiPopover-root > div.MuiPaper-root.MuiPopover-paper.MuiPaper-elevation8.MuiPaper-rounded > div > div.MuiPickersBasePicker-pickerView > div > div:nth-child(98)").click()
    driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div[5]/div[6]/button/span[1]/p").click()
    ele = Select(driver.find_element_by_id("nationality"))
    ele.select_by_value("India")
    gender = Select(driver.find_element_by_id("gender"))
    gender.select_by_value("Male")
    branch = Select(driver.find_element_by_id("branch"))
    branch.select_by_value("5f16ed64f125ec15b432a2b3")
    driver.find_element_by_id("height").send_keys("5.5")
    driver.find_element_by_id("weight").send_keys("60")
    driver.find_element_by_xpath('//*[@id="root"]/main/div/div/form/div/div[2]/div/div[12]/div/div[1]/div/input').send_keys("8095082949")
    eleme = Select(driver.find_element_by_xpath('//*[@id="root"]/main/div/div/form/div/div[2]/div/div[12]/div/div[1]/div/div/select'))
    eleme.select_by_value("IN")
    driver.find_element_by_id("relationship").send_keys("Single")
    #driver.find_element_by_id("referralCode").send_keys("12345")
    driver.find_element_by_id("Notes").send_keys("I Am tester")
    driver.find_element_by_xpath('//*[@id="capBrowseImg"]').send_keys("E:/img.jpg")
test_addmember()
def test_package():
    pack = Select(driver.find_element_by_id("packageName"))
    pack.select_by_visible_text("Platinum")
    time.sleep(5)
    action = ActionChains(driver);
    driver.find_element_by_xpath('//*[@id="root"]/main/div/div/form/div/div[6]/div/div/div/div[1]/div/div[1]/div/div[2]/div').click()
    #driver.find_element_by_xpath("//a[contains(text(),'Jak Me')]").click();
    driver.find_element_by_xpath('//*[@id="root"]/main/div/div/form/div/div[6]/div/div/div/div[1]/div/div[1]/div/div[1]/div/div/div/small[2]').click()

    period = Select(driver.find_element_by_id("period"))
    period.select_by_visible_text("One Month")
    level = Select(driver.find_element_by_id("levelQuestion"))
    level.select_by_value("Beginner")
    goal = Select(driver.find_element_by_id("goalQuestion"))
    goal.select_by_value("Gain Weight")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    exercise = Select(driver.find_element_by_xpath('//*[@id="exercisingQuestion"]'))
    exercise.select_by_visible_text("5 Days a week")
    time.sleep(5)
    driver.find_element_by_css_selector('#root > main > div > div > form > div > div:nth-child(7) > div > button.btn.btn-success.mx-1.px-4').click()
test_package()
def test_addcash():
    driver.find_element_by_id("addCash").send_keys("100")
    driver.find_element_by_id("addCard4lastno").send_keys("1432")
    time.sleep(7)
    driver.close()
    driver.quit()
test_addcash()
