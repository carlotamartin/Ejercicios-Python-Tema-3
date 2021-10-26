import random

num_aleatorio = random.randint(1,15)

num_adivinado = input("Adivina un número entre el 1 y el 15: ")
intentos =0

while(num_adivinado != num_aleatorio):
    num_adivinado = input("No has acertado. Prueba de nuevo a escribir un número entre el 1 y el 15: ")
    intentos +=1
    if(num_adivinado<num_aleatorio):
        print ("El número es mayor")
    else:
        print ("El número es mayor")
print ("Has acertado el número " + srt(num_aleatorio) + " en el intento "+ str(intentos))
