from img.img import *
import sys
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QRadioButton, QLabel, QButtonGroup
from PySide2.QtCore import Qt, QSize

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

        self.tile_frm = QFrame(self.body_frm)
        self.tile_frm.setGeometry(421, 4, 791, 637)
        self.tile_frm.setStyleSheet("QFrame{\n"
                                            "image : url(:/img/tile.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}")

        self.completed_frm = QFrame(self.tile_frm)
        self.completed_frm.setGeometry(558, 10, 211, 71)
        self.completed_frm.setStyleSheet("QFrame{\n"
                                            "image : url(:/img/completed.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}")

        self.completed_lb = QLabel(self.tile_frm)
        self.completed_lb.setGeometry(619, 43, 91, 31)
        self.completed_lb.setFont(QFont("굴림", 20, QFont.Bold))
        self.completed_lb.setStyleSheet("QLabel{\n"
                                            "color : #ffffff;\n"
                                        "}")
        self.completed_lb.setText("0 / 0")
        self.completed_lb.setAlignment(Qt.AlignCenter)


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


        # finale_part
        self.start_bt = QPushButton(self.tile_frm)
        self.start_bt.setGeometry(429, 574, 341, 51)
        self.start_bt.setStyleSheet("QPushButton{\n"
                                        "image : url(:/img/start_bt_normal.png);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "image : url(:/img/start_bt_hover.png);\n"
                                    "}")
        self.start_bt.hide()



    def signal(self) : 
        self.info_rb.clicked.connect(self.menuSet)
        self.prepare_rb.clicked.connect(self.menuSet)
        self.finale_rb.clicked.connect(self.menuSet)



    def menuSet(self) : 
        if self.info_rb.isChecked() : 
            # prepare_part
            self.account_rb.hide()
            self.time_rb.hide()
            #finale_part
            self.start_bt.hide()
            # info_part
            self.onestop_bt.show()

        elif self.prepare_rb.isChecked() : 
            # info_part
            self.onestop_bt.hide()
            # finale_part
            self.start_bt.hide()
            # prepare_part
            self.account_rb.show()
            self.time_rb.show()

        elif self.finale_rb.isChecked() : 
            # info_part
            self.onestop_bt.hide()
            # prepare_part
            self.account_rb.hide()
            self.time_rb.hide()
            #finale_part
            self.start_bt.show()





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    sys.exit(app.exec_())