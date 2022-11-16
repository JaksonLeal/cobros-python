#DEV 1/NOV/2022 JAKSON LEAL

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from datetime import datetime
import util.Recordatorio as r

#Crear formato de fecha
now = datetime.now()
months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
day = str(now.day)
month = str(months[now.month -1])
year = str(now.year)

def enviarCorreo(correoDestino, correoCopia, correoOrigen, contra, numWhatsapp, name, direccion, txtValor, deuda):

    msg = MIMEMultipart()

    message = r.mensaje(numWhatsapp, name, correoDestino, direccion, txtValor, deuda)

    #Estructura del correo
    password = contra
    msg['From'] = correoOrigen
    msg['To'] = correoDestino
    msg['Cc'] = correoCopia
    msg['Subject'] = "SOLICITUD DE PAGO %s" % (now.date()) #Asunto del correo
    tocc = correoCopia.split(",") + [correoDestino]
    
    #Agregar el cuerpo del mensaje
    msg.attach(MIMEText(message, 'plain'))

    #instanciar servidor
    server = smtplib.SMTP('correo.supergiroscasanare.co: 587')
    
    server.starttls()
    
    #Login
    server.login(msg['From'], password)
    
    #Enviar mensaje via servidor.
    server.sendmail(msg['From'], tocc, msg.as_string())
    
    server.quit()
    
    print ("Envio de Correo exitoso a %s" % (msg['To']))
