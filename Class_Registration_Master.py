'''
======================================================================================
                          < Class_Registration_Master_v1.0 >

'수강신청 마스터'를 사용해 나머지 99%의 사람들에게 당신과의 격차를 확실히 느끼게 해주십시오.

                                 * Made by Yoonmen *

                               - 23.1.29 (SUN) 02:22 -
======================================================================================
'''

import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QThread, QObject, QEvent
from PySide2.QtWidgets import QTreeWidgetItem
from PySide2.QtGui import QIcon
import time

from CRM_mainUI import MainUI
from CRM_keyFn import KeyFn


class Main(QObject) : 
    def __init__(self) : 
        super().__init__()

        global mainUI
        mainUI = MainUI()

        global thread_keyFn
        thread_keyFn = QThread()
        thread_keyFn.start()
        global keyFn
        keyFn = KeyFn()
        keyFn.moveToThread(thread_keyFn)

        global thread_basicFn
        thread_basicFn = QThread()
        thread_basicFn.start()
        global basicFn
        basicFn = BasicFn()
        basicFn.moveToThread(thread_basicFn)

        global subjectData
        subjectData = {}

        global majorSubjectCnt
        majorSubjectCnt = 0

        global power
        power = False

        global subjectIsSaved
        subjectIsSaved = True

        mainUI.show()
        self.signal()
        sys.exit(app.exec_())
    


    def signal(self) : 
        # << mainUI (1/1) >> --------------------

        ## prepare_part
        mainUI.prepare_rb.clicked.connect(self.finale_inProgress)

        mainUI.subjectCode_le.returnPressed.connect(basicFn.addSubject)
        mainUI.addSubject_bt.clicked.connect(basicFn.addSubject)

        mainUI.subjectBox_tw.viewport().installEventFilter(self)

        mainUI.subjectSave_bt.clicked.connect(BasicFn.setSubjectData)
        mainUI.subjectBin_bt.clicked.connect(BasicFn.delSubject)

        mainUI.prepare_rb.clicked.connect(self.chkSubjectSave)
        mainUI.subject_rb.clicked.connect(self.chkSubjectSave)

        ## finale_part
        mainUI.finale_rb.clicked.connect(self.setFinale_lb)

        mainUI.start_bt.clicked.connect(basicFn.classRegistration)
        mainUI.cancel_bt.clicked.connect(self.powerOff)



    def finale_inProgress(self) : 
        if power : 
            mainUI.body_frm.hide()
            mainUI.finale_inProgress_lb.show()
            mainUI.finale_inProgress_bt.show()



    def chkSubjectSave(self) : 
        if mainUI.subject_rb.isChecked() : 
            if not subjectIsSaved : 
                mainUI.savePoint_lb.show()



    def setFinale_lb(self) : 
        if mainUI.university_cb.currentIndex() == 0 : universityIsPrepared = False
        else : universityIsPrepared = True
        if (mainUI.ID_box_le.text() == "") or (mainUI.PW_box_le.text() == "") : accountIsPrepared = False
        else : accountIsPrepared = True
        if (int(mainUI.hour_box_le.text()) == 0) and (int(mainUI.min_box_le.text()) == 0) : timeIsPrepared = False
        else : timeIsPrepared = True
        if (len(subjectData) == 0) or (not subjectIsSaved) : subjectIsPrepared = False
        else : subjectIsPrepared = True

        if universityIsPrepared : mainUI.universityIsPrepared()
        else : mainUI.universityIsNotPrepared()

        if accountIsPrepared : mainUI.accountIsPrepared()
        else : mainUI.accountIsNotPrepared()

        if timeIsPrepared : mainUI.timeIsPrepared()
        else : mainUI.timeIsNotPrepared()

        if subjectIsPrepared : mainUI.subjectIsPrepared()
        else : mainUI.subjectIsNotPrepared()



    def powerOff(self) : 
        global power
        power = False

    

    def eventFilter(self, object, event) : 
        if object == mainUI.subjectBox_tw.viewport() : 
            if event.type() == QEvent.Drop : 
                global subjectIsSaved
                subjectIsSaved = False
                mainUI.savePoint_lb.show()

        return False




class BasicFn(QObject) : 
    def setSubjectBox(self) : 
        tmp = []
        for major, insurances in subjectData.items() : 
            item = QTreeWidgetItem(major)
            for insurance in insurances : 
                subItem = QTreeWidgetItem(insurance)
                item.addChild(subItem)
            tmp.append(item)
        mainUI.subjectBox_tw.clear()
        mainUI.subjectBox_tw.insertTopLevelItems(0, tmp)



    def addSubject(self) : 
        subjectName, subjectCode = mainUI.subjectName_le.text(), mainUI.subjectCode_le.text()
        if (subjectName == "") or (subjectCode == "") : 
            mainUI.body_frm.hide()
            mainUI.subjectError_lb.show()
            mainUI.subjectError_bt.show()
        else : 
            global subjectData
            subjectData[(subjectName, subjectCode)] = []
            basicFn.setSubjectBox()

            global majorSubjectCnt
            majorSubjectCnt += 1
            mainUI.completed_txt_lb.setText(str(majorSubjectCnt))

            mainUI.subjectName_le.setText(""); mainUI.subjectCode_le.setText("")



    def setSubjectData(self) : 
        def recursiveSet(veryMajor, major) : 
            insuranceCnt = major.childCount()
            for j in range(insuranceCnt) : 
                insurance = major.child(j)
                subjectData[(veryMajor.text(0), veryMajor.text(1))].append((insurance.text(0), insurance.text(1)))
                ininsuranceCnt = insurance.childCount()
                if ininsuranceCnt > 0 : 
                    recursiveSet(veryMajor, insurance)


        global subjectData, majorSubjectCnt
        subjectData = {}
        majorSubjectCnt = 0
        for i in range(mainUI.subjectBox_tw.topLevelItemCount()) : 
            major = mainUI.subjectBox_tw.topLevelItem(i)
            subjectData[(major.text(0), major.text(1))] = []
            majorSubjectCnt += 1
            recursiveSet(major, major)

        basicFn.setSubjectBox()
        mainUI.completed_txt_lb.setText(str(majorSubjectCnt))

        global subjectIsSaved
        subjectIsSaved = True
        mainUI.savePoint_lb.hide()



    def delSubject(self) : 
        if mainUI.subjectBox_tw.currentItem() : 
            item = mainUI.subjectBox_tw.currentItem()
            if item.parent() : 
                item.parent().removeChild(item)
            else : 
                mainUI.subjectBox_tw.takeTopLevelItem(mainUI.subjectBox_tw.indexOfTopLevelItem(item))

            basicFn.setSubjectData()



    def timeChk(self) : 
        CR_H = int(mainUI.hour_box_le.text())
        CR_M = int(mainUI.min_box_le.text())
        crt_H = time.localtime().tm_hour
        crt_M = time.localtime().tm_min
        crt_S = time.localtime().tm_sec
        
        total = (CR_H*3600 + CR_M*60) - (crt_H*3600 + crt_M*60 + crt_S)
        if total < 0 : return 0

        return total



    def classRegistration(self) : 
        if mainUI.university_cb.currentIndex() == 0 : universityIsPrepared = False
        else : universityIsPrepared = True
        if (mainUI.ID_box_le.text() == "") or (mainUI.PW_box_le.text() == "") : accountIsPrepared = False
        else : accountIsPrepared = True
        if (int(mainUI.hour_box_le.text()) == 0) and (int(mainUI.min_box_le.text()) == 0) : timeIsPrepared = False
        else : timeIsPrepared = True
        if (len(subjectData) == 0) or (not subjectIsSaved) : subjectIsPrepared = False
        else : subjectIsPrepared = True

        if universityIsPrepared and accountIsPrepared and timeIsPrepared and subjectIsPrepared : 
            remainingTime = self.timeChk()
            
            global power
            power = True
            while (remainingTime > 0) and (power) : 
                if (remainingTime == 300) or (remainingTime == 60) : remainingTime = self.timeChk()
                remainingTime -= 1
                H, M, S = remainingTime//3600, remainingTime%3600//60, remainingTime%60
                mainUI.time_HM_lcd.display(f"{str(H).zfill(2)}:{str(M).zfill(2)}")
                mainUI.time_S_lcd.display(f":{str(S).zfill(2)}")
                time.sleep(1)

            if power : 
                account = (mainUI.ID_box_le.text(), mainUI.PW_box_le.text())
                mainUI.body_frm.hide()
                mainUI.registrationScreen_gif_lb.show()
                mainUI.registrationScreen_txt_lb.show()

                universityNum = mainUI.university_cb.currentIndex()
                if universityNum == 1 : 
                    result = keyFn.classRegistration_KIT(account, subjectData)
                elif universityNum == 2 : 
                    result = keyFn.classRegistration_DNUE(account, subjectData)
                elif universityNum == 3 : 
                    result = keyFn.classRegistration_SKKU(account, subjectData)
                
                mainUI.registrationScreen_gif_lb.hide()
                mainUI.registrationScreen_txt_lb.hide()
                if isinstance(result, dict) : 
                    tmp = []
                    for major, insurances in subjectData.items() : 
                        item = QTreeWidgetItem()
                        item.setText(0, major[0]); item.setText(1, major[1])
                        if not major in result : 
                            item.setIcon(2, QIcon(":/img/o_mark_lb.png"))
                        else : 
                            item.setIcon(2, QIcon(":/img/x_mark_lb.png"))
                            item.setText(3, result[major])
                            for insurance in insurances : 
                                subItem = QTreeWidgetItem()
                                subItem.setText(0, insurance[0]); subItem.setText(1, insurance[1])
                                if not insurance in result : 
                                    subItem.setIcon(2, QIcon(":/img/o_mark_lb.png"))
                                    item.addChild(subItem)
                                    break
                                else : 
                                    subItem.setIcon(2, QIcon(":/img/x_mark_lb.png"))
                                    subItem.setText(3, result[insurance])
                                    item.addChild(subItem)
                        tmp.append(item)
                    mainUI.report_tw.insertTopLevelItems(0, tmp)

                    mainUI.report_tw.show()
                    mainUI.report_tw.expandAll()
                    mainUI.report_bt.show()
                    mainUI.report_lb.show()

                else : 
                    if result == "pageError" : 
                        mainUI.pageError_lb.show()
                        mainUI.pageError_bt.show()
                    elif result == "accountError" : 
                        mainUI.accountError_lb.show()
                        mainUI.accountError_bt.show()
                    elif result == "periodError" : 
                        mainUI.periodError_lb.show()
                        mainUI.periodError_bt.show()

                power = False
                mainUI.changeSCMode()
            
            mainUI.time_HM_lcd.display("--:--"); mainUI.time_S_lcd.display(":--")


        else : 
            mainUI.body_frm.hide()
            mainUI.finale_notPrepared_lb.show()
            mainUI.finale_notPrepared_bt.show()

            if universityIsPrepared : mainUI.university_O_mark_lb.show()
            else : mainUI.university_X_mark_lb.show()
            if accountIsPrepared : mainUI.account_O_mark_lb.show()
            else : mainUI.account_X_mark_lb.show()
            if timeIsPrepared : mainUI.time_O_mark_lb.show()
            else : mainUI.time_X_mark_lb.show()
            if subjectIsPrepared : mainUI.subject_O_mark_lb.show()
            else : mainUI.subject_X_mark_lb.show()





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    Main()
