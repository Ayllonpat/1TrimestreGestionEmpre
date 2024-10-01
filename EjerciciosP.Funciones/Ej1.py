#Ejercicio 1

def  area_rectangulo(base, altura):
    areaRectangulo = base * altura
    return areaRectangulo

print(area_rectangulo(15, 10))


#Ejercicio 2
import math

def area_circulo(radio):
    areaCirculo= radio * math.pi
    return areaCirculo

print(area_circulo(5))

#Ejercicio 3

def relacion(a, b):
    if(a>b):
        return 1
    if(b>a):
        return -1
    if(a==b):
        return 0

print(relacion(5,10))
print(relacion(10,5))
print(relacion(5,5))

#Ejercicio 4

def intermedio(a, b):
    suma = a + b
    div = suma/2
    return div

print(intermedio(-12, 24))

#Ejercico 5

def recortar(numero, minimo, maximo):
    if (numero<minimo):
        return minimo
    if (numero>maximo):
        return maximo
    if (numero<maximo & numero>minimo):
        return numero

print(recortar(15,0,10))

#Ejercicio 6

def separar(lista):
    pares = []
    impares= []
    if (lista % 2) == 0:
        pares.append(lista)        
    else:
        impares.append(lista)
        
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    

print(separar())