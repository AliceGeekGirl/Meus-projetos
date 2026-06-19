"""
Sistema de Atendimento de Hospital
Estruturas usadas
• Fila comum → atendimento normal OK
• Fila prioritária → idosos/emergência OK
• Pilha → histórico dos últimos atendimentos OK
• Busca → localizar paciente OK
• BST → cadastro e busca de pacientes por prontuário (Árvore Binária) OK
Extras interessantes
• Simulação de tempo de espera
• Atendimento automático OK
• Menu interativo OK

"""
#Importa a classe deque do módulo collections 
from collections import deque

#Importa o módulo heapq, usado para criar filas de prioridade 
import heapq

#Importa o módulo time para trabalhar com pausas e simulações de tempo cronometrado
import time

#Modelo para representar cada paciente e seus atributos no sistema
class Paciente:

    #Método que constroí o molde com os atributos do objeto
    def __init__(self, cpf, nome_paciente, idade, gravidade):

        self.cpf= cpf #Armazena o CPF do paciente

        self.nome_paciente = nome_paciente #Armazena o nome do paciente recebido como parâmetro

        self.idade = idade #Armazena a idade do paciente recebida como parâmetro

        self.gravidade = gravidade #Armazena o nível de risco/urgência recebido como parâmetro

#Molde (modelo) da Fila Comum
class FilaComum:

    #Método que constroí o molde
    def __init__(self):

        #Inicializa uma fila vazia usando o deque
        self.fila_comum = deque()

    #Método para registrar a chamada do paciente
    def registrar_chamada(self, paciente):

        self.fila_comum.append(paciente) #Adiciona o objeto paciente ao final da fila comum 

    #Método para chamar o próximo paciente
    def chamar_proximo(self):

        #Verifica se o atributo que guarda a fila aponta para None
        if self.fila_comum is None:

            #Lança uma exceção de índice caso a condição acima seja verdadeira
            raise IndexError("Fila vazia")

        #Remove e retorna o primeiro elemento (paciente) da fila comum
        return self.fila_comum.popleft()

#Molde da Fila Prioritária baseada em Heap (Árvore binária de prioridades)
class FilaPrioritaria:

    #Método que constroí o molde com os atributos
    def __init__(self):

        self.fila_prioritaria = [] #Inicializa uma lista vazia que será gerenciada pelo heapq

        self.ordem_chegada = 0 #Contador numérico para registrar a ordem de chegada e desempatar prioridades iguais

    #Método para registrar a chamada do paciente prioritário
    def registrar_chamada(self, paciente):

        self.ordem_chegada += 1 #Incrementa o contador de chegada a cada novo paciente registrado

        #Agrupa gravidade, ordem de chegada e o objeto do paciente em uma estrutura de tupla
        pacientes_embrulhado = (paciente.gravidade, self.ordem_chegada, paciente)

        #Insere a tupla dentro da lista organizando-a como um Min-Heap estruturado
        heapq.heappush(self.fila_prioritaria, pacientes_embrulhado)

    #Método para chamar o próximo paciente prioritário
    def chamar_proximo(self):
        
        #Verifica se a lista da fila prioritária aponta para None
        if self.fila_prioritaria is None:
            
            #Lança uma exceção indicando que não há ninguém para chamar
            raise IndexError("Fila vazia")

        #Remove e retorna o menor elemento (maior prioridade) da árvore Min-Heap
        return heapq.heappop(self.fila_prioritaria)

#Define a classe Prontuario que gerencia o histórico de atendimento de um cliente específico.
class Prontuario:

  #Método construtor que inicializa o prontuário recebendo o paciente como argumento
  def __init__(self, paciente):

    #Inicializa o prontuário para um cliente, criando um histórico vazio.
    self.Historico = deque()  #Usamos deque para um histórico eficiente 

    #Define a propriedade paciente do objeto para guardar os dados/nome do paciente associado
    self.paciente = paciente #Armazena o nome do cliente

  #Método para inserir um novo relato médico e classificação no prontuário
  def add_Historico(self, descricao, nivel_gravidade):

    #Cria uma estrutura de dicionário mapeando a descrição do sintoma e a gravidade em letras maiúsculas
    #Cria um dicionário para o registro
    registro = {"descricao": descricao, "gravidade": nivel_gravidade.upper()} #Adiciona um novo registro ao histórico do paciente.

    #Insere o dicionário recém-criado na última posição do deque do histórico
    self.Historico.append(registro) #Adiciona o registro ao final do deque

    #Imprime no terminal a confirmação dos dados adicionados ao prontuário
    print("Prontuario adicionado para o paciente", self.paciente, "\nDescrição:", descricao, "\nGravidade:", nivel_gravidade)

  #Método utilitário para checar a existência de registros salvos
  def vazio(self):
    
    #Avalia se o tamanho do histórico é igual a zero, retornando True (vazio) ou False (com registros)
    return len(self.Historico) == 0 

  #Método simulando uma Pilha (LIFO) para descartar a última informação registrada
  def remove_Historico(self):

    #Desvia o fluxo caso o método utilitário identifique que não há dados no histórico
    if self.vazio():
      print("Não tem registro para remover")

      #Retorna uma ausência de valor para encerrar a execução do método prematuramente
      return None

    #Caso possua dados no histórico, entra no bloco alternativo
    else:

      #Elimina o último elemento posicionado na extremidade direita do deque
      self.Historico.pop() #Remove o último registro adicionado ao histórico.

  #Método para espiar o registro inserido por último na estrutura
  def Historico_atual(self):

    #Desvia o fluxo caso a lista de prontuários esteja vazia
    if self.vazio():
      print("Não tem prontuarios registrados")

      #Retorna uma ausência de valor indicando falha na recuperação do dado
      return None

    #Caso possua dados, executa a busca do último elemento
    else:

      #Acessa e retorna o elemento no índice -1 (posição final) do deque de histórico
      return self.Historico[-1] #Retorna o registro mais recente do histórico.

  #Método responsável por varrer e imprimir toda a linha do tempo médica do paciente
  def exibir_prontuario_completo(self):

    #Condicional que barra o processamento caso a fila de históricos esteja vazia
    if self.vazio():
      print("Não tem prontuarios registrados")
      
      return None #Aborta o restante da função retornando um valor nulo

    #Imprime uma barra divisória estilizada com o nome do paciente em letras maiúsculas
    print(f"\n=== HISTÓRICO DE ATENDIMENTOS: {self.paciente.upper()} ===")

    #Loop que percorre o deque do fim para o começo (do registro mais novo ao mais antigo)
    for r in reversed(self.Historico):

        #Para limpar, nós isolamos e pegamos apenas o VALOR que está guardado em cada chave
        texto_descricao = r["descricao"] #Extrai o valor associado à chave "descricao" do dicionário atual do loop

        #Extrai o valor associado à chave "gravidade" do dicionário atual do loop
        texto_gravidade = r["gravidade"]

        #Exibe os dados formatados de forma organizada e legível no console
        print(f"-> Sintoma: {texto_descricao} | Risco: {texto_gravidade}\n")

#Cria o molde (modelo) para representar cada nó individual da árvore
class No_Arvore:

  #Método construtor que define o que cada nó carrega e seus braços de ligação
  def __init__(self, id, dados_paciente):

    self.id = id #Armazena a chave de busca (o prontuário/ID do paciente)

    self.dados_paciente = dados_paciente #Guarda o objeto com as informações do paciente

    self.esquerda = None #Inicializa o ponteiro esquerdo vazio (para IDs menores)

    self.direita = None #Inicializa o ponteiro direito vazio (para IDs maiores)

#Cria a estrutura que gerencia os nós (a Árvore Binária de Busca)
class ArvoreBinaria:

  #Método construtor que inicializa a árvore no hospital
  def __init__(self):

    self.raiz = None #Toda árvore nova começa sem nenhum paciente (raiz vazia)

  #Método responsável por inserir um paciente no galho correto de forma iterativa
  def insercao(self, id, dados):

    no = No_Arvore(id, dados) #Instancia (cria) um novo nó com o ID e os dados fornecidos

    #Condicional que verifica se o hospital ainda não tem nenhum paciente na árvore
    if self.raiz == None:

      self.raiz = no #Define o novo nó criado como a Raiz absoluta (o topo da árvore)

      #Encerra o método imediatamente, pois o trabalho principal já foi feito
      return

    #O ponteiro 'atual' começa na raiz ANTES do laço para poder descer os galhos
    atual = self.raiz

    #Abre um laço de repetição infinito para navegar pela estrutura até achar uma vaga
    while True:

      #Compara se o ID do novo paciente é menor do que o ID do nó onde estamos posicionados
      if no.id < atual.id:

        #Verifica se o braço esquerdo desse nó está livre (vazio)
        if atual.esquerda is None:

          atual.esquerda = no #Encaixa o novo paciente permanentemente na vaga da esquerda

          break #Quebra o laço 'while True' finalizando a inserção com sucesso

        #Se a esquerda já estava ocupada, move o nosso ponteiro para o nó da esquerda para continuar procurando
        atual = atual.esquerda

      #Bloco alternativo executado caso o ID do novo paciente seja maior que o ID do nó atual
      elif no.id > atual.id:

        #Verifica se o braço direito desse nó está livre (vazio)
        if atual.direita is None:

          atual.direita = no #Encaixa o novo paciente permanentemente na vaga da direita

          break #Quebra o laço 'while True' finalizando a inserção com sucesso

        #Se a direita já estava ocupada, move o nosso ponteiro para o nó da direita para continuar procurando
        atual = atual.direita

  #Método responsável por varrer a árvore e localizar os dados do paciente pelo ID
  def busca(self, id_alvo):

    atual = self.raiz #Inicia o ponteiro de busca a partir do topo da árvore (raiz)

    #Executa o laço enquanto o ponteiro não atingir um galho inexistente (None)
    while atual is not None:

      #Verifica se o ID que estamos buscando é exatamente igual ao ID do nó atual
      if id_alvo == atual.id:

        #Retorna o pacote completo com os dados do paciente para quem chamou a função
        return atual.dados_paciente

      #Se não achou e o ID buscado for menor que o ID do nó atual, desvia o caminho para a esquerda
      elif id_alvo < atual.id:

        atual = atual.esquerda #Faz o ponteiro caminhar para o próximo nó do lado esquerdo

      #Se o ID buscado for maior que o ID do nó atual, desvia o caminho para a direita
      else:

        atual = atual.direita #Faz o ponteiro caminhar para o próximo nó do lado direito

    #Se o laço 'while' terminar sem entrar no 'return' de sucesso, significa que o ID não existe na árvore
    return None

fila_comum = FilaComum() #Instancia (cria) o objeto da fila para pacientes comuns

fila_prioritaria = FilaPrioritaria() #Instancia (cria) o objeto da fila para pacientes prioritários

arvore_hospital = ArvoreBinaria() #Instancia o objeto gerenciador da Árvore Binária para indexar os prontuários médicos

hospital = {} #Inicializa um dicionário vazio para associar o CPF do paciente ao seu respectivo objeto de dados

#Inicia um loop infinito para manter o menu rodando até que o usuário decida sair
while True:

  print("*--Sistema do Hospital--*\n")

  #Exibe as opções disponíveis para o usuário interagir
  print("1- Cadastrar Paciente\n2- Atender Próximo Paciente\n3- Buscar Dados do Paciente\n4- Ver Histórico do Prontuário do Paciente\n5- Ativar Atendimento Automático\n6- Sair do sistema\n")

  #Captura a escolha do usuário como uma string
  opcao = input("Escolha uma opção: ")

  #Estrutura de controle que analisa a opção digitada 
  match opcao:

    #Caso o usuário escolha a opção 1 (Cadastrar Paciente)
    case "1":

        #Exibe uma mensagem no console e captura o documento de identificação única do paciente (CPF) como texto
        cpf= input("Digite o CPF do paciente: ")

        #Exibe uma mensagem no terminal e aguarda o usuário digitar o nome do paciente.
        nome = input("Digite o nome do paciente: ")

        #Exibe uma mensagem solicitando a idade do paciente e a converte em um tipo inteiro.
        idade = int(input("Digite a idade do paciente: "))

        #Pede um número de identificação único para o Prontuário (será a chave da BST)
        id_prontuario = int(input("Digite o número de ID/Prontuário do paciente: "))

        #Exibe a tabela de triagem baseada no Protocolo de Manchester
        print("Níveis de Prioridade\n")
        print("1 - Emergência\n2 - Muito Urgente\n3 - Urgente\n4 - Pouco Urgente\n5 - Não Urgente\n")

        #Captura o nível de gravidade digitado pelo usuário e converte para número inteiro
        nivel = int(input("Qual é o nível de prioridade do paciente: "))

        #Altera o nível do paciente para 1 (Emergência) caso ele tenha 60 anos ou mais
        if idade >= 60:
            nivel = 1

        paciente = Paciente(cpf, nome, idade, nivel) #Instancia o objeto Paciente enviando os dados de nome, idade, nível e cpf definidos antes

        prontuario_paciente = Prontuario(paciente.nome_paciente) #Cria uma instância da classe Prontuario passando o nome do paciente associado

        #Salva uma estrutura de dicionário interna para o CPF contendo o objeto do paciente e o prontuário em branco
        hospital[cpf] = {"dados": paciente, "prontuario": prontuario_paciente}

        #Chama o método de inserção da árvore para cadastrar o paciente pelo número do prontuário.
        #Guardamos a pasta completa do paciente na árvore também, associada ao ID dele.
        arvore_hospital.insercao(id_prontuario, {"dados": paciente, "prontuario": prontuario_paciente})

        #Avalia se a idade é maior/igual a 60 ou se o nível de gravidade está entre 1 e 3
        if paciente.idade >= 60 or nivel <= 3:

            fila_prioritaria.registrar_chamada(paciente) #Chama o método para colocar o objeto do paciente dentro da fila de prioridade

            #Exibe a mensagem de sucesso confirmando a inserção na fila prioritária
            print(f"🏥 Paciente {paciente.nome_paciente} encaminhado para a FILA PRIORITÁRIA (Gravidade: {nivel}).\n")

        else:
          
            fila_comum.registrar_chamada(paciente) #Executa este bloco se o paciente não cumprir nenhum critério de prioridade

            #Ajuste no print para mostrar a confirmação na tela para o usuário
            print(f"🟢 Paciente {paciente.nome_paciente} encaminhado para a FILA COMUM (Atendimento Normal).\n")

    #Caso o usuário escolha a opção 2 (Atender Próximo Paciente)
    case "2":

        paciente_chamado = None #Inicializa a variável para evitar erro caso as filas estejam vazias

        #Para verificar se uma Fila de Heap tem pacientes, checamos o tamanho da lista interna (.fila_prioritaria)
        if len(fila_prioritaria.fila_prioritaria) > 0:

            tupla_paciente = fila_prioritaria.chamar_proximo() #Pega a tupla embrulhada que saiu da fila

            #Desembrulha pegando apenas o objeto Paciente que está na terceira posição (índice 2)
            paciente_chamado = tupla_paciente[2]

            print(f"⚕️ Atendendo Paciente Prioritário: {paciente_chamado.nome_paciente} (Idade: {paciente_chamado.idade})\n")

            time.sleep(20) #Simula o tempo de atendimento (médico conversando com o paciente)

        #Além disso, checamos se o deque possui elementos usando o tamanho dele (.fila_comum)
        elif len(fila_comum.fila_comum) > 0:

            #Invoca o método para remover e retornar o próximo paciente da fila comum (FIFO)
            paciente_chamado = fila_comum.chamar_proximo()

            #Exibe na tela os dados do paciente comum que está sendo atendido agora
            print(f"🩺 Atendendo Paciente Comum: {paciente_chamado.nome_paciente} (Idade: {paciente_chamado.idade})\n")

            time.sleep(10) #Simula os 10 segundos de duração da consulta médica

        #Se ambas as verificações anteriores falharem, significa que o hospital está sem nenhum paciente aguardando
        else:
            print("⚠️ Não há pacientes na fila de espera.\n")

        #Se encontramos um paciente em alguma das duas checagens acima:
        if paciente_chamado is not None:

            #Capturamos o CPF que está armazenado dentro do próprio objeto do paciente que acabou de ser chamado
            cpf_atendido = paciente_chamado.cpf

            #Usamos esse CPF para ir direto no nosso dicionário 'hospital' e puxar a pasta completa dele
            pasta_do_paciente = hospital[cpf_atendido]

            #Nós usamos o colchete ["prontuario"] para dizer ao Python: "Ignore os dados básicos (como idade/nome) por um momento. Eu quero esticar a mão especificamente na divisória que guarda a folha de histórico médico."
            prontuario_do_paciente = pasta_do_paciente["prontuario"]

            #Solicitamos via teclado os dados médicos da consulta que está acontecendo agora
            sintoma_relatado = input("Digite o sintoma/diagnóstico médico para o prontuário: ")

            #Chamamos o método da classe Prontuario que dá o '.append()' no histórico (Pilha do Paciente)
            prontuario_do_paciente.add_Historico(sintoma_relatado, str(paciente_chamado.gravidade))

            print("📝 Prontuário atualizado no histórico individual com sucesso!\n")

    #Caso o usuário escolha a opção 3 (Buscar Dados do Paciente)
    case "3":

      #Solicita ao usuário o número de CPF do paciente que deseja encontrar no banco de dados
      alvo = input("Digite o CPF do paciente que está buscando: ")

      #Verifica se a chave do CPF informado existe indexada dentro do dicionário do hospital
      if alvo in hospital:

         #Vai no dicionário e abre a pasta do CPF digitado.
         #Entra na repartição que guarda o objeto Paciente.
         #Puxa o texto do nome que está salvo dentro desse objeto
         print(f"Paciente encontrado: {hospital[alvo]['dados'].nome_paciente}\n")

      #Executa este bloco caso a chave procurada não seja encontrada no dicionário
      else:
         print("⚠️ Paciente não encontrado com este CPF.\n")

    #Caso o usuário escolha a opção 4 (Ver Histórico do Prontuário)
    case "4":

        #O usuário digita o número do Prontuário/ID para acessar a ficha clínica
        id_historico = int(input("Digite o ID/Prontuário do paciente para ver o histórico: "))

        #Faz a pesquisa navegando de forma iterativa (com while) pelos nós da Árvore Binária
        resultado_historico = arvore_hospital.busca(id_historico)

        #Se o paciente for localizado em algum dos galhos da árvore:
        if resultado_historico is not None:

            #Resgata o objeto do Prontuario individual que estava guardado dentro daquele nó
            prontuario_do_paciente = resultado_historico["prontuario"]

            #Executa o método da pilha (reversed) para ler os sintomas do mais recente ao mais antigo
            prontuario_do_paciente.exibir_prontuario_completo()

        #Se a árvore foi varrida até o fim e o ID não foi encontrado
        else:
          print("⚠️ Não foi possível exibir o histórico. ID de Prontuário inexistente na árvore.\n")

    #Caso o usuário ative o sistema de atendimento automático
    case "5":
      
      #Executa o laço contínuo enquanto houver pacientes aguardando em qualquer uma das duas estruturas
      while len(fila_prioritaria.fila_prioritaria) + len(fila_comum.fila_comum) > 0:
        
        paciente_chamado = None #Inicializa a variável para evitar erro caso as filas estejam vazias

        #Para verificar se uma Fila de Heap tem pacientes, checamos o tamanho da lista interna (.fila_prioritaria)
        if len(fila_prioritaria.fila_prioritaria) > 0:

            #Pega a tupla embrulhada que saiu da fila
            tupla_paciente = fila_prioritaria.chamar_proximo()

            #Desembrulha pegando apenas o objeto Paciente que está na terceira posição (índice 2)
            paciente_chamado = tupla_paciente[2]

            #Exibe os dados do paciente prioritário na tela para o painel atualizar
            print(f"⚕️ [AUTOMÁTICO] Atendendo Paciente Prioritário: {paciente_chamado.nome_paciente} (Idade: {paciente_chamado.idade})\n")

            time.sleep(20) #Simula o tempo de atendimento (médico conversando com o paciente)

        #Além disso, checamos se o deque possui elementos usando o tamanho dele (.fila_comum)
        elif len(fila_comum.fila_comum) > 0:

            #Invoca o método para remover e retornar o próximo paciente da fila comum (FIFO)
            paciente_chamado = fila_comum.chamar_proximo()

            #Exibe os dados do paciente comum na tela para o painel atualizar
            print(f"🩺 [AUTOMÁTICO] Atendendo Paciente Comum: {paciente_chamado.nome_paciente} (Idade: {paciente_chamado.idade})\n")

            time.sleep(10) #Simula os 10 segundos de duração da consulta médica

        #Se ambas as verificações anteriores falharem, significa que o hospital está sem nenhum paciente aguardando
        else:
          print("⚠️ Não há pacientes na fila de espera.\n")

        #Se encontramos um paciente em alguma das duas checagens acima:
        if paciente_chamado is not None:

            #Capturamos o CPF que está armazenado dentro do próprio objeto do paciente que acabou de ser chamado
            cpf_atendido = paciente_chamado.cpf

            #Usamos esse CPF para ir direto no nosso dicionário 'hospital' e puxar a pasta completa dele
            pasta_do_paciente = hospital[cpf_atendido]

            #Nós usamos o colchete ["prontuario"] para dizer ao Python: "Ignore os dados básicos (como idade/nome) por um momento. Eu quero esticar a mão especificamente na divisória que guarda a folha de histórico médico."
            prontuario_do_paciente = pasta_do_paciente["prontuario"]

            #Solicitamos via teclado os dados médicos da consulta que está acontecendo agora
            sintoma_relatado = "Atendido automaticamente via Mutirão Hospitalar"

            #Chamamos o método da classe Prontuario que dá o '.append()' no histórico (Pilha do Paciente)
            prontuario_do_paciente.add_Historico(sintoma_relatado, str(paciente_chamado.gravidade))

            print("📝 Prontuário atualizado no histórico individual com sucesso!\n")

      #Mensagem exibida fora do laço 'while', indicando que todas as filas foram zeradas com sucesso
      print("🏥 [SISTEMA] Todas as filas foram esvaziadas. Mutirão de atendimento concluído!\n")

    #Caso o usuário deseja sair do sistema
    case "6":
      print("Saindo do sistema...\n") 
      
      break #Quebra o loop 'while True', finalizando o programa

    #Caso seja nenhuma das opções acima
    case _:
      print("Opção inválida! Por favor, digite um número de 1 a 6")