'''
======================================
< Class_Registration_Master_v1.0 >

'수강신청 마스터'를 사용해 나머지 99%의 사람들에게 당신과의 격차를 확실히 느끼게 해주십시오.

* Made by Yoonmen *

- 22.??.?? (???) ??:?? -
======================================
'''

import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QThread, QObject
from PySide2.QtWidgets import QTreeWidgetItem
import webbrowser
import time

from CRM_mainUI import MainUI
from CRM_keyFn import KeyFn


class Main(QObject) : 
    def __init__(self) : 
        super().__init__()

        global mainUI
        mainUI = MainUI()

        global thread_keyFn        # For quit
        thread_keyFn = QThread()
        thread_keyFn.start()
        global keyFn
        keyFn = KeyFn()
        keyFn.moveToThread(thread_keyFn)

        global thread_basicFn       # For quit
        thread_basicFn = QThread()
        thread_basicFn.start()
        global basicFn
        basicFn = BasicFn()
        basicFn.moveToThread(thread_basicFn)

        global timeIsPrepared
        timeIsPrepared = False
        global subjectIsPrepared
        subjectIsPrepared = False

        global subjectData
        subjectData = {}

        mainUI.show()
        self.signal()
        sys.exit(app.exec_())
    


    def signal(self) : 
        # << mainUI (1/1) >> --------------------

        ## info_part
        mainUI.onestop_bt.clicked.connect(basicFn.openOnestop)

        ## prepare_part
        mainUI.addSubject_bt.clicked.connect(basicFn.addSubject)
        mainUI.subjectCode_le.returnPressed.connect(basicFn.addSubject)

        ## finale_part
        mainUI.start_bt.clicked.connect(basicFn.classRegistration)




class BasicFn(QObject) : 
    def openOnestop(self) : 
        webbrowser.open("https://onestop.kumoh.ac.kr/")



    def addSubject(self) : 
        subjectName, subjectCode = mainUI.subjectName_le.text(), mainUI.subjectCode_le.text()
        if (subjectName == "") or (subjectCode == "") : 
            print("[system] 교과목정보를 정확하게 입력해 주십시오.")                # Test code / please delete the contents of this line.
        else : 
            print(f"[system] 교과목명 : {subjectName}")             # Test code / please delete the contents of this line.
            print(f"[system] 교과목 코드 : {subjectCode}")                # Test code / please delete the contents of this line.
            subjectData[(subjectName, subjectCode)] = []
            tmp = []
            for major, insurances in subjectData.items() : 
                item = QTreeWidgetItem(major)
                for insurance in insurances : 
                    subItem = QTreeWidgetItem(insurance)
                    item.addChild(subItem)
                tmp.append(item)
            mainUI.subjectBox_tw.clear()
            mainUI.subjectBox_tw.insertTopLevelItems(0, tmp)

            mainUI.subjectName_le.setText(""); mainUI.subjectCode_le.setText("")



    def timeChk(self) : 
        CR_H = int(mainUI.hour_box_le.text())
        CR_M = int(mainUI.min_box_le.text())
        crt_H = time.localtime().tm_hour
        crt_M = time.localtime().tm_min
        crt_S = time.localtime().tm_sec

        if CR_H < crt_H or (CR_H == crt_H and CR_M <= crt_M) : 
            return False

        remaining_H = CR_H - crt_H
        remaining_M = CR_M - crt_M - 1
        remaining_S = 60 - crt_S
        if crt_M >= CR_M : 
            remaining_H -= 1
            remaining_M += 60
        if crt_S == 0 : 
            remaining_M += 1
            remaining_S = 0
        
        return 60*60*remaining_H + 60*remaining_M + remaining_S



    def classRegistration(self) : 
        if (mainUI.ID_box_le.text() == "") or (mainUI.PW_box_le.text() == "") : accountIsPrepared = False
        else : accountIsPrepared = True
        if (int(mainUI.hour_box_le.text()) == 0) and (int(mainUI.min_box_le.text()) == 0) : timeIsPrepared = False
        else : timeIsPrepared = True

        if accountIsPrepared and timeIsPrepared and subjectIsPrepared : 
            remaining_time = self.timeChk()
            if not remaining_time : 
                print("[system] 수강신청 시간이 현재 시간 이전입니다.")                 # Test code / please delete the contents of this line.
                return

            else : 
                H = remaining_time//3600; M = (remaining_time-H*3600)//60; S = remaining_time-H*3600-M*60
                mainUI.time_HM_lcd.display(f"{str(H).zfill(2)}:{str(M).zfill(2)}")
                mainUI.time_S_lcd.display(f":{str(S).zfill(2)}")
                while remaining_time > 0 : 
                    time.sleep(1)
                    remaining_time -= 1
                    H = remaining_time//3600; M = (remaining_time-H*3600)//60; S = remaining_time-H*3600-M*60
                    mainUI.time_HM_lcd.display(f"{str(H).zfill(2)}:{str(M).zfill(2)}")
                    mainUI.time_S_lcd.display(f":{str(S).zfill(2)}")
                keyFn.classRegistration()

        else : 
            mainUI.body_frm.hide()
            mainUI.finale_notPrepared_lb.show()
            mainUI.finale_notPrepared_bt.show()

            if accountIsPrepared : mainUI.account_O_mark_lb.show()
            else : mainUI.account_X_mark_lb.show()
            if timeIsPrepared : mainUI.time_O_mark_lb.show()
            else : mainUI.time_X_mark_lb.show()
            if subjectIsPrepared : mainUI.subject_O_mark_lb.show()
            else : mainUI.subject_X_mark_lb.show()





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    Main()