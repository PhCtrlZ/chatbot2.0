import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from QtGui import Ui_MainWindow
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from datetime import date
from datetime import datetime
import pyautogui
import subprocess,json,time
import requests
import ctypes   
import winshell
from colorama import Fore, Back, Style
import socket
from tkinter import messagebox
import sys
class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        #start
        #self.uic.startbutton.clicked.connect(self.shows)
    #def shows(self):
        #self.uic.Screen.setText('Tool đã được khởi động')
        self.uic.english.clicked.connect(self.english)
        self.uic.vietnam.clicked.connect(self.vietnam)
        self.uic.start.clicked.connect(self.start)
        self.uic.stop.clicked.connect(self.stop)
    def english(self):
        self.uic.label_1.setText('Username facebook')
        self.uic.label_2.setText('Password facebook')
        self.uic.label_3.setText('Set timer')
        self.uic.label_4.setText('Text')
        self.uic.label_5.setText('ID facebook')
        self.uic.label_6.setText('Table profile')
        self.uic.profile.setText('Convert language English succesfully!!!')
    def vietnam(self):
        self.uic.label_1.setText('Tài khoản fb')
        self.uic.label_2.setText('Mật khẩu fb')
        self.uic.label_3.setText('Cài đặt giờ')
        self.uic.label_4.setText('Lời nhắn')
        self.uic.label_5.setText('ID facebook')
        self.uic.label_6.setText('Table profile')
        self.uic.profile.setText('Đã chuyển qua ngôn ngữ tiếng việt')
    def start(self):
        messagebox.showinfo("Thông Báo","Setting success!!!")
        copy=self.uic.user.toPlainText()
        copy1=self.uic.password.toPlainText()
        copy2=self.uic.time.toPlainText()
        copy3=self.uic.id.toPlainText()
        copy4=self.uic.text.toPlainText()
        path = 'sent.vbs'
        if os.path.isfile(path):
            os.remove(path)
        path_w = 'sent.vbs'
        d=copy
        #input("nhập tài khoản facebook:")
        e=copy1
        #input("nhập mật khẩu facebook:")
        u=copy4
        #input("nhập tin nhắn vào đây(lưu ý ko viết in hoa):")
        c=copy2
        #input("nhập thời gian ví dụ(05-30-2022 06:35:00:AM):")
        n=copy3
        #input("nhập ID facebook bạn muốn nhắn ví dụ(100073313124329):")
        if d==" ":
            messagebox.showerror("Thông báo","Không được để trống ô tài khoản")
        if e==" ":
            messagebox.showerror("Thông báo","Không được để trống ô mật khẩu")
        if u==" ":
            messagebox.showerror("Thông báo","Không được để trống ô tin nhắn")
        if c==" ":
            messagebox.showerror("Thông báo","Không được để trống ô thời gian")
        if n==" ":
            messagebox.showerror("Thông báo","Không được để trống ô ID fb")
        LOGIN_URL = 'https://www.facebook.com/messages/t/'+n
        s="""Set WshShell = WScript.CreateObject("WScript.Shell")\nstrName = wshShell.ExpandEnvironmentStrings( "%USERNAME%" )\n"""""
        with open(path_w, mode='a') as f:
            f.write(s)
        for i in u:
            if i==" ":
                s="""WScript.sleep 200
        Wshshell.sendkeys" " \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ê":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ee" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="q":
                s="""WScript.sleep 200
        Wshshell.sendkeys"q" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="a":
                s="""WScript.sleep 200
        Wshshell.sendkeys"a" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ă":
                s="""WScript.sleep 200
        Wshshell.sendkeys"aw" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="â":
                s="""WScript.sleep 200
        Wshshell.sendkeys"aa" \n"""""   
                with open(path_w, mode='a') as f:
                    f.write(s)   
            if i=="b":
                s="""WScript.sleep 200
        Wshshell.sendkeys"b" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="c":
                s="""WScript.sleep 200
        Wshshell.sendkeys"c" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="d":
                s="""WScript.sleep 200
        Wshshell.sendkeys"d" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="đ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"đ" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="e":
                s="""WScript.sleep 200
        Wshshell.sendkeys"e" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="g":
                s="""WScript.sleep 200
        Wshshell.sendkeys"g" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="h":
                s="""WScript.sleep 200
        Wshshell.sendkeys"h" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="i":
                s="""WScript.sleep 200
        Wshshell.sendkeys"i" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="k":
                s="""WScript.sleep 200
        Wshshell.sendkeys"k" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="l":
                s="""WScript.sleep 200
        Wshshell.sendkeys"l" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="m":
                s="""WScript.sleep 200
        Wshshell.sendkeys"m" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="n":
                s="""WScript.sleep 200
        Wshshell.sendkeys"n" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ô":
                s="""WScript.sleep 200
        Wshshell.sendkeys"oo" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="o":
                s="""WScript.sleep 200
        Wshshell.sendkeys"o" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ơ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ow" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="p":
                s="""WScript.sleep 200
        Wshshell.sendkeys"p" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="q":
                s="""WScript.sleep 200
        Wshshell.sendkeys"q" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="r":
                s="""WScript.sleep 200
        Wshshell.sendkeys"r" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="s":
                s="""WScript.sleep 200
        Wshshell.sendkeys"s" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="t":
                s="""WScript.sleep 200
        Wshshell.sendkeys"t" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="u":
                s="""WScript.sleep 200
        Wshshell.sendkeys"u" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="v":
                s="""WScript.sleep 200
        Wshshell.sendkeys"v" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="x":
                s="""WScript.sleep 200
        Wshshell.sendkeys"x" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="y":
                s="""WScript.sleep 200
        Wshshell.sendkeys"y" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ò":
                s="""WScript.sleep 200
        Wshshell.sendkeys"of" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="á":
                s="""WScript.sleep 200
        Wshshell.sendkeys"as" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ả":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ar" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ã":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ax" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ạ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"aj" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="è":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ef" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="é":
                s="""WScript.sleep 200
        Wshshell.sendkeys"es" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ẻ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"er" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ẽ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ex" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ẹ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ẹ" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ỳ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"yf" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ý":
                s="""WScript.sleep 200
        Wshshell.sendkeys"ys" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ỷ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"yr" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ỹ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"yx" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ỵ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"yj" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
            if i=="ổ":
                s="""WScript.sleep 200
        Wshshell.sendkeys"oor" \n"""""
                with open(path_w, mode='a') as f:
                    f.write(s)
        s="""WScript.sleep 200
        Wshshell.sendkeys"{enter}" """""
        with open(path_w, mode='a') as f:
            f.write(s)

        while True:
            now= datetime.now()
            a=now.strftime("%m-%d-%Y %T:%p")
            b=str(a)
            if b==c:
                print("khởi động chế độ tự động nhắn")
                print("===== Admin Login Facebook =====")
                class FacebookLogin():
                    def __init__(self, email, password, browser='Chrome'):
                        # Store credentials for login
                        self.email = email
                        self.password = password
                        if browser == 'Chrome':
                            # Use chrome
                            self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
                        self.driver.get(LOGIN_URL)
                        time.sleep(1) # Wait for some time to load
                 
                 

                    def login(self):
                        email_element = self.driver.find_element_by_id('email')
                        email_element.send_keys(self.email) # Give keyboard input
                 
                        password_element = self.driver.find_element_by_id('pass')
                        password_element.send_keys(self.password) # Give password as input too
                 
                        login_button = self.driver.find_element_by_id('loginbutton')
                        login_button.click() # Send mouse click

                        time.sleep(15)
                        for _ in range(2):
                            pyautogui.click(542,680)

                        os.startfile('sent.vbs')
                        time.sleep(2) # Wait for 2 seconds for the page to show up
                        exit()
                if __name__ == '__main__':
                    # Enter your login credentials here
                    #fb_login = FacebookLogin(email='100074258102022', password='0914220047', browser='Chrome')
                    fb_login = FacebookLogin(email=d, password=e, browser='Chrome')
                    fb_login.login()
                    print("[+] Login successfully")

    def show(self):
        self.main_win.show()
    def stop(self):
        messagebox.showerror("Thông báo","The tool have been stoping!")
        sys.exit()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
