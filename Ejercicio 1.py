#Ecuaciones del mru (a=0):
#x= x0 + v0t
#v= v0

def mru(velocidad, tiempo):
    distancia = velocidad*tiempo
    return distancia

print("La distancia es: ")
print (mru(8,9)) 
print ("m/s")