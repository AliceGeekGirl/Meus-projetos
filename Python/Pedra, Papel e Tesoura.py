
#Importa o módulo random para podermos gerar escolhas aleatórias para o computador
import random

#Inicializa as variáveis que vão guardar os pontos do usuário e do computador
contador_usuario= 0
contador_computador= 0

print("------Jogo Pedra, Papel e Tesoura------\n")

#Inicia um loop infinito que manterá o jogo rodando até encontrar um comando 'break'
while True:

    #Solicita a opção do usuário e usa o método .capitalize() para garantir que a primeira letra seja maiúscula
    escolha_usuario= input("Escolha Pedra, Papel ou Tesoura: ").capitalize()

    #Validação rápida
    if escolha_usuario != "Pedra" and escolha_usuario != "Papel" and escolha_usuario != "Tesoura":
        print("Incorreto, escolha uma das opcões sugeridas")
        continue #Isso faz o Python voltar lá para o início do 'while True'


    #O computador escolhe aleatoriamente um dos três elementos da lista fornecida
    escolha_computador= random.choice(["Pedra", "Papel", "Tesoura"])

    #Mostra na tela o que cada um escolheu para o jogador acompanhar
    print(f"Você escolheu: {escolha_usuario} | Computador escolheu: {escolha_computador}\n")

    #Verifica se o usuário escolheu "Pedra"
    if escolha_usuario == "Pedra":

        #Se o computador escolheu ""Tesoura", o usuário ganha 
        if escolha_computador == "Tesoura":
            print("Parabéns! Você ganhou!\n")
            contador_usuario+=1 #Soma 1 ponto ao total do usuário

        #Se o computador escolheu "Papel", o usuário perde 
        elif escolha_computador == "Papel":
            print("Sinto muito, mas você perdeu\n")
            contador_computador+=1 #Soma 1 ponto ao total do computador

        #Se não for nenhum dos dois, significa que o computador também escolheu Pedra (Empate)
        else:
            print("Empatou!\n")

    #Verifica se o usuário escolheu "Papel"
    elif escolha_usuario == "Papel": 

        #Se o computador escolheu "Pedra", o usuário ganha 
        if escolha_computador == "Pedra":
            print("Parabéns! Você ganhou!\n")
            contador_usuario+=1 #Soma 1 ponto ao total do usuário

        #Se o computador escolheu "Tesoura", o usuário perde
        elif escolha_computador == "Tesoura":
            print("Sinto muito, mas você perdeu\n")
            contador_computador+=1 #Soma 1 ponto ao total do computador

        #Se não for nenhum dos dois, significa que o computador também escolheu Papel (Empate)
        else:
            print("Empatou!\n")

    #Verifica se o usuário escolheu "Tesoura"
    else:

        #Se o computador escolheu "Papel", o usuário ganha
        if escolha_computador == "Papel":
            print("Ganhou esta rodada!\n")
            contador_usuario+=1 #Soma 1 ponto ao total do usuário
        
        #Se o computador escolheu "Pedra", o usuário perde
        elif escolha_computador == "Pedra":
            print("Perdeu esta rodada\n")
            contador_computador+=1 #Soma 1 ponto ao total do computador

        #Se não for nenhum dos dois, significa que o computador também escolheu Tesoura (Empate)
        else:
            print("Empatou!\n")

    #Pergunta se o jogador quer continuar e já transforma a resposta em letras minúsculas (.lower())
    resposta= input("Deseja continuar jogando? (s/n): \n").lower()

    #Se a resposta do usuário for 'n', o comando break é acionado e saímos do loop 'while'
    if resposta == "n":
        break

print("\n=======================================")
print("*Pontução do Jogo*\n")
print("=======================================")

print(f"Você: {contador_usuario} ponto(s)")
print(f"Computador: {contador_computador} ponto(s)\n")

#Compara os placares para declarar o grande campeão do simulado
if contador_usuario > contador_computador:
    print("🏆 PARABÉNS! Você venceu o jogo! 🏆")
elif contador_computador > contador_usuario:
    print("❌ Fim de jogo! O computador venceu. ❌")
else:
    print("🤝 O jogo terminou em um empate geral! 🤝")
print("=======================================\n")

      
