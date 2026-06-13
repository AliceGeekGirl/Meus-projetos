"""
1- Sistema de Biblioteca
Uma biblioteca precisa controlar empréstimos.
Crie uma classe Livro com:
• título
• autor
• disponível (True ou False)
Crie métodos para:
• emprestar livro
• devolver livro
• mostrar status do livro

"""

#Molde(modelo) do Sistema de Biblioteca
class Livro:

    #Método(Função) que constroí os atributos do objeto
    def __init__(self, titulo, autor):

        #Os atributos são atribuídos à variáveis
        self.titulo= titulo
        self.autor= autor

        #Define que, por padrão, todo livro novo começa disponível
        self.disponivel= True
        
    #Método(Função) para o empréstimo
    def emprestar(self):

        #Se o valor de 'self.disponivel' for verdadeiro
        if self.disponivel:

            #'self.disponivel' atribui o False
            self.disponivel = False

            #Imprime o resultado
            print(f"O livro {self.titulo} do autor(a) {self.autor} foi emprestado")
            
        #Senão
        else:
            
            #Imprime o resultado
            print(f"O livro {self.titulo} do autor(a) {self.autor} está indisponível")
            
    #Método(Função) para devolver
    def devolver(self):

        #Se 'self.disponivel' for igual a False
        if self.disponivel == False:

             #'self.disponivel' atribui o True
             self.disponivel = True

             #Imprime o resultado
             print(f"O livro {self.titulo} do autor(a) {self.autor} foi devolvido")
             
    #Método(Função) para mostrar status        
    def status(self):

        #Se 'self.disponivel' for igual a True
        if self.disponivel == True:
            print("Disponível")

        #Senão
        else:
            print("Emprestado")

#Instacia(cria) o objeto e chama a classe 'Livro' com os valores(atributos)
livro_1= Livro("Orgulho e Preconceito", "Jane Austen")

#Objeto chama os métodos
livro_1.status()
livro_1.emprestar()
livro_1.status()
livro_1.devolver()
livro_1.status()

