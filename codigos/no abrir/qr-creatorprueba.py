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

    def select(self):
        sql="SELECT no_cuenta,nombre,paterno FROM alummno"

        try:
            self.cursor.execute(sql)
            users=self.cursor.fetchall()
            

            for user in users:
                no_cu=user[0]
                nom=[user[1],user[2]]
                nombre=' '.join(nom)
                # Datos del alumno en un diccionario
                alumno = {
                    'id': no_cu,
                    'nombre': nombre
                }

                # Crear el contenido del código QR
                contenido = str(alumno)

                # Crear un objeto QRCode
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )

                # Agregar los datos al código QR
                qr.add_data(contenido)
                qr.make(fit=True)

                # Crear una imagen del código QR
                img = qr.make_image(fill_color="blue", back_color="white")

                # Guardar la imagen del código QR en un archivo
                img.save(f"codigo_qr_{alumno['nombre']}.png")
        except Exception as e:
            tk.messagebox.showerror(title="Error", message="Alumno ya está dado de alta")
            raise
    def close(self):
        self.connection.close()

databas=Database()
databas.select()
#5B666C
#C6DCE7