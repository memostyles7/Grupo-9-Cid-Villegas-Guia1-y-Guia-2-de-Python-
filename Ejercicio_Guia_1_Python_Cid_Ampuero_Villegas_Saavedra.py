#Ejercicio Guia 1 Python
#Integrantes: Guillermo Cid Ampuero Edgar Villegas Saavedra
import serial #se importa la libreria para realizar la comunicacion serial
from serial import Serial #desde la libreria serial se importa Serial
ser_com = serial.Serial('/dev/ttyACM0',9600) #se crea la  variable que permite establecer
                                        #la direccion serial y los baudios
while True: # se crea un while True, que genera un loop  infinito
        read_serial=ser_com.readline() #se lee linea por linea lo enviado desde el Arduino
        print(read_serial) #se muestra por pantalla los datos leidos

