#DEV 1/NOV/2022 JAKSON LEAL

import xlrd
import mail as m
import whatsapp as w
import pyautogui as pg

archivo = 'C:/Users/RSOC1098799204/Downloads/1 - COBROS/datos_envio_cobro_SENSIBLE.xlsx'

wb = xlrd.open_workbook(archivo)
#Escoger hoja para trabajar
sheet = wb.sheet_by_index(0) 

correoCopia = "ejemplo@prueba.com"
correoOrigen = "ejemplo2@prueba2.com"
contra = "Pueba1234"

for i in range(sheet.nrows-1):

    name = sheet.cell_value(i+1, 0)
    deuda = sheet.cell_value(i+1, 1)
    txtValor = sheet.cell_value(i+1, 2)
    direccion = sheet.cell_value(i+1, 3)   
    numWhatsapp = sheet.cell_value(i+1, 4) 
    correoDestino = sheet.cell_value(i+1, 5)
    
    if(numWhatsapp != "" and correoDestino != "" and name != ""): 
        w.enviarWhatsapp(int(numWhatsapp), name, correoDestino, direccion, txtValor, deuda)
        m.enviarCorreo(correoDestino, correoCopia, correoOrigen, contra, int(numWhatsapp), name, direccion, txtValor, deuda)  
    else:
        print("vacio")
        pg.alert("faltan datos en usuario %s"%(name))

