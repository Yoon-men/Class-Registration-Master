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
from collections import deque
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

        mainUI.show()
        self.signal()
        sys.exit(app.exec_())
    


    def signal(self) : 
        # << mainUI (1/1) >> --------------------

        ## info_part
        mainUI.onestop_bt.clicked.connect(basicFn.openOnestop)


        ## finale_part
        mainUI.start_bt.clicked.connect(basicFn.classRegistration)




class BasicFn(QObject) : 
    def openOnestop(self) : 
        webbrowser.open("https://onestop.kumoh.ac.kr/")



    def classRegistration(self) : 
        if (mainUI.ID_box_le.text() != "") and (mainUI.PW_box_le.text() != "") : 
            accountIsPrepared = True
        else : 
            accountIsPrepared = False
        
        if accountIsPrepared and timeIsPrepared and subjectIsPrepared : keyFn.classRegistration()
        else : 
            if not accountIsPrepared : 
                print("[system] Your account is not prepared yet.")                 # Test code / please delete the contents of this line.
            if not timeIsPrepared : 
                print("[system] Your class registration time is not prepared yet.")                 # Test code / please delete the contents of this line.
            if not subjectIsPrepared : 
                print("[system] Your subject for Class registration is not prepared yet.")              # Test code / please delete the contents of this line.





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    Main()