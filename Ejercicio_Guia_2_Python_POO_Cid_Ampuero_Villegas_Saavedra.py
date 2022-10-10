#Ejercicio Guia 2 Python
#Integrantes: Guillermo Cid Ampuero Edgar Villegas Saavedra

import serial #Se importa la libreria que permite la comunicacion Serial
from w1thermsensor import W1ThermSensor #Se importa la libreria  para utilizar el Sensor de Temperatura

class Arduino: #Se define la clase Arduino
    def __init__(self,baudios): #Se define el constructor , con el argumento baudios, que permitira
                                #ingresar la velocidad de comunicacion
        self.baudios=baudios #Se le asigna baudios a self.baudios
    def getDatos(self): #Se define el metodo getDatos, que permitira obtener los datos desde Arduino
        print(serial.Serial('/dev/ttyACM0',self.baudios).readline()) #Se muestran por pantalla los datos obtenidos desde Arduino

class sensorTemperature: #Se define la clase sensorTemperature
    def __init__(self,temperature): #Se define el constructor,con el argumento temperature, que permitira
                                # obtener la temperatura
        self.temperature=temperature #Se le asigna temperature a self.temperature

    def getTemperature(self): #Se define el metodo getTemperature, que permitira obtener la Temperatura
                                #desde el Sensor de Temperatura
        self.temperature=self.temperature.get_temperature() #Se obtiene la temperatura
        print("Temperatura: ",self.temperature) # Se muestra por pantalla el valor de la temperatura

sensor=W1ThermSensor() #Se crea la variable sensor  para almacenar la conexion con el Sensor de Temperatura
while True: #Se genera un ciclo while con la condicion True, para genera un loop infinito
    data=Arduino(9600) #Se crea el objeto data para la clase Arduino
    data.getDatos() #Se llama al metodo getDatos
    temp=sensorTemperature(sensor) #Se crea el objeto temp
    temp.getTemperature() #Se llama al metodo getTemperature

    

