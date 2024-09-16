#!/usr/bin/env python



def pinum(numRectangulos, puntoMedio):
    imagen = 0
    for i in range(numRectangulos):
        imagen = 4/(1+puntoMedio**2)
    return imagen

def area(rango, numRectangulos, puntoMedio):
    valor_calculado = 0
    for i in range(numRectangulos): #Se hace un for con rango de la cantidad de rectángulos
        imagen = 4/(1+puntoMedio**2) #Imagen de cada punto medio
        valor_calculado += imagen * rango #Cálculo del área y suma de todas las áreas
        puntoMedio += rango #Avanza al siguiente punto medio

    return valor_calculado


def SumaRiemman(valorInicial, valorFinal, numRectangulos):
    rango = (valorFinal - valorInicial) / numRectangulos #Divide el área bajo el curva en una cantidad n de rectángulos y rango es el tamaño de la base de cada uno
    punto_medio = rango/2 #Iniciamos el cálculo en el primer punto medio
    valorCalculado = area(rango, numRectangulos, punto_medio) #Invoca a la función pinum con la cantidad de rectangulos y el tamaño de las bases
    print(valorCalculado)


SumaRiemman(0,1,1000)
