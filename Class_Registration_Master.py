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
from PySide2.QtCore import QThread, QCoreApplication, QEvent, QObject, Qt
import time
import webbrowser
from collections import deque

from CRM_mainUI import MainUI
from CRM_registration import Fn

class Main(QObject) : 
    def __init__(self) : 
        super().__init__()

        global mainUI
        mainUI = MainUI()

        global thread_fn
        thread_fn = QThread()
        thread_fn.start()
        global fn
        fn = Fn()
        fn.moveToThread(thread_fn)

        mainUI.show()
        self.signal()
        sys.exit(app.exec_())
    


    def signal(self) : 
        # << mainUI (1/1) >> --------------------
        mainUI.onestop_bt.clicked.connect(fn.classRegistration)                 # Test code / please modify the contents of this line.





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    Main()