import re
import mysql.connector as msc
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from register import Register
from main_page import Login_page


class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.__reg = re.compile(
            r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
        )
        self.setWindowTitle("Log in")
        self.setFixedSize(1550, 900)

        self.user_info_ls = []

        self.setWindowIcon(QIcon("D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\train.ico"))
        
        white_window = QWidget(self)
        shadow_effect = QGraphicsDropShadowEffect(self)
        shadow_effect.setBlurRadius(20)
        shadow_effect.setColor(QColor(0, 0, 0, 50))
        shadow_effect.setOffset(0, 0)
        white_window.setGeometry(490, 80, 550, 750)
        white_window.setStyleSheet("background-color: white; border-radius: 8px;")
        white_window.setGraphicsEffect(shadow_effect)

        # pictures
        self.main_photo = QLabel(self)
        self.photo_1 = QPixmap(
            "D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\a.png"
        )
        self.main_photo.setPixmap(self.photo_1)
        self.main_photo.setGeometry(500, 115, 500, 75)

        self.photo2 = QLabel(self)
        self.photo_2 = QPixmap(
            "D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\photo2.png"
        )
        self.photo2.setPixmap(self.photo_2)
        self.photo2.setGeometry(505, 220, 530, 80)

        self.line_edit_box_settings = """
                            border-radius: 10px;
                            font-size: 25px;
                            border: 1.1px solid #8c8c8c;
                            padding: 14px;
                            padding-left: 70px;
                            background-color: #f0f2f7;
                            """
        self.lbl_not_user = QLabel("", self)

        # buttons
        self.change_phone_to_email = QPushButton("TELEFON", self)
        self.change_phone_to_email.setGeometry(515, 340, 255, 57)
        self.change_phone_to_email.setStyleSheet(
            """
        color: white; 
        background-color: #01C3A7; 
        border-top-left-radius: 10px;
        border-top-right-radius: 0px;
        border-bottom-left-radius: 10px;
        border-bottom-right-radius: 0px;
        border-radius: 10px;
        padding: 15px;
        font: bold;
        font-size: 30px;
        """
        )

        self.change_phone_to_number = QPushButton("POCHTA", self)
        self.change_phone_to_number.setGeometry(760, 340, 255, 57)
        self.change_phone_to_number.setStyleSheet(
            """
        color: #01C3A7; 
        background-color: #F0F2F7; 
        border-top-left-radius: 0px;
        border-top-right-radius: 10px;
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 10px;
        padding: 15px;
        font: bold;
        font-size: 30px;
        """
        )

        # number settings
        self.user_phone_num = QLineEdit(self)
        self.user_phone_num.setGeometry(512, 420, 500, 60)
        self.user_phone_num.setPlaceholderText("+998 (00) 000-00-00")
        self.user_phone_num.setStyleSheet(self.line_edit_box_settings)

        # password settings
        self.password = QLineEdit(self)
        self.password.setGeometry(512, 490, 500, 60)
        self.password.setPlaceholderText("Parolni kiriting")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet(self.line_edit_box_settings)

        # icons for line edit
        self.phone_ico1 = QLabel(self)
        self.phone_ico_1 = QPixmap(
            "D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\phone.png"
        )
        self.phone_ico1.setPixmap(self.phone_ico_1)
        self.phone_ico1.setGeometry(535, 439, 25, 25)

        self.locker_ico1 = QLabel(self)
        self.locker_ico_1 = QPixmap(
            "D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\icn-password.png"
        )
        self.locker_ico1.setPixmap(self.locker_ico_1)
        self.locker_ico1.setGeometry(535, 510, 25, 25)

        # label
        railway_info_lbl = QLabel("© 2015 - 2024 AO O'zbekiston Temir Yo'llari", self)
        railway_info_lbl.setStyleSheet(
            "color: #9fa5b0; font: Calibri; font-size: 19px;"
        )
        railway_info_lbl.setGeometry(595, 790, 370, 20)

        self.sign_up_button = QPushButton("Kirish", self)
        self.sign_up_button.setStyleSheet(
            """
                                          QPushButton:pressed {color: white; background-color: #02b097; border-radius: 10px; font-size: 27px; font: bold;}
                                          QPushButton {color: white; background-color: #01c3a7; border-radius: 10px; font-size: 27px; font: bold;}
                                          """
        )
        self.sign_up_button.setGeometry(512, 600, 500, 60)

        self.not_already_user = QPushButton("Ro'yxatdan o'tish", self)
        self.not_already_user.setStyleSheet(
            "color: #187CEE; border: 0px; font-size: 18px;"
        )
        self.not_already_user.setGeometry(860, 670, 150, 25)

        self.not_already_user.clicked.connect(lambda: self.register())
        self.sign_up_button.clicked.connect(lambda: self.to_login())
        self.change_phone_to_number.clicked.connect(lambda: self.change_login())
        self.change_phone_to_email.clicked.connect(lambda: self.change_login(1))

    # <--------------------------------------------------------------- METHODS --------------------------------------------------------------->
    def to_login(self):
        self.database_info_printer()
        user_number = self.user_phone_num.text()
        user_password = self.password.text()

        new_settings = """
        border-radius: 10px;
        font-size: 25px;
        border: 1.1px solid #8c8c8c;
        border-color: red;
        padding: 14px;
        padding-left: 70px;
        background-color: #f0f2f7;
        """

        already_user = False

        for each in self.user_info_ls:
            if user_number in each and user_password in each:
                already_user = True
                break
        if already_user:
            self.go_to_log_page()
            self.lbl_not_user.setText("")
            self.user_phone_num.setStyleSheet(self.line_edit_box_settings)
            self.password.setStyleSheet(self.line_edit_box_settings)
        else:
            self.lbl_not_user.setStyleSheet("font-size: 17px; color: red;")
            self.lbl_not_user.setGeometry(617, 562, 310, 25)
            self.lbl_not_user.setText("Xatolik! Tekshirib qaytadan urinib ko'ring.")

            self.user_phone_num.setStyleSheet(new_settings)
            self.password.setStyleSheet(new_settings)

    def change_login(self, value=0):
        if value != 1:
            self.user_phone_num.setPlaceholderText(
                "Elektron pochta manzilingizni kiriting"
            )
            self.change_phone_to_number.setStyleSheet(
                """
            color: white; 
            background-color: #01C3A7; 
            border-top-left-radius: 0px;
            border-top-right-radius: 10px;
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 10px;
            padding: 15px;
            font: bold;
            font-size: 30px;
            """
            )
            self.change_phone_to_email.setStyleSheet(
                """
            color: #01C3A7; 
            background-color: #F0F2F7; 
            border-top-left-radius: 10px;
            border-top-right-radius: 0px;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 0px;
            padding: 15px;
            font: bold;
            font-size: 30px;
            """
            )
        else:
            self.user_phone_num.setPlaceholderText("+998 (00) 000-00-00")
            self.change_phone_to_number.setStyleSheet(
                """
            color: #01C3A7; 
            background-color: #F0F2F7; 
            border-top-left-radius: 0px;
            border-top-right-radius: 10px;
            border-bottom-left-radius: 0px;
            border-bottom-right-radius: 10px;
            padding: 15px;
            font: bold;
            font-size: 30px;
            """
            )

            self.change_phone_to_email.setStyleSheet(
                """
            color: white; 
            background-color: #01C3A7; 
            border-top-left-radius: 10px;
            border-top-right-radius: 0px;
            border-bottom-left-radius: 10px;
            border-bottom-right-radius: 0px;
            border-radius: 10px;
            padding: 15px;
            font: bold;
            font-size: 30px;
            """
            )

    def database_info_printer(self):
        con = msc.connect(
            host="localhost",
            username="root",
            password="01162024",
            database="railway_ticket",
        )
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM user_info;")
        data = cursor.fetchall()

        for each in data:
            self.user_info_ls.append(list(each))

    # opening register page
    def register(self):
        self.register = Register()
        self.close()
        self.register.show()

    # method for opening next page
    def go_to_log_page(self):
        self.register = Login_page()
        self.close()
        self.register.show()
