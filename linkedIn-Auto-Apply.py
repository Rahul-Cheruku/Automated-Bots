from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



# ---------------------



EMAIL = "example@abc.com"
PASSWORD = "psd"

chrome_driver_path = Service("C:/Hunter/development/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.linkedin.com/login?trk=homepage-basic_ispen-login-button")
email = driver.find_element(by=By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[1]/input")
password = driver.find_element(by=By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[2]/input")
email.send_keys(EMAIL)
email.send_keys(Keys.ENTER)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&f_JT=P%2CT%2CI&f_WT=2"
           "&geoId=92000000&keywords=python%20developer&location=Worldwide")
time.sleep(3)
# items_list = driver.find_element(by=By.CSS_SELECTOR, value= ".list-style-none")
# print(items_list)
# items = items_list.find_elements(by=By.TAG_NAME, value='li')
# print(items)
# print(len(items))

# for item in x:
#     # try:
#     # time.sleep(3)
#     try:
#         item.click()
#     except:
#         print("passing LOL")
#         pass
#     i = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-unified-top-card__title-container a h2")
#
#     print(i.text + "hello")
#     time.sleep(2)
# print("hello")
# # except:
# #     driver.refresh()
# #     time.sleep(2)
# try:
#     print(driver.find_element(by=By.CSS_SELECTOR, value=".jobs-unified-top-card__title-container a h2").text)
#     apply = driver.find_element(by=By.CLASS_NAME, value="jobs-apply-button--top-card")
#     apply.click()
#     time.sleep(2)
#     number = driver.find_element(by=By.TAG_NAME, value="input")
#     number.clear()
#     number.send_keys("123456789")
#     send = driver.find_element(by=By.CSS_SELECTOR, value=".justify-flex-end button")
#     send.click()
#     time.sleep(1)
#     next1 = driver.find_elements(by=By.CSS_SELECTOR, value=".justify-flex-end button")[1]
#     next1.click()
# except:
#     print("can't apply")
#     time.sleep(2)
#     cancel = driver.find_elements(by=By.CSS_SELECTOR, value=".artdeco-modal[size=small] .artdeco-modal__actionbar button")[1]
#     cancel.click()
# else:
#     driver.refresh()
#     time.sleep(3)
