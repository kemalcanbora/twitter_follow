from selenium import webdriver
from getpass import getpass
import time
import requests
from bs4 import BeautifulSoup

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

    url = 'https://twitter.com/evrekaco/followers'

    driver.get(url)
    initial_value = 0
    end = 300000
    for i in range(1000, end, 1000):
        driver.execute_script("window.scrollTo(" + str(initial_value) + ', ' + str(i) + ")")
        time.sleep(0.5)
        initial_value = i



    time.sleep(600)

username = "usernmae"#input("user name : ")
password = "pass"#getpass("password  : ")
login_twitter(username, password)


