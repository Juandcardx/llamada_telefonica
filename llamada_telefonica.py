# programa para determinar la cantidad total a pagar de una llamada

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("_ _ _ _ _ _ _ $ llamada _ _ _ _ _ _ _ _") 
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

duracion = int(input("digite minutos llamada"))


 #code 
if (duracion < 3):
    print("_ _ _ _ llamada = 300$_ _ _ _ _ _")
else:
    rta = (duracion - 3)
    total = (rta * 50) + 300
    print("el costo de la llamada es: " + str (total) + "$") 
    print("_ _ _ _ _resultado _ _ _ _ _ _ _ _ _")
