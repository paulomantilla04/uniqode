import qrcode
import pymysql
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
from customtkinter import END

# Rutas a carpeta para imagenes
main_folder = os.path.dirname(__file__)
image_folder = os.path.join(main_folder, "images")
font_folder = os.path.join(main_folder, "fonts")


#Fecha actual

fecha_actual = str(date.today())


# Modo color
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")




class MainWindow:
    def __init__(self): 
        self.root = ctk.CTk()
        self.root.title("Uniqode")
        self.root.iconbitmap(os.path.join(image_folder, "uniqode_icon.ico"))
        self.root.geometry("800x500")
        self.root.config(bg="#A7DEE4")
        self.root.resizable(False, False)
        

        # Cargar la fuente descargada
        font_path = os.path.join(font_folder, "Koulen-Regular.ttf")
        custom_font = ctk.CTkFont(family="Koulen", size=40)

        

        # Cargar Imagen
        file_path = os.path.dirname(os.path.realpath(__file__))
        logo_image = ctk.CTkImage(Image.open(file_path + "/images/logo.png"), size=(80,80))

        #Image label
        logo_label = ctk.CTkLabel(self.root, image=logo_image, text="", fg_color="#A7DEE4")
        logo_label.place(x=270, y=150)

        # label
        main_text = ctk.CTkLabel(
            self.root, 
            text="N I Q O D E", 
            font=custom_font,
            bg_color="#A7DEE4",
            text_color="#000000")
        
        main_text.place(x=345, y=160)

        # Botones
        # --- Cargar imagenes botones
        button_one_image = ctk.CTkImage(Image.open(file_path+"/images/scan-code.png"), size=(24,24))
        button_two_image = ctk.CTkImage(Image.open(file_path+"/images/check-bit.png"), size=(24,24))
        button_three_image = ctk.CTkImage(Image.open(file_path+"/images/add-icon.png"), size=(24,24))


        # --- Crear botones
        button_one = ctk.CTkButton(self.root,
                                    text="",
                                    corner_radius=80,
                                    width=30,
                                    height=40,
                                    image=button_one_image,
                                    fg_color="#5034C4",
                                    hover_color="#3C2697",
                                    bg_color="#a7dee4",
                                    cursor="hand2",
                                    command=self.abrirEscaner)
        
        button_one.place(x=276, y=254)

        button_two = ctk.CTkButton(self.root,
                                    text="",
                                    corner_radius=40,
                                    width=30,
                                    height=40,
                                    image=button_two_image,
                                    fg_color="#5034c4",
                                    hover_color="#3C2697",
                                    bg_color="#a7dee4",
                                    cursor="hand2",
                                    command=self.abrirBitacora)
        
        button_two.place(x=364, y=254)

        button_three = ctk.CTkButton(self.root,
                                    text="",
                                    corner_radius=40,
                                    width=30,
                                    height=40,
                                    image=button_three_image,
                                    fg_color="#5034c4",
                                    hover_color="#3c3697",
                                    bg_color="#a7dee4",
                                    cursor="hand2",
                                    command=self.abrirQR)
        
        button_three.place(x=452, y=254)


        self.root.mainloop()

    def abrirEscaner(self):
        self.root.destroy()
        escaner = EscanearCodigo()
        
    def abrirBitacora(self):
        self.root.destroy()
        bitacora = ChecarBitacoras()

    def abrirQR(self):
        self.root.destroy()
        qrs = CrearQR()
        



class EscanearCodigo():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Uniqode - Escanear Codigo QR")
        self.root.iconbitmap(os.path.join(image_folder, "uniqode_icon.ico"))
        self.root.geometry("800x500")
        self.root.config(bg="#A7DEE4")
        self.root.resizable(False, False)


        # Cargar la fuente descargada
        font_path = os.path.join(font_folder, "Koulen-Regular.ttf")
        custom_font = ctk.CTkFont(family="Koulen", size=22)

        # Botones
        # --- Cargar imagenes botones
        file_path = os.path.dirname(os.path.realpath(__file__))
        button_settings_image = ctk.CTkImage(Image.open(file_path+"/images/settings.png"), size=(24,24))
        button_back_image = ctk.CTkImage(Image.open(file_path+"/images/back-icon.png"), size=(24,24))
        logo = ctk.CTkImage(Image.open(file_path+"/images/logo.png"), size=(65,65))
        qr_image = ctk.CTkImage(Image.open(file_path+"/images/qr-draw.png"), size=(200,200))

        # --- Crear botones
        button_back = ctk.CTkButton(self.root,
                                    text="",
                                    corner_radius=80,
                                    width=30,
                                    height=40,
                                    image=button_back_image,
                                    fg_color="#5034C4",
                                    hover_color="#3C2697",
                                    bg_color="#a7dee4",
                                    cursor="hand2",
                                    command=self.regresar
                                    )
        
        button_back.place(x=20, y=80)

        button_settings = ctk.CTkButton(self.root,
                                        text="",
                                        corner_radius=80,
                                        width=30,
                                        height=40,
                                        image=button_settings_image,
                                        fg_color="#5034c4",
                                        hover_color="#3c2697",
                                        bg_color="#a7dee4",
                                        cursor="hand2",
                                        command=self.configuracion)
        
        button_settings.place(x=20, y=130)

        button_scan = ctk.CTkButton(self.root,
                                    text="ESCANEAR",
                                    font=custom_font,
                                    corner_radius=10,
                                    height=50,
                                    width=100,
                                    fg_color="#5034c4",
                                    hover_color="#3c2697",
                                    bg_color="#a7dee4",
                                    cursor="hand2",
                                    anchor="center",
                                    compound="top",
                                    command=self.escanear)
        
        button_scan.place(x=350, y=300)

        logo_label = ctk.CTkLabel(self.root,
                                    text="",
                                    image=logo,
                                    fg_color="#a7dee4")
        
        logo_label.place(x=725, y=30)

        image_label = ctk.CTkLabel(self.root,
                                    image=qr_image,
                                    text="",
                                    fg_color="#a7dee4")
        
        image_label.pack(padx=40, pady=70)






        
        self.root.mainloop()

    def regresar(self):
        self.root.destroy()
        main = MainWindow()
    
    def configuracion(self):
        global aula_seleccionada  # Accede a la variable global
        global materia_seleccionada


        self.ventana = ctk.CTkToplevel(self.root)
        my_font = ctk.CTkFont(family="Arial", size=14, weight="bold")
        self.ventana.title("Opciones")
        self.ventana.geometry("300x200")
        self.ventana.iconbitmap(os.path.join(image_folder, "uniqode_icon.ico"))
        self.ventana.config(bg="#A7DEE4")
        self.ventana.resizable(False, False)

        # RADIO BUTTONS para elegir aula
        radiobutton_var = ctk.StringVar(value="")

        radiobutton_1 = ctk.CTkRadioButton(master=self.ventana, variable=radiobutton_var, value="LSIE", text="LSIE", bg_color="#A7DEE4", text_color="#000000", font=my_font, fg_color="#5034c4", hover_color="#3c2697")
        radiobutton_1.place(x=20, y=10)

        radiobutton_2 = ctk.CTkRadioButton(master=self.ventana, variable=radiobutton_var, value="LAW", text="LAW", font=my_font, bg_color="#A7DEE4", text_color="#000000", fg_color="#5034c4", hover_color="#3c2697")
        radiobutton_2.place(x=20, y=50)

        radiobutton_3 = ctk.CTkRadioButton(master=self.ventana, variable=radiobutton_var, value="FSW", text="FSW", font=my_font, bg_color="#A7DEE4", text_color="#000000", fg_color="#5034c4", hover_color="#3c2697")
        radiobutton_3.place(x=20, y=90)

        radiobutton_4 = ctk.CTkRadioButton(master=self.ventana, variable=radiobutton_var, value="LAI", text="LAI", font=my_font, bg_color="#A7DEE4", text_color="#000000", fg_color="#5034c4", hover_color="#3c2697")
        radiobutton_4.place(x=20, y=130)

        
        # OPTION MENU para elegir materias

        def handle_subject(choice):
            global materia_seleccionada
            materia_seleccionada = choice

        materias = ["Autom. y Comp.", "Leng. de Prog.", "POO", "CD", "Est. y Prob."]
        optionmenu_materias_var = ctk.StringVar(value="Seleccionar Materia")

        optionmenu_materias = ctk.CTkOptionMenu(master=self.ventana, variable=optionmenu_materias_var, values=materias, command=handle_subject, bg_color="#A7DEE4", fg_color="#5034c4", button_color="#5034c4", button_hover_color="#3c2697")
        optionmenu_materias.place(x=120, y=10)



        # Maneja el evento de selección y almacena el valor en la variable global
        def handle_radiobutton():
            global aula_seleccionada
            aula_seleccionada = radiobutton_var.get()

            
        radiobutton_1.configure(command=handle_radiobutton)
        radiobutton_2.configure(command=handle_radiobutton)
        radiobutton_3.configure(command=handle_radiobutton)
        radiobutton_4.configure(command=handle_radiobutton)


    
    def escanear(self):

        cap = cv2.VideoCapture(0)
        printed = False
        error_printed = False

        global nombre_alumno
        global id_alumno
        global nombre


        
        while True:
            ret, frame = cap.read()
            decoded_objects = decode(frame)
            qr_valido_encontrado = False


            for obj in decoded_objects:
                data = obj.data.decode('utf-8')

                if "id" in data and "nombre" in data:
                    try:
                        data_diccionario = ast.literal_eval(data)
                        qr_valido_encontrado = True
                    except (ValueError, SyntaxError):
                        if not error_printed:
                            tk.messagebox.showerror(title="Error", message="El código QR no tiene el formato adecuado")
                            error_printed = True
                
                else:
                    if not error_printed:
                        tk.messagebox.showerror(title="Error", message=f"El código QR no tiene el formato adecuado: {data}")
                        error_printed = True
                
                # Guardamos el nombre y ID en variables globales
                points = obj.polygon
                
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    points = hull
                
                for j in range(4):
                    cv2.line(frame, tuple(points[j]), tuple(points[(j+1) % 4]), (0, 255, 0), 3)
            

                nombre = data_diccionario["nombre"] # -- Paulo Mantilla
                palabras = nombre.split() # ['Paulo', 'Mantilla']
                n = palabras[0]
                ap = palabras[-1][0]
                nombre_alumno = f'{n.capitalize()} {ap.capitalize()}.' # -- Paulo M.

                id_alumno = data_diccionario["id"]


            if qr_valido_encontrado and not printed:
                tk.messagebox.showinfo(title="Éxito", message=f'Escaneo exitoso!')
                printed = True
                database.insert()

                
            cv2.imshow('Uniqode - Lectura QR', frame)

            if (cv2.waitKey(1) & 0xFF == ord('q')) or printed or error_printed:
                break
        cap.release()
        cv2.destroyAllWindows()
        


class ChecarBitacoras():

    def __init__(self):
        
        self.root = ctk.CTk()
        self.root.title("Uniqode - Checar Bitacora")
        self.root.iconbitmap(os.path.join(image_folder, "uniqode_icon.ico"))
        self.root.geometry("900x600")
        self.root.config(bg="#A7DEE4")
        self.root.resizable(False, False)
        

        # Botones
        # --- Cargar imagenes botones
        file_path = os.path.dirname(os.path.realpath(__file__))
        button_back_image = ctk.CTkImage(Image.open(file_path+"/images/back-icon.png"), size=(24,24))
        logo = ctk.CTkImage(Image.open(file_path+"/images/logo.png"), size=(65,65))

        # --- Crear botones
        button_back = ctk.CTkButton(self.root,
                                    text="",
                                    corner_radius=80,
                                    width=30,
                                    height=40,
                                    image=button_back_image,
                                    fg_color="#5034C4",
                                    hover_color="#3C2697",
                                    bg_color="#a7dee4",
                                    cursor="hand2",
                                    command=self.regresar
                                    )
        
        button_back.place(x=20, y=80)

        logo_label = ctk.CTkLabel(self.root,
                                    text="",
                                    image=logo,
                                    fg_color="#a7dee4")
        
        logo_label.place(x=825, y=30)
        # TABLA


        scrollable_frame = ctk.CTkScrollableFrame(self.root, width=600, height=400,corner_radius=40, bg_color="#a7dee4", orientation="vertical")
        scrollable_frame.place(x=130, y=70)

        headers = [["Nombre", "ID", "Aula", "Materia", "Fecha"]]

        self.table = CTkTable(scrollable_frame, values=headers)


        self.table.configure(width=600, height=400)
        self.table.pack()

        # ESTA LINEA GENERA ERROR SI LA TABLA ESTA VACIA, si no se llena, vale popo
        database.select()

        for user in users:
            self.table.add_row([user[0], user[1],user[2], user[3],user[4]])

        

        self.root.mainloop()

    def regresar(self):
        self.root.destroy()
        main = MainWindow()
class CrearQR():
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Uniqode - Crear QR")
        self.root.iconbitmap(os.path.join(image_folder, "uniqode_icon.ico"))
        self.root.geometry("800x500")
        self.root.config(bg="#A7DEE4")
        self.root.resizable(False, False)

        # Botones
        # --- Cargar imagenes botones
        file_path = os.path.dirname(os.path.realpath(__file__))
        button_back_image = ctk.CTkImage(Image.open(file_path+"/images/back-icon.png"), size=(24,24))
        logo = ctk.CTkImage(Image.open(file_path+"/images/logo.png"), size=(65,65))

        # Cargar la fuente descargada
        #font_path = os.path.join(font_folder, "Koulen-Regular.ttf")
        custom_font = ctk.CTkFont(family="Koulen", size=16)
        custom_font2= ctk.CTkFont(family="Arial", size=12,weight="bold")

        button_back = ctk.CTkButton(self.root,
                                    text="",
                                    corner_radius=80,
                                    width=30,
                                    height=40,
                                    image=button_back_image,
                                    fg_color="#5034C4",
                                    hover_color="#3C2697",
                                    bg_color="#a7dee4",
                                    cursor="hand2",
                                    command=self.regresar
                                    )
        
        button_back.place(x=20, y=80)

        logo_label = ctk.CTkLabel(self.root,
                                    text="",
                                    image=logo,
                                    fg_color="#a7dee4")
        
        logo_label.place(x=725, y=30)

        # ========== LABELS Y ENTRYS ==========

        # ==== ID
        global name_entry,app_entry,apm_entry

        id_label = ctk.CTkLabel(self.root, text="No. Cuenta", font=custom_font, text_color="#000000", fg_color="#a7dee4")
        id_label.place(x=320, y=85)

        id_entry = ctk.CTkEntry(self.root, font=custom_font2, fg_color="#ffffff", text_color="#000000", border_color="#ffffff", width=200, bg_color="#a7dee4")
        id_entry.place(x=315, y=110)

        # === NOMBRE

        name_label = ctk.CTkLabel(self.root, text="Nombre", font=custom_font, text_color="#000000", fg_color="#a7dee4")
        name_label.place(x=320, y=150)

        name_entry = ctk.CTkEntry(self.root, font=custom_font2, fg_color="#ffffff", text_color="#000000", border_color="#ffffff", width=200, bg_color="#a7dee4")
        name_entry.place(x=315, y=175)

        # === AP PATERNO

        app_label = ctk.CTkLabel(self.root, text="Apellido Paterno", font=custom_font, text_color="#000000", fg_color="#a7dee4")
        app_label.place(x=320, y=215)

        app_entry = ctk.CTkEntry(self.root, font=custom_font2, fg_color="#ffffff", text_color="#000000", border_color="#ffffff", width=200, bg_color="#a7dee4")
        app_entry.place(x=315, y=240 )

        # === AP MATERNO

        apm_label = ctk.CTkLabel(self.root, text="Apellido Materno", font=custom_font, text_color="#000000", fg_color="#a7dee4")
        apm_label.place(x=320, y=280)

        apm_entry = ctk.CTkEntry(self.root, font=custom_font2, fg_color="#ffffff", text_color="#000000", border_color="#ffffff", width=200, bg_color="#a7dee4")
        apm_entry.place(x=315, y=305)

        # === FUNCION GENERAR Y BOTON

        def generar():
            if id_entry.get()=='' or name_entry.get()=='' or app_entry.get()=='' or apm_entry.get()=='':
                tk.messagebox.showerror(title="Error", message="Verifique que todos los campos estén llenos")
            else:
                global id_ent
                id_ent=int(id_entry.get())
                database.insertAl()
                tk.messagebox.showinfo(title="Éxito", message=f'Registro exitoso')
                database.selectAl()
                us=users[0]
                id_entry.delete(0, END)
                name_entry.delete(0, END)
                app_entry.delete(0, END)
                apm_entry.delete(0, END)

                if id_ent==us[0]:
                    no_cu=us[0]
                    nom=[us[1],us[2]]
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
                    img = qr.make_image(fill_color="black", back_color="white")

                    # Guardar la imagen del código QR en un archivo
                    img.save(f"codigo_qr_{alumno['nombre']}.png")
                    

        button_generate = ctk.CTkButton(self.root,
                                    text="GENERAR",
                                    font=custom_font,
                                    corner_radius=10,
                                    height=50,
                                    width=150,
                                    fg_color="#5034c4",
                                    hover_color="#3c2697",
                                    bg_color="#a7dee4",
                                    cursor="hand2",
                                    anchor="center",
                                    compound="top",
                                    command=generar)
        
        button_generate.place(x=340, y=370)

        self.root.mainloop()

    def regresar(self):
        self.root.destroy()
        main = MainWindow()


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='paulo123',
            db='uniqode'
        )

        self.cursor = self.connection.cursor()
        print("Conexion con exito")
    def insert(self):
        
        sql="INSERT INTO bitacora(nombre_al,nocuenta_al,aula,materia,fecha) VALUES ('{}','{}','{}','{}','{}')".format(nombre_alumno,id_alumno,aula_seleccionada,materia_seleccionada,fecha_actual)

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as error:
            tk.messagebox.showerror(title="Error", message="No se pudo completar la consulta")
            raise
    
    def insertAl(self):
        sql="INSERT INTO alumno(no_cuenta,nombre,paterno,materno) VALUES ({},'{}','{}','{}')".format(id_ent,name_entry.get(),app_entry.get(),apm_entry.get())

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            tk.messagebox.showerror(title="Error", message="El error pudo darse por lo siguiente:\n-El No. Cuenta ya está dado de alta\n-No. Cuenta no valida")
            raise

    def select(self):
        global users
        sql="SELECT nombre_al,nocuenta_al,aula,materia,fecha FROM bitacora"

        try:
            self.cursor.execute(sql)
            users=self.cursor.fetchall()
        except Exception as e:
            raise
    def selectAl(self):
        global users
        sql="SELECT no_cuenta,nombre,paterno FROM alumno WHERE no_cuenta={}".format(id_ent)

        try:
            self.cursor.execute(sql)
            users=self.cursor.fetchall()
        except Exception as e:
            raise

    def close(self):
        self.connection.close()
        print('Conexion terminada')

database = Database()
