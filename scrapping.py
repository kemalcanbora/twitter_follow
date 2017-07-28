from selenium import webdriver
from getpass import getpass
import time
import requests
from selenium.webdriver.common.by import By

def login_twitter(username, password):
    driver = webdriver.Chrome("/usr/bin/chromedriver")
    driver.get("https://twitter.com/login")

    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    username_field.send_keys(username)
    driver.implicitly_wait(1)

    password_field.send_keys(password)
    driver.implicitly_wait(1)

    driver.find_element_by_class_name("EdgeButtom--medium").click()

    url = 'https://twitter.com/kemalcanbora/following'

    driver.get(url)

    initial_value = 0


    end = 30000
    for i in range(1000, end, 1000):
        driver.execute_script("window.scrollTo(" + str(initial_value) + ', ' + str(i) + ")")
        time.sleep(0.5)
        initial_value = i
        liste = driver.find_elements(By.XPATH,"//b[@class='u-linkComplex-target']")
    for el in liste:
        print(el.text)


    # el = driver.find_element(By.XPATH, "//div[@class='u-textTruncate u-inlineBlock ProfileNameTruncated-withBadges ProfileNameTruncated-withBadges--1']")
    # print(el.text)

    time.sleep(600)

username = "tuulrik"#input("user name : ")
password = "pass"#getpass("password  : ")
login_twitter(username, password)


