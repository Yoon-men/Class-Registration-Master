from img.img import *
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFrame, QPushButton, QRadioButton, QLabel, QButtonGroup, QLineEdit, QLCDNumber, QCheckBox, QTreeWidget, QAbstractItemView, QComboBox
from PySide2.QtGui import QFont, QIntValidator
from PySide2.QtCore import Qt, QEvent


global SCMode
SCMode = "start"

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
        self.completed_txt_lb.setText("0")
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
        self.university_rb = QRadioButton(self.body_frm)
        self.university_rb.setGeometry(16, 51, 401, 61)
        self.university_rb.setStyleSheet("QRadioButton::indicator{\n"
                                            "width : 401px;\n"
                                            "height : 111px;\n"
                                        "}\n"
                                        "QRadioButton::indicator::unchecked{\n"
                                            "image : url(:/img/university_rb_normal.png);\n"
                                        "}\n"
                                        "QRadioButton::indicator::hover{\n"
                                            "image : url(:/img/university_rb_hover.png);\n"
                                        "}\n"
                                        "QRadioButton::indicator::checked{\n"
                                            "image : url(:/img/university_rb_checked.png);\n"
                                        "}")
        self.university_rb.setChecked(True)
        self.university_rb.hide()

        self.account_rb = QRadioButton(self.body_frm)
        self.account_rb.setGeometry(16, 125, 401, 61)
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
        self.account_rb.hide()

        self.time_rb = QRadioButton(self.body_frm)
        self.time_rb.setGeometry(16, 199, 401, 61)
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
        self.subject_rb.setGeometry(16, 273, 401, 61)
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

        self.mode_university_lb = QLabel(self.body_frm)
        self.mode_university_lb.setGeometry(444, 11, 380, 50)
        self.mode_university_lb.setStyleSheet("QLabel{\n"
                                                    "image : url(:/img/mode_university.png);\n"
                                                    "border : 0px;\n"
                                                    "background-color : transparent;\n"
                                                "}")
        self.mode_university_lb.hide()

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
        self.prepareGroup.addButton(self.university_rb)
        self.prepareGroup.addButton(self.account_rb)
        self.prepareGroup.addButton(self.time_rb)
        self.prepareGroup.addButton(self.subject_rb)

        self.universityBox_lb = QLabel(self.body_frm)
        self.universityBox_lb.setGeometry(580, 177, 491, 291)
        self.universityBox_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/universityBox_lb.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}")
        self.universityBox_lb.hide()

        self.university_cb = QComboBox(self.body_frm)
        self.university_cb.setGeometry(675, 310, 300, 40)
        self.setUniversity_cb_StyleSheet(138)
        self.university_cb.addItem("---")
        self.university_cb.addItem("KIT")
        self.university_cb.addItem("DNUE")
        self.university_cb.addItem("SKKU")
        self.university_cb.hide()

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
        self.PW_box_le.setEchoMode(QLineEdit.Password)
        self.PW_box_le.hide()

        self.PW_show_ckb = QCheckBox(self.body_frm)
        self.PW_show_ckb.setGeometry(986, 342, 35, 35)
        self.PW_show_ckb.setStyleSheet("QCheckBox::indicator::unchecked{\n"
                                            "image : url(:/img/PW_show_normal.png);\n"
                                            "width : 35px;\n"
                                            "height : 35px;\n"
                                        "}\n"
                                        "QCheckBox::indicator::unchecked::hover{\n"
                                            "image : url(:/img/PW_show_hover.png);\n"
                                        "}\n"
                                        
                                        "QCheckBox::indicator::checked{\n"
                                            "image : url(:/img/PW_hide_normal.png);\n"
                                            "width : 35px;\n"
                                            "height : 35px;\n"
                                        "}\n"
                                        "QCheckBox::indicator::checked::hover{\n"
                                            "image : url(:/img/PW_hide_hover.png);\n"
                                        "}")
        self.PW_show_ckb.hide()

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

        self.addSubject_lb = QLabel(self.body_frm)
        self.addSubject_lb.setGeometry(546, 142, 540, 50)
        self.addSubject_lb.setStyleSheet("QLabel{\n"
                                            "border : 3px solid #8a2c2c;\n"
                                            "background-color : #131514;\n"
                                        "}")
        self.addSubject_lb.hide()

        self.subjectName_le = QLineEdit(self.body_frm)
        self.subjectName_le.setGeometry(555, 152, 239, 30)
        self.subjectName_le.setFont(QFont("굴림", 12))
        self.subjectName_le.setStyleSheet(le_styleSheet)
        self.subjectName_le.setPlaceholderText("(교과목명)")
        self.subjectName_le.hide()

        self.subjectCode_le = QLineEdit(self.body_frm)
        self.subjectCode_le.setGeometry(800, 152, 180, 30)
        self.subjectCode_le.setFont(QFont("굴림", 12))
        self.subjectCode_le.setStyleSheet(le_styleSheet)
        self.subjectCode_le.setPlaceholderText("(교과목코드)")
        self.subjectCode_le.hide()

        self.addSubject_bt = QPushButton(self.body_frm)
        self.addSubject_bt.setGeometry(986, 152, 91, 30)
        self.addSubject_bt.setFont(QFont("나눔고딕OTF", 12, QFont.ExtraBold))
        self.addSubject_bt.setStyleSheet("QPushButton{\n"
                                            "border : 2px solid #8a2c2c;\n"
                                            "background-color : #131514;\n"
                                            "color : #ffffff;\n"
                                        "}\n"
                                        "QPushButton::hover{\n"
                                            "background-color : #e14f50;\n"
                                            "color : #000000;\n"
                                        "}")
        self.addSubject_bt.setText("추가")
        self.addSubject_bt.setFocusPolicy(Qt.NoFocus)
        self.addSubject_bt.hide()

        self.subjectBox_tw = QTreeWidget(self.body_frm)
        self.subjectBox_tw.setGeometry(546, 200, 541, 301)
        self.subjectBox_tw.setFont(QFont("나눔고딕OTF", 13, QFont.Bold))
        self.subjectBox_tw.setStyleSheet("QTreeWidget{\n"
                                            "border : 3px solid #8a2c2c;\n"
                                            "background-color : #131514;\n"
                                            "color : #ffffff;\n"
                                        "}\n"

                                        "QHeaderView{\n"
                                            "border : 0px;\n"
                                        "}\n"
                                        "QHeaderView::section{\n"
                                            "border : 1px solid #8a2c2c;\n"
                                            "background-color : #642223;\n"
                                            "font-family : 나눔고딕OTF;\n"
                                            "font-weight : bold;\n"
                                            "font-size : 13pt;\n"
                                            "color : #ffffff;\n"
                                        "}\n"

                                        "QTreeWidget::item::selected{\n"
                                            "background-color : #434343;\n"
                                            "color : #ffffff;\n"
                                        "}\n"
                                        "QTreeWidget::item::hover{\n"
                                            "background-color : #434343;\n"
                                        "}\n"

                                        "QTreeView::branch:has-children:!has-siblings:closed,\n"
                                        "QTreeView::branch:closed:has-children:has-siblings{\n"
                                            "border-image : none;\n"
                                            "image : url(:/img/branch_closed.png);\n"
                                        "}\n"
                                        "QTreeView::branch:open:has-children:!has-siblings,\n"
                                        "QTreeView::branch:open:has-children:has-siblings{\n"
                                            "border-image : none;\n"
                                            "image : url(:/img/branch_open.png);\n"
                                        "}")
        self.subjectBox_tw.setColumnWidth(0, 350)
        self.subjectBox_tw.setHeaderLabels(["교과목명", "교과목코드"])
        self.subjectBox_tw.setFocusPolicy(Qt.NoFocus)
        self.subjectBox_tw.setDragDropMode(QAbstractItemView.DragDrop)
        self.subjectBox_tw.setDefaultDropAction(Qt.MoveAction)
        self.subjectBox_tw.hide()

        self.subjectBin_bt = QPushButton(self.body_frm)
        self.subjectBin_bt.setGeometry(1092, 461, 41, 41)
        self.subjectBin_bt.setStyleSheet("QPushButton{\n"
                                            "image : url(:/img/subjectBin_bt_normal.png);\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                            "image : url(:/img/subjectBin_bt_hover.png);\n"
                                        "}")
        self.subjectBin_bt.hide()

        self.subjectSave_bt = QPushButton(self.body_frm)
        self.subjectSave_bt.setGeometry(1092, 415, 41, 41)
        self.subjectSave_bt.setStyleSheet("QPushButton{\n"
                                                "image : url(:/img/subjectSave_bt_normal.png);\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                                "image : url(:/img/subjectSave_bt_hover.png);\n"
                                            "}")
        self.subjectSave_bt.hide()

        self.savePoint_lb = QLabel(self.body_frm)
        self.savePoint_lb.setGeometry(1139, 431, 8, 8)
        self.savePoint_lb.setStyleSheet("QLabel{\n"
                                            "image : url(:/img/savePoint.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}")
        self.savePoint_lb.hide()

        error_bt_styleSheet = ("QPushButton{\n"
                                    "image : url(:/img/finale_notPrepared_bt_normal.png);\n"
                                "}\n"
                                "QPushButton:hover{\n"
                                    "image : url(:/img/finale_notPrepared_bt_hover.png);\n"
                                "}")

        self.subjectError_lb = QLabel(self.superBody_frm)
        self.subjectError_lb.setGeometry(325, 120, 561, 401)
        self.subjectError_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/subjectError_lb.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}")
        self.subjectError_lb.hide()

        self.subjectError_bt = QPushButton(self.superBody_frm)
        self.subjectError_bt.setGeometry(340, 458, 529, 53)
        self.subjectError_bt.setStyleSheet(error_bt_styleSheet)
        self.subjectError_bt.hide()


        # finale_part
        self.start_bt = QPushButton(self.body_frm)
        self.start_bt.setGeometry(849, 578, 341, 51)
        self.start_bt.setStyleSheet("QPushButton{\n"
                                        "image : url(:/img/start_bt_normal.png);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "image : url(:/img/start_bt_hover.png);\n"
                                    "}")
        self.start_bt.setFocusPolicy(Qt.NoFocus)
        self.start_bt.hide()

        self.cancel_bt = QPushButton(self.body_frm)
        self.cancel_bt.setGeometry(849, 578, 341, 51)
        self.cancel_bt.setStyleSheet("QPushButton{\n"
                                        "image : url(:/img/cancel_bt_normal.png);\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                        "image : url(:/img/cancel_bt_hover.png);\n"
                                    "}")
        self.cancel_bt.setFocusPolicy(Qt.NoFocus)
        self.cancel_bt.hide()

        lcd_styleSheet = ("QLCDNumber{\n"
                            "color : #4f2120;\n"
                            "border : 0px;\n"
                            "background-color : transparent;\n"
                        "}")
        self.time_HM_lcd = QLCDNumber(self.body_frm)
        self.time_HM_lcd.setGeometry(555, 253, 331, 141)
        self.time_HM_lcd.setStyleSheet(lcd_styleSheet)
        self.time_HM_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.time_HM_lcd.display("--:--")
        self.time_HM_lcd.hide()

        self.time_S_lcd = QLCDNumber(self.body_frm)
        self.time_S_lcd.setGeometry(745, 253, 331, 141)
        self.time_S_lcd.setStyleSheet(lcd_styleSheet)
        self.time_S_lcd.setSegmentStyle(QLCDNumber.Flat)
        self.time_S_lcd.display(":--")
        self.time_S_lcd.hide()

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
        self.finale_notPrepared_bt.setStyleSheet(error_bt_styleSheet)
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

        self.university_O_mark_lb = QLabel(self.superBody_frm)
        self.university_O_mark_lb.setGeometry(847, 246, 20, 20)
        self.university_O_mark_lb.setStyleSheet(O_mark_styleSheet)
        self.university_O_mark_lb.hide()
        self.university_X_mark_lb = QLabel(self.superBody_frm)
        self.university_X_mark_lb.setGeometry(847, 246, 20, 20)
        self.university_X_mark_lb.setStyleSheet(X_mark_styleSheet)
        self.university_X_mark_lb.hide()

        self.account_O_mark_lb = QLabel(self.superBody_frm)
        self.account_O_mark_lb.setGeometry(847, 293, 20, 20)
        self.account_O_mark_lb.setStyleSheet(O_mark_styleSheet)
        self.account_O_mark_lb.hide()
        self.account_X_mark_lb = QLabel(self.superBody_frm)
        self.account_X_mark_lb.setGeometry(847, 293, 20, 21)
        self.account_X_mark_lb.setStyleSheet(X_mark_styleSheet)
        self.account_X_mark_lb.hide()

        self.time_O_mark_lb = QLabel(self.superBody_frm)
        self.time_O_mark_lb.setGeometry(847, 340, 20, 20)
        self.time_O_mark_lb.setStyleSheet(O_mark_styleSheet)
        self.time_O_mark_lb.hide()
        self.time_X_mark_lb = QLabel(self.superBody_frm)
        self.time_X_mark_lb.setGeometry(847, 340, 20, 21)
        self.time_X_mark_lb.setStyleSheet(X_mark_styleSheet)
        self.time_X_mark_lb.hide()

        self.subject_O_mark_lb = QLabel(self.superBody_frm)
        self.subject_O_mark_lb.setGeometry(847, 388, 20, 20)
        self.subject_O_mark_lb.setStyleSheet(O_mark_styleSheet)
        self.subject_O_mark_lb.hide()
        self.subject_X_mark_lb = QLabel(self.superBody_frm)
        self.subject_X_mark_lb.setGeometry(847, 388, 20, 21)
        self.subject_X_mark_lb.setStyleSheet(X_mark_styleSheet)
        self.subject_X_mark_lb.hide()

        self.finale_inProgress_lb = QLabel(self.superBody_frm)
        self.finale_inProgress_lb.setGeometry(325, 120, 561, 401)
        self.finale_inProgress_lb.setStyleSheet("QLabel{\n"
                                                    "image : url(:/img/finale_inProgress_lb.png);\n"
                                                    "border : 0px;\n"
                                                    "background-color : transparent;\n"
                                                "}")
        self.finale_inProgress_lb.hide()

        self.finale_inProgress_bt = QPushButton(self.superBody_frm)
        self.finale_inProgress_bt.setGeometry(340, 458, 529, 53)
        self.finale_inProgress_bt.setStyleSheet(error_bt_styleSheet)
        self.finale_inProgress_bt.hide()

        self.finaleUniversity_lb = QLabel(self.body_frm)
        self.finaleUniversity_lb.setGeometry(17, 52, 399, 34)
        self.universityIsNotPrepared()
        self.finaleUniversity_lb.installEventFilter(self)
        self.finaleUniversity_lb.hide()
        

        self.finaleAccount_lb = QLabel(self.body_frm)
        self.finaleAccount_lb.setGeometry(17, 100, 399, 34)
        self.accountIsNotPrepared()
        self.finaleAccount_lb.installEventFilter(self)
        self.finaleAccount_lb.hide()

        self.finaleTime_lb = QLabel(self.body_frm)
        self.finaleTime_lb.setGeometry(17, 148, 399, 34)
        self.timeIsNotPrepared()
        self.finaleTime_lb.installEventFilter(self)
        self.finaleTime_lb.hide()

        self.finaleSubject_lb = QLabel(self.body_frm)
        self.finaleSubject_lb.setGeometry(17, 196, 399, 34)
        self.subjectIsNotPrepared()
        self.finaleSubject_lb.installEventFilter(self)
        self.finaleSubject_lb.hide()

        self.registrationScreen_txt_lb = QLabel(self.superBody_frm)
        self.registrationScreen_txt_lb.setGeometry(320, 300, 581, 61)
        self.registrationScreen_txt_lb.setStyleSheet("QLabel{\n"
                                                        "image : url(:/img/registrationScreen_txt_lb.png);\n"
                                                        "border : 0px;\n"
                                                        "background-color : transparent;\n"
                                                    "}")
        self.registrationScreen_txt_lb.hide()

        self.pageError_lb = QLabel(self.superBody_frm)
        self.pageError_lb.setGeometry(325, 120, 561, 401)
        self.pageError_lb.setStyleSheet("QLabel{\n"
                                            "image : url(:/img/pageError_lb.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}")
        self.pageError_lb.hide()

        self.pageError_bt = QPushButton(self.superBody_frm)
        self.pageError_bt.setGeometry(340, 458, 529, 53)
        self.pageError_bt.setStyleSheet(error_bt_styleSheet)
        self.pageError_bt.hide()

        self.accountError_lb = QLabel(self.superBody_frm)
        self.accountError_lb.setGeometry(325, 120, 561, 401)
        self.accountError_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/accountError_lb.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}")
        self.accountError_lb.hide()

        self.accountError_bt = QPushButton(self.superBody_frm)
        self.accountError_bt.setGeometry(340, 458, 529, 53)
        self.accountError_bt.setStyleSheet(error_bt_styleSheet)
        self.accountError_bt.hide()

        self.periodError_lb = QLabel(self.superBody_frm)
        self.periodError_lb.setGeometry(325, 120, 561, 401)
        self.periodError_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/periodError_lb.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}")
        self.periodError_lb.hide()

        self.periodError_bt = QPushButton(self.superBody_frm)
        self.periodError_bt.setGeometry(340, 458, 529, 53)
        self.periodError_bt.setStyleSheet(error_bt_styleSheet)
        self.periodError_bt.hide()



    def signal(self) : 
        self.info_rb.clicked.connect(self.setMenu)
        self.prepare_rb.clicked.connect(self.setMenu)
        self.finale_rb.clicked.connect(self.setMenu)

        self.university_rb.clicked.connect(self.setMode)
        self.account_rb.clicked.connect(self.setMode)
        self.time_rb.clicked.connect(self.setMode)
        self.subject_rb.clicked.connect(self.setMode)

        self.university_cb.currentIndexChanged.connect(self.setUniversity_cb_Alignment)

        self.PW_show_ckb.stateChanged.connect(self.showPW)

        self.hour_box_le.textChanged.connect(self.setTime)
        self.min_box_le.textChanged.connect(self.setTime)

        self.start_bt.clicked.connect(self.changeSCMode)
        self.cancel_bt.clicked.connect(self.changeSCMode)

        self.finale_notPrepared_bt.clicked.connect(self.returnToMain_finale_notPrepared)
        self.finale_inProgress_bt.clicked.connect(self.returnToMain_finale_inProgress)
        self.subjectError_bt.clicked.connect(self.returnToMain_subjectError)
        self.pageError_bt.clicked.connect(self.returnToMain_pageError)
        self.accountError_bt.clicked.connect(self.returnToMain_accountError)
        self.periodError_bt.clicked.connect(self.returnToMain_periodError)



    def setMenu(self) : 
        if self.info_rb.isChecked() : 
            # prepare_part
            self.university_rb.hide()
            self.account_rb.hide()
            self.time_rb.hide()
            self.subject_rb.hide()
            if self.university_rb.isChecked() : 
                self.mode_university_lb.hide()
                self.universityBox_lb.hide()
                self.university_cb.hide()
            elif self.account_rb.isChecked() : 
                self.mode_account_lb.hide()
                self.accountBox_lb.hide()
                self.ID_box_le.hide()
                self.PW_box_le.hide()
                self.PW_show_ckb.hide()
            elif self.time_rb.isChecked() : 
                self.mode_time_lb.hide()
                self.timeBox_lb.hide()
                self.hour_box_le.hide()
                self.min_box_le.hide()
            elif self.subject_rb.isChecked() : 
                self.mode_subject_lb.hide()
                self.addSubject_lb.hide(); self.subjectName_le.hide(); self.subjectCode_le.hide(); self.addSubject_bt.hide()
                self.subjectBox_tw.hide()
                self.subjectBin_bt.hide()
                self.subjectSave_bt.hide()
                self.savePoint_lb.hide()
            #finale_part
            self.start_bt.hide()
            self.cancel_bt.hide()
            self.time_HM_lcd.hide(); self.time_S_lcd.hide()
            self.finaleUniversity_lb.hide()
            self.finaleAccount_lb.hide()
            self.finaleTime_lb.hide()
            self.finaleSubject_lb.hide()
            # info_part
            self.onestop_bt.show()

        elif self.prepare_rb.isChecked() : 
            # info_part
            self.onestop_bt.hide()
            # finale_part
            self.start_bt.hide()
            self.cancel_bt.hide()
            self.time_HM_lcd.hide(); self.time_S_lcd.hide()
            self.finaleUniversity_lb.hide()
            self.finaleAccount_lb.hide()
            self.finaleTime_lb.hide()
            self.finaleSubject_lb.hide()
            # prepare_part
            self.university_rb.show()
            self.account_rb.show()
            self.time_rb.show()
            self.subject_rb.show()
            if self.university_rb.isChecked() : 
                self.mode_university_lb.show()
                self.universityBox_lb.show()
                self.university_cb.show()
            elif self.account_rb.isChecked() : 
                self.mode_account_lb.show()
                self.accountBox_lb.show()
                self.ID_box_le.show()
                self.PW_box_le.show()
                self.PW_show_ckb.show()
            elif self.time_rb.isChecked() : 
                self.mode_time_lb.show()
                self.timeBox_lb.show()
                self.hour_box_le.show()
                self.min_box_le.show()
            elif self.subject_rb.isChecked() : 
                self.mode_subject_lb.show()
                self.addSubject_lb.show(); self.subjectName_le.show(); self.subjectCode_le.show(); self.addSubject_bt.show()
                self.subjectBox_tw.show()
                self.subjectBin_bt.show()
                self.subjectSave_bt.show()

        elif self.finale_rb.isChecked() : 
            # info_part
            self.onestop_bt.hide()
            # prepare_part
            self.university_rb.hide()
            self.account_rb.hide()
            self.time_rb.hide()
            self.subject_rb.hide()
            if self.university_rb.isChecked() : 
                self.mode_university_lb.hide()
                self.universityBox_lb.hide()
                self.university_cb.hide()
            elif self.account_rb.isChecked() : 
                self.mode_account_lb.hide()
                self.accountBox_lb.hide()
                self.ID_box_le.hide()
                self.PW_box_le.hide()
                self.PW_show_ckb.hide()
            elif self.time_rb.isChecked() : 
                self.mode_time_lb.hide()
                self.timeBox_lb.hide()
                self.hour_box_le.hide()
                self.min_box_le.hide()
            elif self.subject_rb.isChecked() : 
                self.mode_subject_lb.hide()
                self.addSubject_lb.hide(); self.subjectName_le.hide(); self.subjectCode_le.hide(); self.addSubject_bt.hide()
                self.subjectBox_tw.hide()
                self.subjectBin_bt.hide()
                self.subjectSave_bt.hide()
                self.savePoint_lb.hide()
            #finale_part
            if SCMode == "start" : 
                self.start_bt.show()
            elif SCMode == "cancel" : 
                self.cancel_bt.show()
            self.time_HM_lcd.show(); self.time_S_lcd.show()
            self.finaleUniversity_lb.show()
            self.finaleAccount_lb.show()
            self.finaleTime_lb.show()
            self.finaleSubject_lb.show()



    def setMode(self) : 
        if self.university_rb.isChecked() : 
            self.mode_account_lb.hide()
            self.accountBox_lb.hide()
            self.ID_box_le.hide()
            self.PW_box_le.hide()
            self.PW_show_ckb.hide()
            self.mode_time_lb.hide()
            self.timeBox_lb.hide()
            self.hour_box_le.hide()
            self.min_box_le.hide()
            self.mode_subject_lb.hide()
            self.addSubject_lb.hide(); self.subjectName_le.hide(); self.subjectCode_le.hide(); self.addSubject_bt.hide()
            self.subjectBox_tw.hide()
            self.subjectBin_bt.hide()
            self.subjectSave_bt.hide()
            self.savePoint_lb.hide()
            self.mode_university_lb.show()
            self.universityBox_lb.show()
            self.university_cb.show()
        elif self.account_rb.isChecked() : 
            self.mode_university_lb.hide()
            self.universityBox_lb.hide()
            self.university_cb.hide()
            self.mode_time_lb.hide()
            self.timeBox_lb.hide()
            self.hour_box_le.hide()
            self.min_box_le.hide()
            self.mode_subject_lb.hide()
            self.addSubject_lb.hide(); self.subjectName_le.hide(); self.subjectCode_le.hide(); self.addSubject_bt.hide()
            self.subjectBox_tw.hide()
            self.subjectBin_bt.hide()
            self.subjectSave_bt.hide()
            self.savePoint_lb.hide()
            self.mode_account_lb.show()
            self.accountBox_lb.show()
            self.ID_box_le.show()
            self.PW_box_le.show()
            self.PW_show_ckb.show()
        elif self.time_rb.isChecked() : 
            self.mode_university_lb.hide()
            self.universityBox_lb.hide()
            self.university_cb.hide()
            self.mode_account_lb.hide()
            self.accountBox_lb.hide()
            self.ID_box_le.hide()
            self.PW_box_le.hide()
            self.PW_show_ckb.hide()
            self.mode_subject_lb.hide()
            self.addSubject_lb.hide(); self.subjectName_le.hide(); self.subjectCode_le.hide(); self.addSubject_bt.hide()
            self.subjectBox_tw.hide()
            self.subjectBin_bt.hide()
            self.subjectSave_bt.hide()
            self.savePoint_lb.hide()
            self.mode_time_lb.show()
            self.timeBox_lb.show()
            self.hour_box_le.show()
            self.min_box_le.show()
        elif self.subject_rb.isChecked() : 
            self.mode_university_lb.hide()
            self.universityBox_lb.hide()
            self.university_cb.hide()
            self.mode_account_lb.hide()
            self.accountBox_lb.hide()
            self.ID_box_le.hide()
            self.PW_box_le.hide()
            self.PW_show_ckb.hide()
            self.mode_time_lb.hide()
            self.timeBox_lb.hide()
            self.hour_box_le.hide()
            self.min_box_le.hide()
            self.mode_subject_lb.show()
            self.addSubject_lb.show(); self.subjectName_le.show(); self.subjectCode_le.show(); self.addSubject_bt.show()
            self.subjectBox_tw.show()
            self.subjectBin_bt.show()
            self.subjectSave_bt.show()



    def setUniversity_cb_StyleSheet(self, px) : 
        self.university_cb.setStyleSheet("QComboBox{\n"
                                            "font-family : 나눔고딕OTF;\n"
                                            "font-weight : bold;\n"
                                            "font-size : 15pt;\n"
                                            "border-radius : 5px;\n"
                                            "color : #cccccc;\n"
                                            "background-color : #303030;\n"
                                            f"padding-left : {px}px;\n"
                                        "}\n"
                                        "QComboBox QAbstractItemView{\n"
                                            "border : 2px solid #aaaaaa;\n"
                                            "border-radius : 0px;\n"
                                            "background-color : #303030;\n"
                                            "color : #cccccc;\n"
                                            "selection-background-color : #ffffff;\n"
                                            "selection-color : #000000;\n"
                                            "outline : 0px;\n"
                                        "}\n"
                                        "QComboBox::down-arrow{\n"
                                            "image : url(:/img/drop_down.png);\n"
                                            "width : 18px;\n"
                                            "height : 18px;\n"
                                        "}\n"
                                        "QComboBox::drop-down{\n"
                                            "border-color : #b1b1b1;\n"
                                            "padding-right : 10px;\n"
                                        "}")

    def setUniversity_cb_Alignment(self) : 
        textLen = len(self.university_cb.currentText())
        if textLen == 3 : self.setUniversity_cb_StyleSheet(138)
        elif textLen == 4 : self.setUniversity_cb_StyleSheet(126)



    def showPW(self) : 
        if self.PW_show_ckb.isChecked() : 
            self.PW_box_le.setEchoMode(QLineEdit.Normal)
        else : 
            self.PW_box_le.setEchoMode(QLineEdit.Password)



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



    def returnToMain_finale_notPrepared(self) : 
        self.finale_notPrepared_lb.hide()
        self.university_X_mark_lb.hide(); self.university_O_mark_lb.hide()
        self.account_X_mark_lb.hide(); self.account_O_mark_lb.hide()
        self.time_X_mark_lb.hide(); self.time_O_mark_lb.hide()
        self.subject_X_mark_lb.hide(); self.subject_O_mark_lb.hide()
        self.finale_notPrepared_bt.hide()
        self.body_frm.show()
        self.changeSCMode()



    def returnToMain_finale_inProgress(self) : 
        self.finale_inProgress_lb.hide()
        self.finale_inProgress_bt.hide()
        self.body_frm.show()
        self.finale_rb.setChecked(True)
        self.setMenu()



    def returnToMain_subjectError(self) : 
        self.subjectError_lb.hide()
        self.subjectError_bt.hide()
        self.body_frm.show()



    def returnToMain_pageError(self) : 
        self.pageError_lb.hide()
        self.pageError_bt.hide()
        self.body_frm.show()



    def returnToMain_accountError(self) : 
        self.accountError_lb.hide()
        self.accountError_bt.hide()
        self.body_frm.show()



    def returnToMain_periodError(self) : 
        self.periodError_lb.hide()
        self.periodError_bt.hide()
        self.body_frm.show()



    def changeSCMode(self) : 
        global SCMode

        if SCMode == "start" : 
            self.start_bt.hide()
            self.cancel_bt.show()
            SCMode = "cancel"

        elif SCMode == "cancel" : 
            self.cancel_bt.hide()
            self.start_bt.show()
            SCMode = "start"



    # preparationState_group
    ## << finaleUniversity_lb(1/4) >>
    def universityIsPrepared(self) : 
        self.finaleUniversity_lb.setStyleSheet("QLabel{\n"
                                                    "image : url(:/img/finaleUniversity_lb_prepared_normal.png);\n"
                                                    "border : 0px;\n"
                                                    "background-color : transparent;\n"
                                                "}\n"
                                                "QLabel:hover{\n"
                                                    "image : url(:/img/finaleUniversity_lb_prepared_hover.png);\n"
                                                "}")

    def universityIsNotPrepared(self) : 
        self.finaleUniversity_lb.setStyleSheet("QLabel{\n"
                                                    "image : url(:/img/finaleUniversity_lb_notPrepared_normal.png);\n"
                                                    "border : 0px;\n"
                                                    "background-color : transparent;\n"
                                                "}\n"
                                                "QLabel:hover{\n"
                                                    "image : url(:/img/finaleUniversity_lb_notPrepared_hover.png);\n"
                                                "}")


    ## << finaleAccount_lb (2/4) >>
    def accountIsPrepared(self) : 
        self.finaleAccount_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/finaleAccount_lb_prepared_normal.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}\n"
                                            "QLabel:hover{\n"
                                                "image : url(:/img/finaleAccount_lb_prepared_hover.png);\n"
                                            "}")

    def accountIsNotPrepared(self) : 
        self.finaleAccount_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/finaleAccount_lb_notPrepared_normal.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}\n"
                                            "QLabel:hover{\n"
                                                "image : url(:/img/finaleAccount_lb_notPrepared_hover.png);\n"
                                            "}")


    ## << finaleTime_lb (3/4) >>
    def timeIsPrepared(self) : 
        self.finaleTime_lb.setStyleSheet("QLabel{\n"
                                            "image : url(:/img/finaleTime_lb_prepared_normal.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}\n"
                                        "QLabel:hover{\n"
                                            "image : url(:/img/finaleTime_lb_prepared_hover.png);\n"
                                        "}")

    def timeIsNotPrepared(self) : 
        self.finaleTime_lb.setStyleSheet("QLabel{\n"
                                            "image : url(:/img/finaleTime_lb_notPrepared_normal.png);\n"
                                            "border : 0px;\n"
                                            "background-color : transparent;\n"
                                        "}\n"
                                        "QLabel:hover{\n"
                                            "image : url(:/img/finaleTime_lb_notPrepared_hover.png);\n"
                                        "}")


    # << finaleSubject_lb (4/4) >>
    def subjectIsPrepared(self) : 
        self.finaleSubject_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/finaleSubject_lb_prepared_normal.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}\n"
                                            "QLabel:hover{\n"
                                                "image : url(:/img/finaleSubject_lb_prepared_hover.png);\n"
                                            "}")

    def subjectIsNotPrepared(self) : 
        self.finaleSubject_lb.setStyleSheet("QLabel{\n"
                                                "image : url(:/img/finaleSubject_lb_notPrepared_normal.png);\n"
                                                "border : 0px;\n"
                                                "background-color : transparent;\n"
                                            "}\n"
                                            "QLabel:hover{\n"
                                                "image : url(:/img/finaleSubject_lb_notPrepared_hover.png);\n"
                                            "}")



    def eventFilter(self, object, event) : 
        if object == self.onestop_bt : 
            if event.type() == QEvent.HoverEnter : 
                self.onestop_img_lb.show()
                self.onestop_txt_lb.show()
            elif event.type() == QEvent.HoverLeave : 
                self.onestop_img_lb.hide()
                self.onestop_txt_lb.hide()
        
        elif object == self.finaleUniversity_lb : 
            if event.type() == QEvent.HoverEnter : 
                self.time_HM_lcd.hide(); self.time_S_lcd.hide()
                self.universityBox_lb.show()
                self.university_cb.show()
            elif event.type() == QEvent.HoverLeave : 
                self.time_HM_lcd.show(); self.time_S_lcd.show()
                self.universityBox_lb.hide()
                self.university_cb.hide()
        
        elif object == self.finaleAccount_lb : 
            if event.type() == QEvent.HoverEnter : 
                self.time_HM_lcd.hide(); self.time_S_lcd.hide()
                self.accountBox_lb.show()
                self.ID_box_le.show()
                self.PW_box_le.show()
            elif event.type() == QEvent.HoverLeave : 
                self.time_HM_lcd.show(); self.time_S_lcd.show()
                self.accountBox_lb.hide()
                self.ID_box_le.hide()
                self.PW_box_le.hide()

        elif object == self.finaleTime_lb : 
            if event.type() == QEvent.HoverEnter : 
                self.time_HM_lcd.hide(); self.time_S_lcd.hide()
                self.timeBox_lb.show()
                self.hour_box_le.show()
                self.min_box_le.show()
            elif event.type() == QEvent.HoverLeave : 
                self.time_HM_lcd.show(); self.time_S_lcd.show()
                self.timeBox_lb.hide()
                self.hour_box_le.hide()
                self.min_box_le.hide()

        elif object == self.finaleSubject_lb : 
            if event.type() == QEvent.HoverEnter : 
                self.time_HM_lcd.hide(); self.time_S_lcd.hide()
                self.subjectBox_tw.show()
            elif event.type() == QEvent.HoverLeave : 
                self.time_HM_lcd.show(); self.time_S_lcd.show()
                self.subjectBox_tw.hide()

        return False





if __name__ == "__main__" : 
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    sys.exit(app.exec_())
