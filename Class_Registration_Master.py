'''
======================================
< Class_Registration_Master_v1.0 >

'수강신청 마스터'를 사용해 나머지 99%의 사람들에게 당신과의 격차를 확실히 느끼게 해주십시오.

* Made by Yoonmen *

- 22.??.?? (???) ??:?? -
======================================
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

from selenium.common.exceptions import ElementNotInteractableException, NoAlertPresentException, StaleElementReferenceException

import time

option = Options()
# option.add_argument("headless")               # Test code / please unlock the contents of this line.
option.add_argument("start-maximized")
option.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chromedriver_autoinstaller.get_chrome_version()} Safari/537.36")
option.add_experimental_option("excludeSwitches", ["enable-logging"])

try : 
    driver = webdriver.Chrome(options=option)
except : 
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=option)

driver.implicitly_wait(60)

driver.get("https://sugang.kumoh.ac.kr/html/stud/sugang.html")
time.sleep(0.2)
driver.find_element(By.ID, "Form_로그인.아이디").send_keys("20774796")
driver.find_element(By.ID, "Form_로그인.비밀번호").send_keys("123456789")

try : 
    driver.find_element(By.ID, "Form_버튼.pb_확인").click()
    time.sleep(0.2)
    alert = driver.switch_to.alert
    print(alert.text)               # Test code / please delete the contents of this line.
    if "수강신청기간이" in alert.text.split() : 
        print("[system] 해당 학년의 수강 신청 기간이 아닙니다.")                # Test code / please delete the contents of this line.
    elif "아이디" in alert.text.split() : 
        print("[system] 아이디 또는 비밀번호를 다시 확인해 주십시오.")              # Test code / please delete the contents of this line.
    alert.accept()
except NoAlertPresentException : 
    print("[system] 로그인을 완료했습니다.")             # Test code / please delete the contents of this line.

subjects = ["CD006001"]
for i in subjects : 
    driver.find_element(By.ID, "Form_희망수강과목입력.개설교과목코드").send_keys(i)
    try : 
        driver.find_element(By.ID, "Form_버튼.pb1").click()
        time.sleep(0.2)
        alert = driver.switch_to.alert
        if "아니므로" in alert.text.split() : print("[system] 교과목 코드를 다시 확인해주십시오.")
        elif "이중으로" in alert.text.split() : print("[system] 이미 수강신청을 완료한 과목이므로 다음 과목으로 넘어갑니다.")
        alert.accept()
    except NoAlertPresentException : 
        print("[system] 다음 과정으로 넘어갑니다.")             # Test code / please delete the contents of this line.
time.sleep(100)                 # Test code / please delete the contents of this line.
driver.quit()