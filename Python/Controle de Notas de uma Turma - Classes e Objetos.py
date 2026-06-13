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

class Aluno:
    def __init__(self, nome):
        
        self.nome= nome
        self.notas= []

    def adicionar(self, nota):
        self.notas.append(nota)
        return self.notas

    def calcular_media(self):
        self.media= sum(self.notas)/len(self.notas)
        return self.media

    def status(self):
        if self.media >= 7:
            return "Aprovado"
        elif self.media >=5:
            return "Recuperação"
        else:
            return "Reprovado"

    def __str__(self):
        return (f"{self.nome}")

a1 = Aluno("Ana")
a1.adicionar(8)
a1.adicionar(7)

a2 = Aluno("Carlos")
a2.adicionar(9)
a2.adicionar(10)

alunos = [a1, a2]

#max() percorre a lista 'alunos'
#key=lambda a: define que, para cada aluno 'a', o critério de comparação é o resultado de calcular_media()
#No fim, a variável 'melhor' guarda o objeto Aluno completo que venceu essa comparação
melhor = max(alunos, key=lambda a: a.calcular_media())

print(f"Maior média: {melhor.nome}")
        
