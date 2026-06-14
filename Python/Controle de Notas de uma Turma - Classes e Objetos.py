"""
2- Controle de Notas de uma Turma
Crie uma classe Aluno com:
• nome
• lista de notas
Crie métodos para:
• adicionar nota
• calcular média
• verificar se o aluno está aprovado (média ≥ 7)
Depois mostre qual aluno teve a maior média da turma.
"""

#Molde (modelo) do Aluno
class Aluno:

    #Método construtor: Inicializa os atributos do objeto quando ele é criado
    def __init__(self, nome):

        #Armazena o nome do aluno
        self.nome = nome

        #Inicializa uma lista vazia para guardar as notas      
        self.notas = []       

    #Método para adicionar uma nova nota à lista do aluno
    def adicionar(self, nota):

        #Insere a nota no final da lista
        self.notas.append(nota)  
        return self.notas

    #Método para calcular e retornar a média aritmética das notas
    def calcular_media(self):
        
        #Soma todas as notas da lista e divide pela quantidade total de notas
        self.media = sum(self.notas) / len(self.notas)
        return self.media

    #Método para verificar a situação acadêmica do aluno com base na média
    def status(self):

        #Nota: Para este método funcionar perfeitamente, 'calcular_media()' precisa ter sido chamado pelo menos uma vez antes.
        if self.media >= 7:
            return "Aprovado"
        elif self.media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"

    #Método especial que define como o objeto será representado em formato de texto (string)
    def __str__(self):
        return f"{self.nome}"


# --- Criação e manipulação dos objetos (Instanciação) ---

#Criando o objeto para a aluna Ana e adicionando suas notas
a1 = Aluno("Ana")
a1.adicionar(8)
a1.adicionar(7)

#Criando o objeto para o aluno Carlos e adicionando suas notas
a2 = Aluno("Carlos")
a2.adicionar(9)
a2.adicionar(10)

#Agrupando todos os objetos do tipo Aluno em uma lista para a turma
alunos = [a1, a2]


#--- Encontrando o aluno com a maior média ---

#A função max() percorre a lista 'alunos'.
#argumento 'key=lambda a: a.calcular_media()' diz ao Python que ele não deve comparar os objetos Aluno diretamente (o que causaria um erro), mas sim executar o método calcular_media() para cada aluno 'a' e usar esse resultado numérico na comparação.
melhor = max(alunos, key=lambda a: a.calcular_media())

#Exibe o nome do aluno que possui a maior média calculada
print(f"Maior média: {melhor.nome}")
        
