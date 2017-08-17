import pandas as pd
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



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
        # print(len(username_listesi_lst))

    for el in isim_listesi:
        isim_listesi_lst.append(el.text)
        # print(len(isim_listesi_lst))
    dataframe=pd.DataFrame({"username":username_listesi_lst,"isim_listesi":isim_listesi_lst})
    # driver.close()
    return (dataframe["isim_listesi"][0])


def search_on_google(param):

    chop = webdriver.ChromeOptions()
    chop.add_extension('User-Agent-Switcher-for-Chrome_v1.0.43.crx')
    driver = webdriver.Chrome(chrome_options=chop)

    driver.get("http://www.google.com")
    input_element = driver.find_element_by_name("q")
    time.sleep(6)
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
    time.sleep(6)
    username_listesi = driver.find_elements(By.XPATH, "//div[@class='details definition-list']")
    time.sleep(6)
    print(username_listesi)

    for el in username_listesi:
        username_listesi.append(el.text)
        print(username_listesi)

def chrome_extension_add():
    chop = webdriver.ChromeOptions()
    chop.add_extension('/usr/local/bin/Proxy-for-Chrome_v1.14.crx')
    driver = webdriver.Chrome(chrome_options=chop)
    driver.get("http://www.google.com")
    time.sleep(6)

def angelco(x):

    driver.get("https://angel.co/login")
    username_field = driver.find_element_by_class_name("js-email")
    pass_field = driver.find_element_by_id("user_password")

    username_field.send_keys("kemalcanbora@gmail.com")
    driver.implicitly_wait(1)
    pass_field.send_keys("")
    driver.implicitly_wait(1)

    driver.find_element_by_class_name("c-button").click()


    time.sleep(6)
    url = 'https://angel.co/'+str(x)+'/'
    driver.get(url)

    driver.find_element_by_class_name("hidden_more").click()
    content = driver.find_elements(By.XPATH, "//div[@class='content']")
    hidden_content= driver.find_elements(By.XPATH, "//div[@class='content']/span")
    full_tex = content + hidden_content


    time.sleep(5)
    founders = driver.find_elements(By.XPATH, "//div[@class='founders section']//div[@class='name']")
    teams=     driver.find_elements(By.XPATH, "//div[@class='section team']//div[@class='name']")
    financing=     driver.find_elements(By.XPATH, "//div[@class='past_financing section']//div[@class='name']")


    tags= driver.find_elements(By.XPATH, "//span[@class='js-market_tags']//a[@class='tag']")
    location= driver.find_elements(By.XPATH, "//span[@class='js-location_tags']")
    company_size= driver.find_elements(By.XPATH, "//span[@class='js-company_size']")

    ##########
    tags_links = driver.find_element_by_class_name('js-market_tags')
    tag_a=tags_links.find_element_by_css_selector('a').get_attribute('href')

    tags_links_lst = []
    for el in tag_a:
        print(el)

    ##########

    company_size_lst = []
    for el in company_size:
        company_size_lst.append(el.text)
        company_size_Df= pd.DataFrame({"company_size_lst ": company_size_lst})

    location_lst = []
    for el in location:
        location_lst.append(el.text)
        location_Df= pd.DataFrame({"location_lst  ": location_lst })

    tags_lst = []
    for el in tags:
        tags_lst.append(el.text)
        tagsDf = pd.DataFrame({"tags_lst ": tags_lst })

    founders_lst=[]
    for el in founders :
        founders_lst.append(el.text)
        foundersDf=pd.DataFrame({"founders_lst":founders_lst})

    team_lst = []
    for el in teams:
        team_lst.append(el.text)
        teamDf = pd.DataFrame({"team_lst ": team_lst })

    financing_lst = []
    for el in financing:
        financing_lst.append(el.text)
        financingDf = pd.DataFrame({"financing_lst ": financing_lst })


    frames=[teamDf,foundersDf,financingDf]
    fullset_datadf=pd.concat(frames)
    print(fullset_datadf)

    print(tags_lst)
    print(company_size_lst)
    print(location_lst)

    time.sleep(6)

    for i,item in enumerate(tags_lst):
        print(tags_lst[i])
        url = 'https://angel.co/' + str(tags_lst[i]) + '/'
        driver.get(url)
        rev=     driver.find_elements(By.XPATH, "//div[@class='results_holder']//div[@class='name']")
        rev_lst = []
        for el in rev:
            rev_lst.append(el.text)
            rev_lstDf = pd.DataFrame({"rev_lst ": rev_lst })
        print(rev_lst)


#########################dasda################3
username = "tuulrik"#input("user name : ")
password = ""#getpass("password  : ")

# sonuc=login_twitter(username, password)
# x=search_on_google(sonuc)
angelco("evreka")