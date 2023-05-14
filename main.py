from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import *
import time

from selenium.webdriver.chrome.options import Options
chrome_driver_path = Service("C:/Hunter/development/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/rahul/AppData/Local/Google/Chrome/User Data/Default") #Path to your chrome profile
driver = webdriver.Chrome(service=chrome_driver_path, options=options)


#
# driver = webdriver.Chrome(service=chrome_driver_path)
driver.get("https://tinder.onelink.me/9K8a/3d4abb81")

# time.sleep(2)
# try:
#     more_opt = driver.find_element(by=By.CSS_SELECTOR, value=".Tt\(u\)--ml")
#     more_opt.click()
#     time.sleep(2)
# except:
#     pass



fb_login = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button")
fb_login.click()
time.sleep(5)
main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle
# driver.find_element_by_xpath(u'//a[text()="click here"]').click()
signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break
driver.switch_to.window(signin_window_handle)
email = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
email.send_keys("codeydon@gmail.com")
password = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
password.send_keys("thisispomai")
password.send_keys(Keys.ENTER)
driver.switch_to.window(main_window_handle)

# time.sleep(5)
# try:
#     driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button").click()
#     time.sleep(5)
# except:
#     pass
# try:
#     driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
#     time.sleep(5)
# except:
#     pass
# try:
#     driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/button[1]").click()
#     time.sleep(5)
# except:
#     pass
# d=4
#
# list1 = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div")
# print(list1)
# # like = list1[]
while True:
    # try:
    #     #
    try:
        time.sleep(2)

        # "/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button"
        # "/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[4]/button"

        button = driver.find_elements(by=By.TAG_NAME, value= "button")
        time.sleep(2)
        for i in button:
            if i.text == "LIKE":
                i.click()
                print(i.get_attribute("xpath"))
        # for i in range(len(button)):
        #
        #     print(i, button[i].text)

        # driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[5]/div/div[4]/button").click()


    except Exception as e:
        print(e)
        print("majak")
        pass
#
#     # except NoSuchElementException:
#     #     driver.refresh()
#     #     time.sleep(5)
#
#
# print("FOUND")
