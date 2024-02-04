import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import mysql.connector as msc
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Login_page(QWidget):
    def __init__(self):
        QMainWindow.__init__(self)

        self.ticket_info_ls = []
        self.ticket_from = ""
        self.ticket_to = ""
        self.departure_date = ""
        self.return_date = 0

        self.setWindowIcon(
            QIcon(
                "D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\train.ico"
            )
        )
        self.qlabel_user_infp = QLabel(self)
        self.setWindowTitle("Railway.uz")
        self.setFixedSize(1550, 670)
        # self.create_table()

        self.main_photo = QLabel(self)
        self.photo_1 = QPixmap(
            "D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\main-pic.png"
        )
        self.main_photo.setPixmap(self.photo_1)
        self.main_photo.setGeometry(0, 0, 1550, 670)

        self.error_lbl = QLabel("", self)
        self.error_lbl.setStyleSheet("font-size: 17px; font: bold; color: white;")
        self.error_lbl.setGeometry(500, 620, 580, 20)

        self.label_railways = QLabel(self)
        self.label_railways.setText(
            """
O‘zbekiston
temir yo‘llari"""
        )
        self.label_railways.setGeometry(20, 100, 600, 220)
        self.label_railways.setStyleSheet(
            "font-size:60px; color: white; font: helvetica neue; font-weight: bold"
        )

        grey_label_background = QLabel(self)
        grey_label_background.setStyleSheet("background-color: rgba(69, 69, 69, .65);")
        grey_label_background.setGeometry(0, 480, 1550, 190)

        radio_button_set = """
            QRadioButton{font: 13pt Helvetica MS; color: white;}
            QRadioButton::indicator { width: 15px; height: 15px;};
            """

        self.combo_box_set = """
        QComboBox {
            font-size: 20px;
            color: #8c8d91;
            padding: 10px;
            border-radius: 8px;
            padding-left: 40px;
        }
        QComboBox QScrollBar:vertical {
            width: 10px;
            border: 0px solid transparent;
            background: #FFFFFF;

        }
        """

        label_set = "background-color: transparent; border-radius: 0px; color: white; font-size: 14px; font: bold;"
        self.dep_ret_set = "padding: 12px; font-size: 20px; color: #8c8d91; border-radius: 8px; padding-right: 45px;"

        self.centralwidget = QtWidgets.QWidget(self)
        self.rb_two_way = QtWidgets.QRadioButton("Borish - Qaytish", self.centralwidget)
        self.rb_two_way.setGeometry(QtCore.QRect(20, 540, 180, 30))
        self.rb_two_way.setStyleSheet(radio_button_set)

        self.rb_two_way.setChecked(True)

        self.rb_one_way = QtWidgets.QRadioButton("Bir tomonga", self.centralwidget)
        self.rb_one_way.setGeometry(QtCore.QRect(20, 575, 160, 30))
        self.rb_one_way.setStyleSheet(radio_button_set)

        self.msg_quit = QMessageBox(self)
        self.msg_quit.setFont(QFont("Poor Richard"))
        self.msg_quit.setIcon(QMessageBox.Question)
        self.msg_quit.setStyleSheet(
            """
        QMessageBox QPushButton {
            color: #ffffff;
            background-color: #3498db;
            border: 1px solid #2980b9;
            font-size: 20;
            padding: 5px 10px;
            border-radius: 3px;
        }
        QPushButton { min-width: 100px;
                    font-size: 20px;
                    font-weight: bold;
                    
        }
        QMessageBox QPushButton:hover {
            background-color: #4fa3df;
        }
        """
        )
        self.msg_quit.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.msg_quit.setFont(QFont("Calibri", 30))

        self.msg_info = QMessageBox(self)
        self.msg_info.setFont(QFont("Poor Richard"))
        self.msg_info.setIcon(QMessageBox.Question)
        self.msg_info.setStyleSheet(
            """
        QMessageBox QPushButton {
            color: #ffffff;
            background-color: #3498db;
            border: 1px solid #2980b9;
            font-size: 20;
            padding: 5px 10px;
            border-radius: 3px;
        }
        QPushButton { min-width: 100px;
                    font-size: 20px;
                    font-weight: bold;
                    
        }
        QMessageBox QPushButton:hover {
            background-color: #4fa3df;
        }
        """
        )
        self.msg_info.setFont(QFont("Calibri", 30))

        self.label_from_where = QLabel("Qayerdan", self)
        self.label_from_where.setStyleSheet(label_set)
        self.label_from_where.setGeometry(370, 525, 100, 30)
        self.combo_box_from_where = QComboBox(self)
        self.combo_box_from_where.setGeometry(370, 555, 200, 50)
        self.combo_box_from_where.setStyleSheet(self.combo_box_set)
        self.combo_box_from_where.addItems(
            [
                "Toshkent",
                "Samarqand",
                "Buxoro",
                "Xiva",
                "Urganch",
                "Nukus",
                "Navoiy",
                "Andijon",
                "Qarshi",
                "Jizzax",
                "Termiz",
                "Guliston",
                "Qo'qon",
                "Marg'ilon",
                "Pop",
                "Namangan",
            ]
        )
        self.combo_box_from_where.currentIndexChanged.connect(
            lambda: self.cb_index_changed()
        )

        self.label_to_where = QLabel("Qayerga", self)
        self.label_to_where.setStyleSheet(label_set)
        self.label_to_where.setGeometry(575, 525, 100, 30)
        self.combo_box_to_where = QComboBox(self)
        self.combo_box_to_where.setGeometry(575, 555, 200, 50)
        self.combo_box_to_where.setStyleSheet(self.combo_box_set)

        self.destination_ico1 = QLabel(self)
        self.dest_ico_1 = QPixmap(
            "D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\destination.png"
        )
        self.destination_ico1.setPixmap(self.dest_ico_1)
        self.destination_ico1.setGeometry(378, 568, 25, 25)

        self.destination_ico2 = QLabel(self)
        self.dest_ico_2 = QPixmap(
            "D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\destination.png"
        )
        self.destination_ico2.setPixmap(self.dest_ico_1)
        self.destination_ico2.setGeometry(583, 568, 25, 25)

        self.fly_time = QLineEdit(self)
        self.fly_time.setGeometry(800, 555, 200, 50)
        self.fly_time.setStyleSheet(self.dep_ret_set)
        self.fly_time.setPlaceholderText("31-01-2024")
        self.fky_time_lbl = QLabel("O'sha yerga", self)
        self.fky_time_lbl.setStyleSheet(label_set)
        self.fky_time_lbl.setGeometry(805, 525, 100, 30)

        self.cal_ico1 = QLabel(self)
        self.cal_ico_1 = QPixmap(
            "D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\cal.png"
        )
        self.cal_ico1.setPixmap(self.cal_ico_1)
        self.cal_ico1.setGeometry(960, 568, 25, 25)

        self.land_time = QLineEdit(self)
        self.land_time.setGeometry(1005, 555, 200, 50)
        self.land_time.setStyleSheet(self.dep_ret_set)
        self.land_time.setPlaceholderText("31-01-2024")
        self.land_time_lbl = QLabel("Orqaga", self)
        self.land_time_lbl.setStyleSheet(label_set)
        self.land_time_lbl.setGeometry(1010, 525, 100, 30)

        self.cal_ico2 = QLabel(self)
        self.cal_ico_2 = QPixmap(
            "D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\cal.png"
        )
        self.cal_ico2.setPixmap(self.cal_ico_2)
        self.cal_ico2.setGeometry(1165, 568, 25, 25)

        self.main_button_to_find_ticket = QPushButton("Bilet izlash", self)
        self.main_button_to_find_ticket.setGeometry(1250, 555, 220, 50)
        self.main_button_to_find_ticket.setStyleSheet(
            """
            QPushButton:pressed {color: white; background-color: #205dab; border-radius: 23px; font-size: 22px; font: bold;}
            QPushButton {color: white; background-color: #1463c9; border-radius: 23px; font-size: 22px; font: bold;}
            """
        )

        self.rb_two_way.toggled.connect(lambda: self.change())
        self.rb_one_way.toggled.connect(lambda: self.change(1))

        self.main_button_to_find_ticket.clicked.connect(lambda: self.find_tickets())

    def change(self, val=0):
        if val == 1:
            self.land_time.setGeometry(8000, 555, 400, 50)
            self.fly_time.setGeometry(800, 555, 400, 50)
            self.cal_ico_1 = QPixmap()
            self.cal_ico1.setPixmap(self.cal_ico_1)
            self.land_time_lbl.setText("")
        else:
            self.land_time.setGeometry(1005, 555, 200, 50)
            self.fly_time.setGeometry(800, 555, 200, 50)
            self.land_time_lbl.setText("Orqaga")
            self.new_ico_1 = QLabel(self)
            self.new_ico1 = QPixmap(
                "D:\\codes\\python_codes\\4. 5-month\\HW\\5. HW_23.01.24\\photos\\cal.png"
            )
            self.new_ico_1.setPixmap(self.new_ico1)
            self.new_ico_1.setGeometry(960, 568, 25, 25)

    def cb_index_changed(self):
        self.combo_box_to_where.clear()
        new_destination = [
            "Toshkent",
            "Samarqand",
            "Buxoro",
            "Xiva",
            "Urganch",
            "Nukus",
            "Navoiy",
            "Andijon",
            "Qarshi",
            "Jizzax",
            "Termiz",
            "Guliston",
            "Qo'qon",
            "Marg'ilon",
            "Pop",
            "Namangan",
        ]
        from_where = self.combo_box_from_where.currentText()
        if from_where in new_destination:
            rm_ind = new_destination.index(from_where)
            new_destination.pop(rm_ind)

        self.combo_box_to_where.addItems(new_destination)

    def find_tickets(self):
        self.database_info_printer()
        self.ticket_from = self.combo_box_from_where.currentText()
        self.ticket_to = self.combo_box_to_where.currentText()
        self.departure_date = self.land_time.text()
        self.return_date = self.fly_time.text()
        available_tickets = []
        combo_box_new_set = """
        QComboBox {
            font-size: 20px;
            color: #8c8d91;
            padding: 10px;
            border-radius: 8px;
            padding-left: 40px;
            border: 1px solid red;
        }
        QComboBox QScrollBar:vertical {
            width: 10px;
            border: 1px solid red;
            background: #FFFFFF;

        }"""
        dep_ret_new_set = "padding: 12px; font-size: 20px; color: #8c8d91; border-radius: 8px; padding-right: 45px; border: 1px solid red"
        isAvailable = False

        for each in self.ticket_info_ls:
            if (
                (self.ticket_from in each)
                and (self.ticket_to in each)
                and (self.departure_date in each)
                and (self.return_date in each)
                and each[-1] == 1
            ):
                isAvailable = True
                print(each)
                available_tickets.append(each)

        if not isAvailable:
            self.combo_box_from_where.setStyleSheet(combo_box_new_set)
            self.combo_box_to_where.setStyleSheet(combo_box_new_set)
            self.land_time.setStyleSheet(dep_ret_new_set)
            self.fly_time.setStyleSheet(dep_ret_new_set)
            self.error_lbl.setText(
                "Bunday bilet topilmadi. Iltimos, tekshirib qaytadan urunib ko'ring!"
            )
        else:
            self.combo_box_from_where.setStyleSheet(self.combo_box_set)
            self.combo_box_to_where.setStyleSheet(self.combo_box_set)
            self.land_time.setStyleSheet(self.dep_ret_set)
            self.fly_time.setStyleSheet(self.dep_ret_set)
            self.error_lbl.setText("")
            self.goto_order()

    def database_info_printer(self):
        con = msc.connect(
            host="localhost",
            username="root",
            password="01162024",
            database="railway_ticket",
        )
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM ticket_info;")
        data = cursor.fetchall()

        for each in data:
            self.ticket_info_ls.append(list(each))

    @staticmethod
    def create_database():
        try:
            con = msc.connect(host="localhost", user="root", password="01162024")
            cursor = con.cursor()
            sql_query = "CREATE DATABASE IF NOT EXISTS railway_ticket;"
            cursor.execute(sql_query)
            con.commit()
        finally:
            if con.is_connected():
                cursor.close()
                con.close()

    def create_table(self):
        self.create_database()
        try:
            con = msc.connect(
                host="localhost",
                user="root",
                password="01162024",
                database="railway_ticket",
            )

            cursor = con.cursor()
            sql_query = """CREATE TABLE IF NOT EXISTS ticket_info(
                id int primary key auto_increment,
                from_where varchar(50),
                where_to varchar(30),
                departure_date varchar(30),
                return_date varchar(30),
                is_available tinyint(1)
            );
            """
            cursor.execute(sql_query)
            con.commit()
        finally:
            if con.is_connected():
                cursor.close()
                con.close()
                self.insert_data()

    def insert_data(self):
        con = msc.connect(
            host="localhost",
            username="root",
            password="01162024",
            database="railway_ticket",
        )
        cursor = con.cursor()

        sql_question = """INSERT INTO ticket_info(from_where, where_to, departure_date, return_date, is_available) 
                        VALUES
                            ("Toshkent", "Samarqand", "01-02-2024", "12-02-2024", 1),
                            ("Samarqand", "Navoiy", "15-02-2024", "17-02-2024", 1),
                            ("Qarshi", "Toshkent", "20-02-2024", "22-02-2024", 1),
                            ("Jizzax", "Samarqand", "25-02-2024", "27-02-2024", 1),
                            ("Samarqand", "Navoiy", "01-03-2024", "03-03-2024", 1),
                            ("Toshkent", "Qarshi", "08-03-2024", "10-03-2024", 1),
                            ("Namangan", "Samarqand", "15-03-2024", "17-03-2024", 1),
                            ("Buxoro", "Xiva", "20-03-2024", "22-03-2024", 1),
                            ("Qarshi", "Samarqand", "25-03-2024", "27-03-2024", 1),
                            ("Nukus", "Buxoro", "30-03-2024", "01-04-2024", 1),
                            ("Toshkent", "Guliston", "05-04-2024", "07-04-2024", 1),
                            ("Samarqand", "Pop", "10-04-2024", "12-04-2024", 1),
                            ("Buxoro", "Toshkent", "15-04-2024", "17-04-2024", 1),
                            ("Toshkent", "Samarqand", "20-04-2024", "22-04-2024", 1),
                            ("Samarqand", "Toshkent", "25-04-2024", "27-04-2024", 1),
                            ("Qo'qon", "Buxoro", "30-04-2024", "02-05-2024", 1),
                            ("Toshkent", "Nukus", "05-05-2024", "07-05-2024", 1),
                            ("Buxoro", "Jizzax", "10-05-2024", "12-05-2024", 1),
                            ("Xiva", "Toshkent", "15-05-2024", "17-05-2024", 1),
                            ("Toshkent", "Qarshi", "20-05-2024", "22-05-2024", 1)"""

        cursor.execute(sql_question)
        con.commit()
        cursor.close()
        con.close()

    def goto_order(self):
        self.msg_quit.setText(
            f"""Haqiqatdan ham, {self.ticket_from} dan {self.ticket_to} ga {self.departure_date} kuni ketib, {self.return_date} kuni keladigan poyezda bilet olmoqchimisiz?"""
        )
        result = self.msg_quit.exec_()

        if result == 16384:
            con = msc.connect(
                host="localhost",
                username="root",
                password="01162024",
                database="railway_ticket",
            )
            cursor = con.cursor()

            sql_question = """UPDATE ticket_info
                            SET is_available = 0
                            WHERE from_where = %s
                            AND where_to = %s
                            AND departure_date = %s
                            AND return_date = %s;
                            """
            data = (
                self.ticket_from,
                self.ticket_to,
                self.departure_date,
                self.return_date,
            )

            cursor.execute(sql_question, data)
            con.commit()
            cursor.close()
            con.close()
            self.msg_info.setText("Bilet muvaffaqiyatli band qilindi!")
            result = self.msg_info.exec_()

