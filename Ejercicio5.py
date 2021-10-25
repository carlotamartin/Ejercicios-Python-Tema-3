#1 galón = 3,78541 litros

un_galon_en_litros = 3,78541
def coste_gasolina(total_galones):
    total_a_pagar= total_galones*un_galon_en_litros
    return total_a_pagar

print("El total a pagar en una gasolinara si llenas 10 galones es: "+str(coste_gasolina(10)))