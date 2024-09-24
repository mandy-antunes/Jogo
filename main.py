'''
Jogo do Adivinhe o Número
2024.07.30
Mandy Antunes
'''
# Objetivo: desenvolver um jogo, onde o usuário deverá tentar adivinhar um número secreto sorteado pelo PC

# Módulos e Bibliotecas
from random import randint # importa uma biblioteca para o programa

# Variáveis
msg = '' #variavel para adicionar uma mensagem
numeroSecreto = 0 #usado para sorteio do numero


# Constantes
CAR = "+" #caracter usado para desenhar a estrutura do jogo
TDT = 40 #tamanho da tela a ser desenhada
MAR = 2 #margem de dois caracteres
INI = 1 #indica onde inicia a contagem dos numeros sorteados
FIM = 100 #indica onde para a contagem dos numeros sorteados
TVS = 3 #numero de tentativas de jogada

# Listas
listaMsgs = [] #variavel para listaMsgs

# Funções
# função para mostrar um linha de caracteres
def mostraLinha():
  print(CAR*TDT) #imprime os caracteres para desenhar o inicio do jogo

# função para mostrar um texto centralizado entre um número de caracteres
def msgCentro(msg):
  print(f"{CAR} {msg:^{TDT-MAR-MAR}} {CAR}") #imprime a mensagem no inicio do texto

# função para mostrar um cabeçalho com texto entre as linhas
def cabecalho(listaMsgs):
  mostraLinha() #chama e imprime a função mostraLinha
  for msg in listaMsgs: #enquanto tiver msg em listaMsgs
    msgCentro(msg) #a msgCentro vai conter a mensagem da listaMsgs
  mostraLinha() #chama e imprime a função mostraLinha

#função para sortear numero secreto
def sorteiaNum():
  numeroSecreto = randint(INI,FIM) #usado para sortear o numero secreto de forma aleatoria e chamando as constantes de inicio e fim
  return numeroSecreto #usado para poder ser chamado em outras partes do código

# funcao para pegar a resposta e testar se é um numero
def pegaResposta():
  resposta = input(f"{CAR} Sua resposta: ") #pegar resposta do usuário
  while not resposta.isdigit(): #verifica se o numero digitado pelo usuario é o mesmo numero sorteado
    listaMsgs = ["Resposta Inválida!", "Tente outro Número!"] #resposta retornada quando o valor digitado pelo usuario não é correspondente com o número secreto
    cabecalho(listaMsgs) #imprime a mensagem descrita acima no mesmo formato do cabeçalho
    resposta = input(f"{CAR} Sua resposta: ") #pega o valor digitado pelo usuario em uma nova tentativa
  resposta = int(resposta) #transforma a resposta em formato de numero inteiro
  return resposta #usado para poder ser chamado em outras partes do código
    
# funçao para dar dica
def dica(numeroSecreto, resposta):
  if numeroSecreto < resposta: #testa se a resposta do usuario é maior que o numero secreto
    cabecalho = ("Tente um número MENOR!") #se for maior, imprime essa dica
  else:
    cabecalho = ("Tente um número MAIOR!") #se for menor, imprime essa dica

#funçao para o jogo startar
def startGame():
  TVS = 3 #define o numero de tentativas
  numeroSecreto = sorteiaNum() #atribui a funçao sorteiaNum para o numeroSecreto
  listaMsgs = ['JOGO DO ADIVINHE O NUMERO','Powered by Profe Berssa'] #define as mensagem que estarao no cabeçalho
  cabecalho(listaMsgs) #atribui as mensagens para o cabeçalho
  playGame(TVS, numeroSecreto) #atribui a playGame as tentativas e o numero secreto como parâmetro
  
def playGame(TVS, numeroSecreto):
  for tentativas in range(TVS): #enquanto tiver tentativas em TVS
    resposta = pegaResposta() #pega a resposta do usuario
    testeAcerto = resposta == numeroSecreto #testa se é o mesmo valor do numero secreto
    if testeAcerto: #se o testeAcerto for true
      listaMsgs = ['OLOKO BIXO!!!', 'ACERTOU MEMO!!!'] #recebe esta lista de mensagem
      cabecalho(listaMsgs) #no formato do cabeçalho
      break #quebra um loop
    elif tentativas != 2: #se o teste for true e as tentativas forem diferente de 2
      listaMsgs = ['SE É RUIM D+', 'NÃO É ASSIM CRIATURA!'] #recebe esta lista de mensagem
      cabecalho(listaMsgs) #no formato do cabeçalho
      dica(numeroSecreto, resposta) #atribui o numeroSecreto e a resposta para dica
    else: #se nenhum dos testes for true
      cabecalho("MelDels que feio!!!") #imprime esta mensagem no cabeçalho
  else: #se nao tiver mais tentativas
    listaMsgs = ["FIM DE JOGO!", "O NUMERO SECRETO ERA", numeroSecreto, "PARABENS YOU LOSE!"] #recebe esta lista de mensagem
    cabecalho(listaMsgs) #no formato do cabeçalho
    listaMsgs = ["Deseja Jogar Novamente?", "[0 - NÃO]", "[1 - SIM]"] #recebe esta lista de mensagem para continuar jogando ou nao 
    cabecalho(listaMsgs) #no formato do cabeçalho
    resposta = pegaResposta() #pega a resposta do usuario
    if resposta == 1: #testa se a resposta for 1
      startGame() #se for, começa o jogo novamente
    else: #se nao for
      listaMsgs = ["FOI BOM JOGAR COM VOCÊ!", "ATÉ A PROXIMA"] #recebe esta lista de mensagem
      cabecalho(listaMsgs) #e atribui ao cabeçalho
      
# Programa Principal
startGame() #começa o jogo