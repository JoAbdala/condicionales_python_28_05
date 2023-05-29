peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

if imc <= 15:
    Condicion = "Delgadez muy severa"
elif 15 <= imc <= 15.9:
    Condicion = "Delgadez severa"
elif 16 <= imc <= 18.4:
    Condicion = "Delgadez"
elif 18.5 <= imc <= 24.9:
    Condicion = "Peso Saludable"
elif 25 <= imc <= 29.9:
    Condicion = "Sobrepeso"
elif 30 <= imc <= 34.9:
    Condicion = "Obesidad moderada"
elif 35 <= imc <= 39.9:
    Condicion = "Obesidad severa"
else:
    Condicion = "Obesidad muy severa (Obesidad morbida)"

print("Su Condiciòn Fìsica es  :", Condicion)






