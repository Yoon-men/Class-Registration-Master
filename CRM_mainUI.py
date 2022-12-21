from img.img import *
import sys
from PySide2.QtGui import QFont, QIntValidator
from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QRadioButton, QLabel, QButtonGroup, QLineEdit, QLCDNumber
from PySide2.QtCore import Qt, QEvent

class MainUI(QMainWindow) : 
    def __init__(self) : 
        super().__init__()

        self.mainUI()
        self.signal()

    def mainUI(self) : 
        # basic_part
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setFixedSize(1215, 662)
        self.setWindowTitle("Class_Registration_Master_v1.0")

        self.superBody_frm = QFrame(self)
        self.superBody_frm.setGeometry(0, 0, 1215, 662)
        self.superBody_frm.setStyleSheet("QFrame{\n"
                                            "background-color : #131514;\n"
                                        "}")

        # body_part
        self.body_frm = QFrame(self)
        self.body_frm.setGeometry(4, 10, 1205, 644)
        self.body_frm.setStyleSheet("QFrame{\n"
                                        "background-color : #131514;\n"
                                        "border : 4px solid #8a2c2c;\n"
                                    "}")

        self.rightLine = QFrame(self.body_frm)
        self.rightLine.setGeometry(429, 0, 3, 640)

        self.topLine = QFrame(self.body_frm)
        self.topLine.setGeometry(1, 34, 431, 3)

        self.tile_lb = QLabel(self.body_frm)
        self.tile_lb.setGeometry(430, 0, 771, 641)
        self.tile_lb.setStyleSheet("QLabel{\n"
                                            "image : url(:/img/tile.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}")

        self.completed_lb = QLabel(self.body_frm)
        self.completed_lb.setGeometry(969, 15, 221, 71)
        self.completed_lb.setStyleSheet("QLabel{\n"
                                            "image : url(:/img/completed.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}")

        self.completed_txt_lb = QLabel(self.body_frm)
        self.completed_txt_lb.setGeometry(1023, 50, 111, 31)
        self.completed_txt_lb.setFont(QFont("굴림", 20, QFont.Bold))
        self.completed_txt_lb.setStyleSheet("QLabel{\n"
                                                "color : #ffffff;\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}")
        self.completed_txt_lb.setText("0 / 0")
        self.completed_txt_lb.setAlignment(Qt.AlignCenter)


        # menu_part
        self.info_rb = QRadioButton(self.body_frm)
        self.info_rb.setGeometry(1, 2, 147, 34)
        self.info_rb.setStyleSheet("QRadioButton::indicator{\n"
                                        "width : 147px;\n"
                                        "height : 34px;\n"
                                    "}\n"
                                    "QRadioButton::indicator::unchecked{\n"
                                        "image : url(:/img/info_rb_normal.png);\n"
                                    "}\n"
                                    "QRadioButton::indicator::hover{\n"
                                        "image : url(:/img/info_rb_hover.png);\n"
                                    "}\n"
                                    "QRadioButton::indicator::checked{\n"
                                        "image : url(:/img/info_rb_checked.png);\n"
                                    "}")
        self.info_rb.setChecked(True)

        self.prepare_rb = QRadioButton(self.body_frm)
        self.prepare_rb.setGeometry(143, 2, 147, 34)
        self.prepare_rb.setStyleSheet("QRadioButton::indicator{\n"
                                            "width : 147px;\n"
                                            "height : 34px;\n"
                                        "}\n"
                                        "QRadioButton::indicator::unchecked{\n"
                                            "image : url(:/img/prepare_rb_normal.png);\n"
                                        "}\n"
                                        "QRadioButton::indicator::hover{\n"
                                            "image : url(:/img/prepare_rb_hover.png);\n"
                                        "}\n"
                                        "QRadioButton::indicator::checked{\n"
                                            "image : url(:/img/prepare_rb_checked.png);\n"
                                        "}")

        self.finale_rb = QRadioButton(self.body_frm)
        self.finale_rb.setGeometry(285, 2, 147, 34)
        self.finale_rb.setStyleSheet("QRadioButton::indicator{\n"
                                        "width : 147px;\n"
                                        "height : 34px;\n"
                                    "}\n"
                                    "QRadioButton::indicator::unchecked{\n"
                                        "image : url(:/img/finale_rb_normal.png);\n"
                                    "}\n"
                                    "QRadioButton::indicator::hover{\n"
                                        "image : url(:/img/finale_rb_hover.png);\n"
                                    "}\n"
                                    "QRadioButton::indicator::checked{\n"
                                        "image : url(:/img/finale_rb_checked.png);\n"
                                    "}")

        self.menuGroup = QButtonGroup(self)
        self.menuGroup.addButton(self.info_rb)
        self.menuGroup.addButton(self.prepare_rb)
        self.menuGroup.addButton(self.finale_rb)


        # info_part
        self.onestop_bt = QPushButton(self.body_frm)
        self.onestop_bt.setGeometry(17, 52, 399, 34)
        self.onestop_bt.setStyleSheet("QPushButton{\n"
                                            "image : url(:/img/onestop_bt_normal.png);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "image : url(:/img/onestop_bt_hover.png);\n"
                                        "}")
        self.onestop_bt.installEventFilter(self)

        self.onestop_img_lb = QLabel(self.body_frm)
        self.onestop_img_lb.setGeometry(471, 91, 376, 441)
        self.onestop_img_lb.setStyleSheet("QLabel{\n"   
                                            "image : url(:/img/onestop_img.png);\n"
                                            "border : 3px solid #8a2c2c;\n"
                                        "}")
        self.onestop_img_lb.hide()

        self.onestop_txt_lb = QLabel(self.body_frm)
        self.onestop_txt_lb.setGeometry(189, 577, 831, 31)
        self.onestop_txt_lb.setStyleSheet("QLabel{\n"
                                            "image : url(:/img/onestop_txt.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}")
        self.onestop_txt_lb.hide()


        # prepare_part
        self.account_rb = QRadioButton(self.body_frm)
        self.account_rb.setGeometry(16, 51, 401, 61)
        self.account_rb.setStyleSheet("QRadioButton::indicator{\n"
                                            "width : 401px;\n"
                                            "height : 111px;\n"
                                        "}\n"
                                        "QRadioButton::indicator::unchecked{\n"
                                            "image : url(:/img/account_rb_normal.png);\n"
                                        "}\n"
                                        "QRadioButton::indicator::hover{\n"
                                            "image : url(:/img/account_rb_hover.png);\n"
                                        "}\n"
                                        "QRadioButton::indicator::checked{\n"
                                            "image : url(:/img/account_rb_checked.png);\n"
                                        "}")
        self.account_rb.setChecked(True)
        self.account_rb.hide()

        self.time_rb = QRadioButton(self.body_frm)
        self.time_rb.setGeometry(16, 125, 401, 61)
        self.time_rb.setStyleSheet("QRadioButton::indicator{\n"
                                        "width : 401px;\n"
                                        "height : 111px;\n"
                                    "}\n"
                                    "QRadioButton::indicator::unchecked{\n"
                                        "image : url(:/img/time_rb_normal.png);\n"
                                    "}\n"
                                    "QRadioButton::indicator::hover{\n"
                                        "image : url(:/img/time_rb_hover.png);\n"
                                    "}\n"
                                    "QRadioButton::indicator::checked{\n"
                                        "image : url(:/img/time_rb_checked.png);\n"
                                    "}")
        self.time_rb.hide()

        self.subject_rb = QRadioButton(self.body_frm)
        self.subject_rb.setGeometry(16, 199, 401, 61)
        self.subject_rb.setStyleSheet("QRadioButton::indicator{\n"
                                            "width : 401px;\n"
                                            "height : 111px;\n"
                                        "}\n"
                                        "QRadioButton::indicator::unchecked{\n"
                                            "image : url(:/img/subject_rb_normal.png);\n"
                                        "}\n"
                                        "QRadioButton::indicator::hover{\n"
                                            "image : url(:/img/subject_rb_hover.png);\n"
                                        "}\n"
                                        "QRadioButton::indicator::checked{\n"
                                            "image : url(:/img/subject_rb_checked.png);\n"
                                        "}")
        self.subject_rb.hide()

        self.mode_account_lb = QLabel(self.body_frm)
        self.mode_account_lb.setGeometry(444, 15, 341, 41)
        self.mode_account_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/mode_account.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}")
        self.mode_account_lb.hide()

        self.mode_time_lb = QLabel(self.body_frm)
        self.mode_time_lb.setGeometry(444, 15, 261, 41)
        self.mode_time_lb.setStyleSheet("QLabel{\n"
                                            "image : url(:/img/mode_time.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}")
        self.mode_time_lb.hide()

        self.mode_subject_lb = QLabel(self.body_frm)
        self.mode_subject_lb.setGeometry(444, 14, 327, 44)
        self.mode_subject_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/mode_subject.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}")
        self.mode_subject_lb.hide()

        self.prepareGroup = QButtonGroup(self)
        self.prepareGroup.addButton(self.account_rb)
        self.prepareGroup.addButton(self.time_rb)
        self.prepareGroup.addButton(self.subject_rb)

        self.accountBox_lb = QLabel(self.body_frm)
        self.accountBox_lb.setGeometry(580, 177, 491, 291)
        self.accountBox_lb.setStyleSheet("QLabel{\n"
                                            "image : url(:/img/accountBox_lb.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}")
        self.accountBox_lb.hide()

        le_styleSheet = ("QLineEdit{\n"
                            "color : #dddddd;\n"
                            "background-color : #232323;\n"
                            "border : 2px solid #8a2c2c;\n"
                            "selection-color : #000000;\n"
                            "selection-background-color : #ffffff;\n"
                        "}\n"
                        "QLineEdit:focus{\n"
                            "border-color : #e14f50;\n"
                        "}")

        self.ID_box_le = QLineEdit(self.body_frm)
        self.ID_box_le.setGeometry(680, 264, 351, 41)
        self.ID_box_le.setFont(QFont("굴림", 14))
        self.ID_box_le.setStyleSheet(le_styleSheet)
        self.ID_box_le.hide()

        self.PW_box_le = QLineEdit(self.body_frm)
        self.PW_box_le.setGeometry(680, 339, 351, 41)
        self.PW_box_le.setFont(QFont("굴림", 14))
        self.PW_box_le.setStyleSheet(le_styleSheet)
        self.PW_box_le.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.PW_box_le.hide()

        self.timeBox_lb = QLabel(self.body_frm)
        self.timeBox_lb.setGeometry(580, 177, 491, 291)
        self.timeBox_lb.setStyleSheet("QLabel{\n"
                                        "image : url(:/img/timeBox_lb.png);\n"
                                        "border : 0px;\n"
                                        "background-color : transparent;\n"
                                    "}")
        self.timeBox_lb.hide()

        self.hour_box_le = QLineEdit(self.body_frm)
        self.hour_box_le.setGeometry(682, 308, 90, 31)
        self.hour_box_le.setFont(QFont("굴림", 14, QFont.ExtraBold))
        self.hour_box_le.setStyleSheet(le_styleSheet)
        self.hour_box_le.setValidator(QIntValidator())
        self.hour_box_le.setAlignment(Qt.AlignCenter)
        self.hour_box_le.setText("0")
        self.hour_box_le.hide()

        self.min_box_le = QLineEdit(self.body_frm)
        self.min_box_le.setGeometry(850, 308, 90, 31)
        self.min_box_le.setFont(QFont("굴림", 14, QFont.ExtraBold))
        self.min_box_le.setStyleSheet(le_styleSheet)
        self.min_box_le.setValidator(QIntValidator())
        self.min_box_le.setAlignment(Qt.AlignCenter)
        self.min_box_le.setText("0")
        self.min_box_le.hide()


        # finale_part
        self.start_bt = QPushButton(self.body_frm)
        self.start_bt.setGeometry(849, 578, 341, 51)
        self.start_bt.setStyleSheet("QPushButton{\n"
                                        "image : url(:/img/start_bt_normal.png);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "image : url(:/img/start_bt_hover.png);\n"
                                    "}")
        self.start_bt.hide()

        self.time_lcd = QLCDNumber(self.body_frm)
        self.time_lcd.setGeometry(555, 210, 521, 221)
        self.time_lcd.setStyleSheet("QLCDNumber{\n"
                                        "color : #4f2120;\n"
                                        "border : 0px;\n"
                                        "background-color : transparent;\n"
                                    "}")
        self.time_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.time_lcd.display("00:00")
        self.time_lcd.hide()

        self.finale_notPrepared_lb = QLabel(self.superBody_frm)
        self.finale_notPrepared_lb.setGeometry(325, 120, 561, 401)
        self.finale_notPrepared_lb.setStyleSheet("QLabel{\n"
                                                    "image : url(:/img/finale_notPrepared_lb.png);\n"
                                                    "border : 0px;\n"
                                                    "background-color : transparent;\n"
                                                "}")
        self.finale_notPrepared_lb.hide()

        self.finale_notPrepared_bt = QPushButton(self.superBody_frm)
        self.finale_notPrepared_bt.setGeometry(340, 458, 529, 53)
        self.finale_notPrepared_bt.setStyleSheet("QPushButton{\n"
                                                    "image : url(:/img/finale_notPrepared_bt_normal.png);\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                    "image : url(:/img/finale_notPrepared_bt_hover.png);\n"
                                                "}")
        self.finale_notPrepared_bt.hide()

        O_mark_styleSheet = ("QLabel{\n"
                                "image : url(:/img/o_mark_lb.png);\n"
                                "border : 0px;\n"
                                "background-color : transparent;\n"
                            "}")
        X_mark_styleSheet = ("QLabel{\n"
                                "image : url(:/img/x_mark_lb.png);\n"
                                "border : 0px;\n"
                                "background-color : transparent;\n"
                            "}")

        self.account_O_mark_lb = QLabel(self.superBody_frm)
        self.account_O_mark_lb.setGeometry(847, 264, 20, 20)
        self.account_O_mark_lb.setStyleSheet(O_mark_styleSheet)
        self.account_O_mark_lb.hide()
        self.account_X_mark_lb = QLabel(self.superBody_frm)
        self.account_X_mark_lb.setGeometry(847, 264, 20, 21)
        self.account_X_mark_lb.setStyleSheet(X_mark_styleSheet)
        self.account_X_mark_lb.hide()

        self.time_O_mark_lb = QLabel(self.superBody_frm)
        self.time_O_mark_lb.setGeometry(847, 311, 20, 20)
        self.time_O_mark_lb.setStyleSheet(O_mark_styleSheet)
        self.time_O_mark_lb.hide()
        self.time_X_mark_lb = QLabel(self.superBody_frm)
        self.time_X_mark_lb.setGeometry(847, 311, 20, 21)
        self.time_X_mark_lb.setStyleSheet(X_mark_styleSheet)
        self.time_X_mark_lb.hide()

        self.subject_O_mark_lb = QLabel(self.superBody_frm)
        self.subject_O_mark_lb.setGeometry(847, 359, 20, 20)
        self.subject_O_mark_lb.setStyleSheet(O_mark_styleSheet)
        self.subject_O_mark_lb.hide()
        self.subject_X_mark_lb = QLabel(self.superBody_frm)
        self.subject_X_mark_lb.setGeometry(847, 359, 20, 21)
        self.subject_X_mark_lb.setStyleSheet(X_mark_styleSheet)
        self.subject_X_mark_lb.hide()



    def signal(self) : 
        self.info_rb.clicked.connect(self.setMenu)
        self.prepare_rb.clicked.connect(self.setMenu)
        self.finale_rb.clicked.connect(self.setMenu)

        self.account_rb.clicked.connect(self.setMode)
        self.time_rb.clicked.connect(self.setMode)
        self.subject_rb.clicked.connect(self.setMode)

        self.hour_box_le.textChanged.connect(self.setTime)
        self.min_box_le.textChanged.connect(self.setTime)

        self.finale_notPrepared_bt.clicked.connect(self.returnToMain)



    def setMenu(self) : 
        if self.info_rb.isChecked() : 
            # prepare_part
            self.account_rb.hide()
            self.time_rb.hide()
            self.subject_rb.hide()
            if self.account_rb.isChecked() : 
                self.mode_account_lb.hide()
                self.accountBox_lb.hide()
                self.ID_box_le.hide()
                self.PW_box_le.hide()
            elif self.time_rb.isChecked() : 
                self.mode_time_lb.hide()
                self.timeBox_lb.hide()
                self.hour_box_le.hide()
                self.min_box_le.hide()
            elif self.subject_rb.isChecked() : 
                self.mode_subject_lb.hide()
            #finale_part
            self.start_bt.hide()
            self.time_lcd.hide()
            # info_part
            self.onestop_bt.show()

        elif self.prepare_rb.isChecked() : 
            # info_part
            self.onestop_bt.hide()
            # finale_part
            self.start_bt.hide()
            self.time_lcd.hide()
            # prepare_part
            self.account_rb.show()
            self.time_rb.show()
            self.subject_rb.show()
            if self.account_rb.isChecked() : 
                self.mode_account_lb.show()
                self.accountBox_lb.show()
                self.ID_box_le.show()
                self.PW_box_le.show()
            elif self.time_rb.isChecked() : 
                self.mode_time_lb.show()
                self.timeBox_lb.show()
                self.hour_box_le.show()
                self.min_box_le.show()
            elif self.subject_rb.isChecked() : 
                self.mode_subject_lb.show()

        elif self.finale_rb.isChecked() : 
            # info_part
            self.onestop_bt.hide()
            # prepare_part
            self.account_rb.hide()
            self.time_rb.hide()
            self.subject_rb.hide()
            if self.account_rb.isChecked() : 
                self.mode_account_lb.hide()
                self.accountBox_lb.hide()
                self.ID_box_le.hide()
                self.PW_box_le.hide()
            elif self.time_rb.isChecked() : 
                self.mode_time_lb.hide()
                self.timeBox_lb.hide()
                self.hour_box_le.hide()
                self.min_box_le.hide()
            elif self.subject_rb.isChecked() : 
                self.mode_subject_lb.hide()
            #finale_part
            self.start_bt.show()
            self.time_lcd.show()



    def setMode(self) : 
        if self.account_rb.isChecked() : 
            self.mode_time_lb.hide()
            self.timeBox_lb.hide()
            self.hour_box_le.hide()
            self.min_box_le.hide()
            self.mode_subject_lb.hide()
            self.mode_account_lb.show()
            self.accountBox_lb.show()
            self.ID_box_le.show()
            self.PW_box_le.show()
        elif self.time_rb.isChecked() : 
            self.mode_account_lb.hide()
            self.accountBox_lb.hide()
            self.ID_box_le.hide()
            self.PW_box_le.hide()
            self.mode_subject_lb.hide()
            self.mode_time_lb.show()
            self.timeBox_lb.show()
            self.hour_box_le.show()
            self.min_box_le.show()
        elif self.subject_rb.isChecked() : 
            self.mode_account_lb.hide()
            self.accountBox_lb.hide()
            self.ID_box_le.hide()
            self.PW_box_le.hide()
            self.mode_time_lb.hide()
            self.timeBox_lb.hide()
            self.hour_box_le.hide()
            self.min_box_le.hide()
            self.mode_subject_lb.show()



    def setTime(self) : 
        if self.hour_box_le.text() == "" : 
            self.hour_box_le.setText("0")
            self.hour_box_le.selectAll()
        if int(self.hour_box_le.text()) > 0 : 
            self.hour_box_le.setText(str(int(self.hour_box_le.text())))
        if int(self.hour_box_le.text()) > 24 : 
            self.hour_box_le.setText(str(int(self.hour_box_le.text())%24))

        if self.min_box_le.text() == "" : 
            self.min_box_le.setText("0")
            self.min_box_le.selectAll()
        if int(self.min_box_le.text()) > 0 : 
            self.min_box_le.setText(str(int(self.min_box_le.text())))
        if int(self.min_box_le.text()) > 59 : 
            self.min_box_le.setText(str(int(self.min_box_le.text())%60))
        
        if int(self.hour_box_le.text()) == 24 : 
            self.min_box_le.setText("0")
        
        self.time_lcd.display(f"{self.hour_box_le.text().zfill(2)}:{self.min_box_le.text().zfill(2)}")



    def returnToMain(self) : 
        self.finale_notPrepared_lb.hide()
        self.account_X_mark_lb.hide() ; self.account_O_mark_lb.hide()
        self.time_X_mark_lb.hide() ; self.time_O_mark_lb.hide()
        self.subject_X_mark_lb.hide() ; self.subject_O_mark_lb.hide()
        self.finale_notPrepared_bt.hide()
        self.body_frm.show()



    def eventFilter(self, object, event) : 
        if event.type() == QEvent.HoverEnter : 
            self.onestop_img_lb.show()
            self.onestop_txt_lb.show()
        if event.type() == QEvent.HoverLeave : 
            self.onestop_img_lb.hide()
            self.onestop_txt_lb.hide()
        return False





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    sys.exit(app.exec_())