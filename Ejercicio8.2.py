import random

#Creamos un numero aleatorio
num_aleatorio = random.randint(1,300)

#Inicializamos el numero que introduciremos por teclado a 0 para que empiece a funcionar el buble
num_adivinado = 0

#Inicializamos los intentos a 0
intentos =0

#Creamos un bucle que vaya pidiendo numeros hasta que coincida con el numero aleatorio. Solos podrá acertar en 9 intentos

while(num_adivinado != num_aleatorio and intentos<9):
    num_adivinado = int(input("Adivina un numero entre el 1 y el 300: "))
    intentos +=1
    if(num_adivinado<num_aleatorio):
        print ("El numero es mayor")
    elif (num_adivinado>num_aleatorio):
        print ("El numero es menor")
    else:
        break

if (num_adivinado == num_aleatorio):
    print ("Has acertado el numero " + str(num_aleatorio) + " en el intento "+ str(intentos))
else:
    print("¡Se te han acabado los intentos!")