"""
Joaozinho quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem, ao utilizar um automóvel que faz 12 KM/L. Para isso, ele gostaria que você o auxiliasse através de um simples programa. Para efetuar o cálculo, deve-se fornecer o tempo gasto na viagem (em horas) e a velocidade média durante a mesma (em km/h). Assim, pode-se obter distância percorrida e, em seguida, calcular quantos litros seriam necessários. Mostre o valor com 3 casas decimais após o ponto.

Entrada
O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem (em horas) e o segundo é a velocidade média durante a mesma (em km/h).

Saída
Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

"""

#Recebe o tempo gasto na viagem (em horas) e converte para valor inteiro
tempo = int(input("Digite o tempo gasto na viagem (horas): "))

#Recebe a velocidade média (em km/h) e converte para valor inteiro
velocidade = int(input("Digite a velocidade média dessa viagem (km/h): "))

#Calcula a distância total percorrida multiplicando o tempo pela velocidade
#Fórmula: Distância = Tempo * Velocidade
distancia_percorrida = tempo * velocidade

#Calcula a quantidade de litros necessária
#Como o carro faz 12 KM por litro, dividimos a distância total por 12
quantidade_litros = distancia_percorrida / 12

#Exibe o resultado formatado com 3 casas decimais usando f-string (:.3f)
print(f"É necessário {quantidade_litros:.3f} L para realizar a viagem")