import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QObject
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoAlertPresentException, StaleElementReferenceException, NoSuchElementException

from CRM_mainUI import MainUI

class KeyFn(QObject) : 
    def classRegistration(self, account, subjectData) : 
        mainUI = MainUI()

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

        driver.implicitly_wait(3)
        driver.get("https://sugang.kumoh.ac.kr/html/stud/sugang.html")

        time.sleep(0.2)
        try : 
            driver.find_element(By.ID, "Form_로그인.아이디").send_keys(account[0])
            driver.find_element(By.ID, "Form_로그인.비밀번호").send_keys(account[1])
        except NoSuchElementException : 
            print("[system] 수강신청 사이트가 아직 열리지 않았거나 사이트의 내용이 변경되었습니다.")                 # Test code / please delete the contents of this line.
            return

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
        

        def registration(subject) : 
            subjectName, subjectCode = subject[0], subject[1]

            driver.find_element(By.ID, "Form_희망수강과목입력.개설교과목코드").send_keys(subjectCode)
            try : 
                driver.find_element(By.ID, "Form_버튼.pb1").click()

                time.sleep(0.2)
                alert = driver.switch_to.alert
                if "아니므로" in alert.text.split() : 
                    print("[system] 교과목 코드를 다시 확인해주십시오.")                # Test code / please delete the contents of this line.
                    return False
                elif "이중으로" in alert.text.split() : 
                    print("[system] 이미 수강신청을 완료한 과목입니다.")                # Test code / please delete the contents of this line.
                    return False
                # (+ 수강신청하려는 과목의 인원이 마감된 경우)                 # Test code / please delete the contents of this line.

                alert.accept()
            except NoAlertPresentException : 
                print(f"[system] '{subjectName}' 과목의 수강신청이 완료되었습니다.")                 # Test code / please delete the contents of this line.
                return True

        subjectData = subjectData.items()
        majorSubjectCnt = len(subjectData)
        registrationCnt = 0
        for major, insuranceLi in subjectData : 
            if not registration(major) : 
                for insurance in insuranceLi : 
                    if registration(insurance) : 
                        break
            majorSubjectCnt += 1
            mainUI.completed_txt_lb.setText(f"{registrationCnt} / {majorSubjectCnt}")

        time.sleep(100)                 # Test code / please delete the contents of this line.
        driver.quit()





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    account = (20772077, 20772077)
    subjectData = {("努力 未来 A BEAUTIFUL STAR", "YK1012-22")}
    KeyFn().classRegistration(account, subjectData)
