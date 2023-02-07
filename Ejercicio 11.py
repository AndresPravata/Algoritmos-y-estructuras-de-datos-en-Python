#Ejercicio 11
dolar=float(input("Por favor, ingrese el monto en dolares que desea comprar: "))
pesos=dolar*115.5
comision=pesos*0.04
total=pesos+comision
print ("La transacción será de $",pesos, "a una cotización de 115.50 al día 23 de marzo")
print ("Usted deberá abonar ", comision, "en concepto de comisión")
print ("El valor final de la transacción sera de $",total)