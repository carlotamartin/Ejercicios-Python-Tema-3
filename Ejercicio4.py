ganados = int(input("Escribe el número de partidos ganados: "))
print(" ")
perdidos = int(input("Escribe el número de partidos perdidos: "))
print(" ")
empatados = int(input("Escribe el número de partidos empatados: "))
print(" ")
puntuacion_total = (ganados*3)+(perdidos*1)+(empatados*0)
print("La puntuación total es: "+str(puntuacion_total))