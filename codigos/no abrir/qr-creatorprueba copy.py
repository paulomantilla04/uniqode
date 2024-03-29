import pymysql
import qrcode
import customtkinter as ctk
from customtkinter import *
import os
from PIL import Image, ImageTk
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import ast
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from CTkTable import *
from datetime import date

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            db='uniqode'
        )

        self.cursor = self.connection.cursor()
        print("Conexion con exito")

    def selectAl(self):
        id_ent=476786
        global users
        sql="SELECT no_cuenta,nombre,paterno FROM alumno WHERE no_cuenta={}".format(id_ent)

        try:
            self.cursor.execute(sql)
            users=self.cursor.fetchall()
        except Exception as e:
            raise
    
    def close(self):
        self.connection.close()

databas=Database()

databas.selectAl()
us=users[0]
print(us[0])
#5B666C
#C6DCE7