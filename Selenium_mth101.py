import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

driver  = webdriver.Chrome(r"C:\Users\hplap\Downloads\chromedriver_win32\chromedriver")

driver.get("https://hello.iitk.ac.in/user/login")
# driver.close()

driver.find_element_by_id("edit-name").send_keys("jsajal21@iitk.ac.in")
time.sleep(0.2)
driver.find_element_by_id("edit-pass").send_keys("imgenius2@3SA")
time.sleep(0.4)
driver.find_element_by_id("edit-submit").click()
time.sleep(0.4)
driver.get("https://hello.iitk.ac.in/course/mth101a2122")
time.sleep(0.4)
driver.find_element_by_id("edit-access-course").click()
driver.get("https://hello.iitk.ac.in/mth101a2122/#/lecture/34")
# driver.find_element_by_link_text("MATHEMATICS I").click()
# driver.find_element(By.partialLinkText("MTH101AA")).click()
# driver.close
# /html/body/app-root/div[2]/div/div[2]/app-home/div[4]/div[2]/ul/li[1]/span[1]



