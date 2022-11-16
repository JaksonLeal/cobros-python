#DEV 1/NOV/2022 JAKSON LEAL
import pyautogui as pg, webbrowser as web, time as t
import pyperclip as ppc
import util.Recordatorio as r

def enviarWhatsapp(numWhatsapp, name, correoDestino, direccion, txtValor, deuda):
    
    message = r.mensaje(numWhatsapp, name, correoDestino, direccion, txtValor, deuda)

    #formatear numero
    phone_no = "+57"+str(numWhatsapp)
    parsedMessage=""

    #API de whatsapp
    web.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+parsedMessage) #abrir una ventana en el navegador
    
    t.sleep(12)
    ppc.copy(message)
    pg.hotkey('ctrl', 'v')
    t.sleep(6)
    pg.press('enter')
    t.sleep(5)
    pg.hotkey('ctrl', 'w')
    t.sleep(2)
