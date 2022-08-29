from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time


#####################################################
######### Scode = شماره دانشجویی Spass = رمز عبور سامانه
#####################################################
def login(Scode = "98", Spass = ""):

    url = 'https://portal1.shdu.ac.ir'
    AccepteStudent_xpath = 'pnlLogin_chkAccepteStudent'
    Login_UserName_xpath = '//*[@id="pnlLogin_UserName"]'
    Login_Password_xpath = '//*[@id="pnlLogin_Password"]'

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    begining_handels = driver.window_handles
    driver.switch_to.window(begining_handels[0])
    
    if driver.title !="ورود":
        driver.close()
        driver.switch_to.window(begining_handels[1])
    driver.maximize_window()
    try:
        driver.find_element(By.ID, AccepteStudent_xpath).click()
    except:
        pass
    driver.find_element(By.XPATH, Login_UserName_xpath).send_keys(Scode)
    driver.find_element(By.XPATH, Login_Password_xpath).send_keys(Spass, Keys.ENTER)

    return driver

def list_erae_shode(home_driver):
    driver = home_driver
    amozesh_xpath = '//span[text()="سيستم جامع مديريت آموزش"]'
    entekhabVahed_xpath = '//a[text()="انتخاب واحد"]'
    list_erae_shode_id = "id131"
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, amozesh_xpath))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, entekhabVahed_xpath))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, list_erae_shode_id))).click()
    handels = driver.window_handles
    driver.switch_to.window(driver.window_handles[len(handels)-1])
    driver.maximize_window()
    return driver


def lesson_checker (list_erae_shode_driver):
    driver = list_erae_shode_driver
    codes = ["631301", "431210", "431209", "531204", "331202",
            "331105" , "431207", "331107", "731201"]

    FullLessonGroups_xpath = '//*[@id="ctl00_CH1_chkFullLessonGroups"]'
    txtLessonCode_xpath = '//*[@id="ctl00_CH1_txtLessonCode"]'
    btnSearch_xpath = '//*[@id="ctl00_CH1_btnSearch"]'
    btnShowSearch_xpath = '//*[@id="ctl00_CH1_btnShowSearch"]'

    del_loop = [6 * Keys.BACKSPACE]
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, FullLessonGroups_xpath))).click()
    while(True):
        for lessonCode in codes:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, txtLessonCode_xpath))).send_keys(lessonCode)
            WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, btnSearch_xpath))).click()
            time.sleep(1)
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, btnShowSearch_xpath))).click()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, txtLessonCode_xpath))).send_keys(del_loop)

def entekhab_vahed(home_driver):
    driver = home_driver

    amozesh_xpath = '//span[text()="سيستم جامع مديريت آموزش"]'
    entekhabVahed_xpath = '//a[text()="انتخاب واحد"]'
    entekhabVahed_id = 'id31'
    start_text_xpath = '//span[text()="دروس اخذ شده در صورت عدم پرداخت بدهي قطعي نميباشد و حذف خواهد شد."]'

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, amozesh_xpath))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, entekhabVahed_xpath))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, entekhabVahed_id))).click()
    handels = driver.window_handles
    driver.switch_to.window(driver.window_handles[len(handels)-1])
    driver.maximize_window()

    while(True):
        try:
            driver.find_element(By.XPATH , start_text_xpath)
            os.system("CLS")
            print("Ohhhhhhhhhhhhh it's Started")
            break
        except EC.NoSuchElementException:
            driver.refresh()

    return driver

def lesson_taker(entekhab_vahed_driver):
    driver = entekhab_vahed_driver
    codes = ["831180"]
    code_input_xpath = '//*[@id="ctl00_CH1_txtGCode"]'
    vahed_id = 'ctl00_CH1_lblSumUnits'
    del_loop = [6 * Keys.BACKSPACE]
    
    if len(codes) ==1:
        spammer(codes, driver)
        driver.close()
    else:
        while(True):
            for lessonCode in codes:
                print(lessonCode)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, vahed_id)))
                vaheds_taken_before = int(driver.find_element(By.ID, vahed_id).text)
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, code_input_xpath))).send_keys(lessonCode , Keys.ENTER)

                try:
                    WebDriverWait(driver , 1).until(EC.alert_is_present() )
                    my_alert = driver.switch_to.alert
                    print(my_alert.text)
                    my_alert.accept()
                    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, code_input_xpath))).send_keys(del_loop)
                except TimeoutException:
                    driver.refresh()
                except:
                    try:
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, vahed_id)))
                        vaheds_taken_after = int(driver.find_element(By.ID, vahed_id).text)
                        print(f"vaheds_taken_after:{vaheds_taken_after}  vaheds_taken_before :{vaheds_taken_before}")
                        if vaheds_taken_after > vaheds_taken_before :
                            print(lessonCode , 'taken')
                        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, code_input_xpath))).send_keys(del_loop)
                    except TimeoutException:
                        driver.refresh()
            
def spammer (codes , driver):
    driver = driver
    code_input_xpath = '//*[@id="ctl00_CH1_txtGCode"]'
    vahed_id = 'ctl00_CH1_lblSumUnits'
    del_loop = [6 * Keys.BACKSPACE]

    while(True):
        for lessonCode in codes:
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, code_input_xpath))).send_keys(lessonCode , Keys.ENTER)
            WebDriverWait(driver,20).until(EC.alert_is_present())
            try:
                driver.switch_to.alert.accept()
            except:
                pass
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, code_input_xpath))).send_keys(del_loop)

def main_for_entekhab():
    home_driver = login()
    entekhab_vahed_driver = entekhab_vahed(home_driver)
    lesson_taker(entekhab_vahed_driver)

def main_for_list_erae():
    home_driver = login()
    list_erae_shode_driver = list_erae_shode(home_driver)
    lesson_checker(list_erae_shode_driver)

def choice():
    print('\033[96m' + "Please choose: ")
    print('\33[31m' + "1) entekhab vahed")
    print('\33[32m' + "2) list erae shode" + '\33[0m')
    c = 0
    while( c == 0):
        e = int(input("? "))
        if e == 1 or e == 2:
            c = e
        else:
            print('\33[31m' + "only 1 or 2 is accepted ... try again" + '\33[0m')
    return c

if __name__ == "__main__":
    user_choice = choice()

    main_for_entekhab() if user_choice == 1 else main_for_list_erae()
