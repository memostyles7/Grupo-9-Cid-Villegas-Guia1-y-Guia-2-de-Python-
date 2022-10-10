/*Codigo Arduino para realizar la muestra de valores por el Monitor Serial, para la  Guia 1 Python y Guia 2 Python 
Integrantes: Guillermo Cid Ampuero Edgar Villegas Saavedra*/
#include <Serial.h> //Se incluye la libreria Serial, para poder realizar la comunicacion serial
void setup() {
  Serial.begin(9600);

}
void loop(){
 int cm=0;//Se define la variable cm, que permitira almacenar la medida de la distancia captada por el Sensor Ultrasonico.
 cm = (int)distancia(3,2);/*Se utiliza la funcion definida para medir la Distancia, a la cual se le ingresa como paramatros el numero de pines a los cuales se conectaron los 
                            pines Trigger y Echo del Sensor Ultrasonico.*/
 Serial.print("Distancia:");//Se muestra por pantalla la distancia
 Serial.print(cm);//Se muestra por pantalla el valor de la distancia
 Serial.print("[cms]");//Se muestra la unidad de la distancia
 Serial.println();//Se imprime un caracter vacio para poder hacer un salto de linea
 delay(100); //Se deja un delay de 100 [ms]
 }

float distancia(int pinTrigger, int pinEcho){/*Se define la Funcion distancia que permite obtener la distancia medida por el Sensor Ultrasonico.
                                              donde sus parametros son el numero del Pin Trigger y el numero del Pin Echo*/
  pinMode(pinTrigger, OUTPUT);//Se configura el estado del pinTrigger como una Salida.
  digitalWrite(pinTrigger, HIGH); // Se activa el pinTrigger.
  delayMicroseconds(10);//La activacion del pinTrigger se realiza durante 10 usegundos.
  digitalWrite(pinTrigger, LOW);// Se desactiva el pinTrigger.
  pinMode(pinEcho, INPUT);//Se configura el estado del pinTrigger como una Entrada.
  unsigned long t= pulseIn(pinEcho, HIGH);//Se define la variable t,que permite almacenar el tiempo que estuvo activo el prinEcho.
  float cms=(0.0343*(t/2.00));//Se calcula la distancia mediante la formula mostrada y se almacena en la variable cms, considerando que la Velocidad del Sonido es 343 m/s.
  return cms; //Se returna el valor de distancia de la medicion obtenida por el Sensor Ultrasonico.
}
