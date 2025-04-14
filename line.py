import math
def line():
    pendiente=input("Ingrese el coeficiente A: ")
    ordenada= input("Ingrese el coeficiente B: ")
    x1=input("Ingrese el coeficiente X1: ")
    x2=input("Ingrese el coeficiente X2: ")    
    pendiente=float(pendiente)
    ordenada=float(ordenada)
    x1=float(x1)
    x2=float(x2)
    print(f"El coeficiente A de su ecuación de la recta es: {pendiente}")
    print(f"El coeficiente B de su ecuación de la recta es: {ordenada}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {x2}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {pendiente}X + {ordenada}") 
    print("")
    print("Dados los siguientes puntos:")
    y1=(pendiente*x1)+ ordenada
    y2=(pendiente*x2)+ ordenada
    p=[x1,y1]
    q=[x2,y2]

    print(f"\tP1 ({x1}, {y1})")
    print(f"\tP2 ({x2}, {y2})")
    distancia=math.dist(p, q)
    print("")
    print(f"La distancia entre ellos es: {distancia}")
