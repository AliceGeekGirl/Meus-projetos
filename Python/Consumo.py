"""
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

Entrada
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

Saída
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

"""

#Solicita ao usuário a distância total percorrida.
#O valor digitado é convertido de texto para um número inteiro (int) e armazenado na variável.
distancia_percorrida = int(input("Digite a distância percorrida: "))

#Solicita ao usuário o total de combustível gasto.
#O valor digitado é convertido para um número decimal (float) e armazenado na variável.
total_combustivel_gasto = float(input("Digite o total de combustível gasto: "))

#Calcula o consumo médio dividindo a distância pelo combustível gasto.
consumo = distancia_percorrida / total_combustivel_gasto

#Exibe o resultado na tela formatado.
#O ponto de formatação ":.3f" garante que o número terá exatamente 3 casas decimais.
print(f"{consumo:.3f} km/l")