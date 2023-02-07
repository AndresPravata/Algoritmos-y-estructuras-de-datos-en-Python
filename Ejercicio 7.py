#Ejercicio 7
import math
a=int(input("Por favor, ingrese el primer número "))
b=int(input("Por favor, ingrese el segundo número "))
print("5 x ",a, " + 10 x ",b, " = ",5*a+10*b)
print(b, "^ 2 = ", b**2)
n=int(input("Por favor, ingrese otro número "))
c=n
print("(2 * ",n," - 1) / (2 * ",n," + 1) = ", round ((2*n-1)/(2*n+1),2))
n=math.sqrt(n)
print (c," ^ 1/2 = ",round (n,2))
x=int(input("Por favor, ingrese un primer número "))
y=int(input("Por favor, ingrese un segundo número "))
print("2 x ",x, " - ",y, " = ",2*x-y)
print("( ",x," - ",y,") / ( ",x," + ",y,") = ", round (((x-y)/(x+y)),2))