import random

#Creamos un numero aleatorio
num_aleatorio = random.randint(1,15)

num_adivinado = 0
intentos =0


while(num_adivinado != num_aleatorio):
    num_adivinado = int(input("Adivina un numero entre el 1 y el 15: "))
    intentos +=1
    if(num_adivinado<num_aleatorio):
        print ("El numero es mayor")
    else:
        print ("El numero es menor")

print ("Has acertado el numero " + str(num_aleatorio) + " en el intento "+ str(intentos))
