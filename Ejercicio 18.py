#Ejercicio 18
a=int(input("Por favor, ingrese el primer número entero "))
b=int(input("Por favor, ingrese el segundo número entero "))
c=int(input("Por favor, ingrese el tercer número entero "))
if (a<b) and (a<c):
    print (a)
    if (b<c):
        print (b)
        print (c)
        if c<b:
            print (c)
            print (b)
        if b==c:
            print (b,c)
          
if (b<a) and (b<c):
    print (b)
    if (a<c):
        print (a)
        print (c)
    if c<a:
        print (c)
        print (a)
    if a==c:
        print (a,c)

if (c<a) and (c<b):
    print (c)
    if (a<b):
        print (a)
        print (b)
    if b<a:
        print (b)
        print (a)
    else:
        print (a,b)

if a==b and b==c and a==c:
    print (a,b,c)