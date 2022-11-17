print("Calculadora")
print("1. Suma")
print("2. Producto entre 2 numeros")
print("3. Division")
print("4. Factorial")
print("5. Tablas de multiplicar")
print("6. Cuadrado y cubo")
print("7. Promedio")
print("8. Cantidad de números enteros e impresion de los valores máximo y mínimo")
op = int(input("Ingrese la opcion deseada: "))
       #if op == 1 :
def suma (n1, n2):
    resp= n1+n2
    return resp
#Division
if op== 1 : 
        n1=int(input("Primer numero: "))
        n2=int(input("Segundo numero: "))
        resp = print("El resultado es: ",suma(n1,n2))
elif op == 2 : #usando 2 provisionalmente, corresponde al 6
        n1=int(input("Ingresar numero: "))
        d= n1**2
        t= n1**3
        resp = print("El doble es: ",d, "y el triple es: ",t)
elif op== 3 : 
        print("Division")
        n1=int(input("Primer numero: "))
        n2=int(input("Segundo numero: "))
        resp = n1/n2
        print("El resultado es: ",resp)
 
        