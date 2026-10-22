import numpy as np
# Nicole Robles NC 0120
#Ejemplo de numpy  Numerical Python
print("---Espaciado Linealmente en array-0120---")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print("---Matriz Identidad en 2D array-0120---")
matrix=np.eye(3)
print(matrix)
print("---Genera numeros al azar(Aleatorios) en 2D array-0120---")
numale=np.random.random((3,4)) # genera 12 numeros aleatorios
print(numale)
print("---Genera 9 numeros aleatorios entre 0 y 1---")
numale=np.random.random((3,3)) # genera 12 numeros aleatorios
print(numale)
# como generar numero 9 aleatorios comprendidos entre 1 y 20 
# con numpy en un arreglo de 3 por 3
print("---Genera 9 numeros aleatorios entre 0 y 20---")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)
print("Nicole Robles NC 0120")