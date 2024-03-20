#comentario de una linea


#Variables: Espacio de memoria,con nombre, donde guardo valores
#Los nombres de variables deben ser cortos, descriptivos, NO TENER ESPACIOS
#EN BLANCO ni caracteres especiales,no deben empezar por un numero

#Descriptivo significa que representa la categoria del dato que quiero guardar
#En python las variables pueden contener cualquier dato de tipo primitivo
#números (enteros,reales), cadens de carcateres (string), booleanos (Tru,F)
#carascters(letras)

variable=1
variable= 'Juventud divino tesoro,te vas para no volver,cuando quiero llorar no lloro'
variable=True
variable='a'
variable=3.1415926535

#Para asignar un valor a la varibale se usa el operador=


#OPERADORES: Mecanismo para obtener un dato apartir de otros datos
#Los datos que intervienen se llaman operandos.

#Aritmeticos: + - * / 
#De comparavion: Retornan Tru or False. < > >= <= == !=
#Logica Booleana: OR AND. Retornan True o False de acuerdo a una Tabla de verdad
#Los operandos siemrpre son booleanor(True or False)


a=True 
b=False

print (a and b)

#Los operadores booleanos y de comparacion son muy utilizados al definir condiciones 

#Sentencias de control de flujo: En general un programa se ejecuta linea por linea de manera secuencial
#Se puede romper esa secuencialidad empleando un conjunto de sentencias(expresiones) que permite:
#1. Seleccinar la ejecución de un bloque de codigo 
#2.Repetir la ejecución de un bloque de código 
#3. Seleccionar entre ejecutar un bloque de codigo u otro bloque de código 
#De esa manera "ROMPER" la secuencialidad 
#Principios del paradigma de programación estructurado 

#Sentencia if. Si se cumple una condición (se evalua como True) se ejecuta un bloque de código 

print("Linea 1")
print("Linea 2")

if 5>8 or 3<7:
    print("Esto se muestra si la condición es verdadera")
    
else:
    print("Esto se muestra si la condición es falsa")
    
    
#3

entrada= int (input("Cuántos años tiene?"))

if entrada<18:
    print("Es menor de edad")
else:
    print("Ya esta grande")
    
    
#Taller crear un programa en Python que genere un numero aleatorio entre 2 y 12. Si el numero es 7 imprimir ganó si no imprimir deje el juego 