correctas = int(input("Escribe el número de respuestas correctas: "))
print(" ")
incorrectas = int(input("Escribe el número de respuestas incorrectas: "))
print(" ")
en_blanco = int(input("Escribe el número de respuestas en blanco: "))
print(" ")
puntuacion_total = (correctas*3)+(incorrectas*-1)+(en_blanco*0)
print("La puntuación total es: "+str(puntuacion_total))