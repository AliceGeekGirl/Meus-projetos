"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:

Distancia = math.sqrt((math.pow(x2-x1, 2))+(math.pow(y2-y1, 2)))

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.

"""
#Importa a biblioteca 'math', que fornece funções matemáticas como raiz quadrada e potência
import math

#Lê as coordenadas do primeiro ponto (P1)
#O input() recebe o dado como texto (string) e o float() converte esse texto em um número decimal
x1 = float(input("Digite o número x1 no ponto P1: "))
y1 = float(input("Digite o número y1 no ponto P1: "))

#Lê as coordenadas do segundo ponto (P2) da mesma forma
x2 = float(input("Digite o número x2 no ponto P2: "))
y2 = float(input("Digite o número y2 no ponto P2: "))

#Calcula a distância euclidiana entre os dois pontos utilizando a fórmula fornecida:
#1. math.pow(base, expoente): eleva a diferença das coordenadas ao quadrado (2)
#2. As duas potências são somadas
#3. math.sqrt(valor): calcula a raiz quadrada do resultado dessa soma
distancia = math.sqrt((math.pow(x2 - x1, 2)) + (math.pow(y2 - y1, 2)))

#Exibe o resultado na tela formatado
#O :.4f dentro das chaves indica que o número flutuante (f) deve ser exibido com exatamente 4 casas decimais
print(f"O valor da distância é {distancia:.4f}")