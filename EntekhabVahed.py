
# ///////////////////////////////////////////

## selenium اول نصب کنید
## برای این کار
## pip install selenium
## CMD داخل
## کپی کنید
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
import time

#شماره دانشجویی
Scode = "98"

#رمز عبور
Spass = ""

#کد درسا

cc="""
831380
"""
codes= [c for c in cc.split()]

file_path = os.path.dirname(os.path.abspath(__file__))
driver_path = os.path.join(file_path, 'chromedriver.exe')
driver = webdriver.Chrome(executable_path= driver_path)

driver.get("https://portal1.shdu.ac.ir")
begining_handels = driver.window_handles
driver.switch_to.window(begining_handels[0])
if driver.title !="ورود":
    driver.close()
    driver.switch_to.window(begining_handels[1])
driver.maximize_window()

driver.find_element(By.XPATH,'//*[@id="pnlLogin_UserName"]').send_keys(Scode)
driver.find_element(By.XPATH,'//*[@id="pnlLogin_Password"]').send_keys(Spass, Keys.ENTER)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="سيستم جامع مديريت آموزش"]'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="انتخاب واحد"]'))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'id31'))).click()


handels = driver.window_handles
driver.switch_to.window(driver.window_handles[len(handels)-1])
driver.maximize_window()

while(True):
    try:
        driver.find_element(By.XPATH,'//span[text()="دروس اخذ شده در صورت عدم پرداخت بدهي قطعي نميباشد و حذف خواهد شد."]')
        print("Ohhhhhhhhhhhhh it's Started")
        os.system("CLS")
        break
    except EC.NoSuchElementException:
        driver.refresh()
        

while(True):
    for lessonCode in codes:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_CH1_txtGCode"]'))).send_keys(lessonCode , Keys.ENTER)
        try:
            WebDriverWait(driver, 4).until(EC.alert_is_present())
            driver.switch_to.alert.accept()
        except :
            os.system("CLS")
            print(lessonCode ,"Taken")
            pass
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ctl00_CH1_txtGCode"]'))).send_keys(Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,Keys.BACKSPACE,)