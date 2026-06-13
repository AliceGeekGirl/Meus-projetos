"""
3- Sistema de Loja
Crie uma classe Produto com:
• nome
• preço
• quantidade em estoque
Crie métodos para:
• vender produto
• repor estoque
• mostrar valor total em estoque
valor total = preço × quantidade
"""

#Molde(modelo) do Produto
class Produto:

    #Método(Função) que constroí o molde(class) com os atributos do objeto
    def __init__(self, nome, preco, quantidade_estoque):

        #Os atributos são atribuídos à variáveis
        self.nome= nome
        self.preco= preco
        self.quantidade_estoque= quantidade_estoque

    #Método(Função) para vender com o valor
    def vender(self, qtd):
        
        #Subtrair o valor de 'self.quantidade_estoque' pela 'qtd'
        self.quantidade_estoque -= qtd

        #Imprime os resultados
        print(f"Foram {qtd} quantidades de {self.nome} vendidas")
        print(f"Atualmente o estoque de {self.nome} é {self.quantidade_estoque}")

    #Método(Função) para repor com o valor
    def repor(self, qtd):

        #Somar o valor de 'self.quantidade_estoque' pela 'qtd'
        self.quantidade_estoque += qtd

        #Imprime os resultados
        print(f"Foi reposto {qtd} quantidades de {self.nome}")
        print(f"Atualmente o estoque de {self.nome} é {self.quantidade_estoque}")

    #Método(Função) para mostrar com o valor
    def mostrar_valor(self):

        #Varíavel 'self.valor' calcula o produto de 'self.preco' com 'self.quantidade_estoque'
        self.valor= self.preco * self.quantidade_estoque

        #Imprime os resultados
        print(f"O valor total em estoque do {self.nome}: R$ {self.valor}")

#Instancia(cria) o objeto e chama a classe 'Produto' com atributos
loja= Produto("Arroz", 9.50, 15)

#Objeto chama os métodos 
loja.vender(3)
loja.repor(1)
loja.mostrar_valor()

