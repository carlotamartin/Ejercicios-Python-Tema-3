import random

#Creamos un numero aleatorio
num_aleatorio = random.randint(1,15)

#Inicializamos el numero que introduciremos por teclado a 0 para que empiece a funcionar el buble
num_adivinado = 0

#Inicializamos los intentos a 0
intentos =0

#Creamos un bucle que vaya pidiendo numeros hasta que coincida con el numero aleatorio
while(num_adivinado != num_aleatorio):
    num_adivinado = int(input("Adivina un numero entre el 1 y el 15: "))
    intentos +=1
    if(num_adivinado<num_aleatorio):
        print ("El numero es mayor")
    else:
        print ("El numero es menor")

print ("Has acertado el numero " + str(num_aleatorio) + " en el intento "+ str(intentos))
