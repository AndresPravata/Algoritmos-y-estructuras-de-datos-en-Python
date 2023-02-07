#Ejercicio 15
palabra1=str(input("Por favor, ingrese una palabra "))
palabra2=str(input("Por favor, ingrese otra palabra "))
a=len(palabra1)
b=len(palabra2)
if a==b:
    print ("Las palabras ",palabra1," y ",palabra2," tienen la misma longitud")
if a>b:
    print ("La palabra",palabra1," tiene mayor longitud que el término ",palabra2)
if a<b:
    print ("La palabra",palabra1," tiene menor longitud que el término ",palabra2)