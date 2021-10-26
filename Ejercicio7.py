def is_leap(year):
    leap = False
    if(((year % 4) ==0) and ((year% 100) !=0)and ((year% 400) ==0)):
        leap=True
# Write your logic here
    return leap
year = int(input("Escribe un año y comprueba si es bisiesto o no: "))
if is_leap(year)== False:
    print("No es bisiesto el año "+str(year))
else:
    print("El año "+str(year) +" si es bisiesto")

