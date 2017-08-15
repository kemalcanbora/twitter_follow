import pandas as pd
import time
import  requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

### for proxy ##
# PROXY = "fr3.vpnme.me"
# webdriver.DesiredCapabilities.CHROME['proxy']={
#     "httpProxy":PROXY,
#     "ftpProxy":PROXY,
#     "sslProxy":PROXY,
#     "noProxy":None,
#     "proxyType":"MANUAL",
#     "autodetect":False,
#     "class": "org.openqa.selenium.Proxy",
# }

driver = webdriver.Chrome("/usr/bin/chromedriver")

def login_twitter(username, password):
    driver.get("https://twitter.com/login")

    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    username_field.send_keys(username)
    driver.implicitly_wait(1)

    password_field.send_keys(password)
    driver.implicitly_wait(1)

    driver.find_element_by_class_name("EdgeButtom--medium").click()

    url = 'https://twitter.com/enevo/following'

    driver.get(url)

    initial_value = 0

    end = 3000
    for i in range(1000, end, 1000):
        driver.execute_script("window.scrollTo(" + str(initial_value) + ', ' + str(i) + ")")
        time.sleep(0.5)
        initial_value = i
        username_listesi = driver.find_elements(By.XPATH,"//b[@class='u-linkComplex-target']")
        isim_listesi = driver.find_elements(By.XPATH, "//a[@class='fullname ProfileNameTruncated-link u-textInheritColor js-nav']")

    username_listesi_lst = []
    isim_listesi_lst = []

    for el in username_listesi[1:]:
        username_listesi_lst.append(el.text)

    for el in isim_listesi:
        isim_listesi_lst.append(el.text)
    dataframe=pd.DataFrame({"username":username_listesi_lst,"isim_listesi":isim_listesi_lst})

    return (dataframe["isim_listesi"][0])

    time.sleep(6)

def search_on_google(param):
    driver.get("http://www.google.com")
    input_element = driver.find_element_by_name("q")
    time.sleep(60)
    input_element.send_keys(str(param)+" crunchbase")
    input_element.submit()

    RESULTS_LOCATOR = "//div/h3/a"

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))

    ## return results###
    #page1_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)
    #for item in page1_results:
    #     print(item.text)

    time.sleep(3)
    assert "No results found." not in driver.page_source
    driver.find_element_by_xpath('.//*[@id="rso"]/div[1]/div/div/div/div/h3/a').click()
    print(driver.current_url)
    return (driver.current_url)

def crunchbase(crunch_link):
    driver.get(crunch_link)
    time.sleep(60)
    username_listesi = driver.find_elements(By.XPATH, "//div[@class='overview-stats']")
    time.sleep(60)
    for el in username_listesi:
        username_listesi.append(el.text)
        print(username_listesi)

def proxy_crunchbase(param):
    driver.get("https://www.proxysite.com/tr/")
    time.sleep(3)
    input_element = driver.find_element_by_name("d")
    input_element.send_keys(str(param))
    input_element.submit()
    time.sleep(3)

    defin= driver.find_elements(By.XPATH, "//div[@class='details definition-list']")

    for el in defin:
        print(el.text)



username = "tuulrik"#input("user name : ")
password = "XXX"#getpass("password  : ")

sonuc=login_twitter(username, password)
x=search_on_google(sonuc)
crunchbase(x)