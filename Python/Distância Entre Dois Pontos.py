"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

Distancia = math.sqrt((math.pow(x2-x1, 2))+(math.pow(y2-y1, 2)))

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.

"""
import math

x1= float(input("Digite o número x1 no ponto P1: "))
y1= float(input("Digite o número y1 no ponto P1: "))

x2= float(input("Digite o número x2 no ponto P2: "))
y2= float(input("Digite o número y2 no ponto P2: "))

distancia= math.sqrt((math.pow(x2-x1, 2))+(math.pow(y2-y1, 2)))

print(f"O valor da distância é {distancia:.4f}")