import qrcode

# Datos del alumno en un diccionario
alumno = {
    'id': 476585,
    'nombre': 'Hugo Benitez Neria'
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
