from random import sample
import main
import DB
import os
import controlMainMenu

banco = DB.Banco() # Variavei que vai gerenciar o banco
numerosEscolhidos = [] # Armazana Numeros que ja foram escolhidos pelo usuario

# Verificando se há Banco de Dados.
if not os.path.exists("BancoDeDados/"):
    os.mkdir("BancoDeDados/")
    banco.NotHasDB()
    print("Novo Banco De Dados!")
else:
    if not os.path.exists("BancoDeDados/estatisticas.db"):
        banco.NotHasDB()
        print("Novo Banco De Dados!")

# Funções de Controle do programa
""" Essa função vai sortear e mostrar no programa principal 5 números aleatórios. É executa quando o usuario preciona 'Começar'.
    - static = Label que mostra os numeros Sorteados
    - status = Armazena o Label para mostrar as mensagems do programa
    - escolhidos = Lista de numeros que foram escolhidos pelo usuario
 """
def sortear(static, status, escolhidos):
    if botao.quantidadePressionada < 5: # Se o usúario nao escolher numeros o suficiente
        status.configure(text="Escolha 5 Numeros Primeiro!", foreground="red")
    else:
        numeros = sample(range(81), 5) # Sorteia 5 números de 0 a 80
        while 0 in numeros: # Retirar 0
            numeros = sample(range(81), 5)
        
        static['text'] = " ".join([str(x) for x in numeros]) # Mostra na aplicação principal

        msg = verificar(escolhidos, numeros) # Verificar quantos acertou
        status.configure(text=msg, foreground="yellow") # Mostrar mensagem de quantos número acertou.

"""Ver quantos numeros foram acertados!
    - static = Numeros escolhidos pelo usuario
    - numeros = Numeros Sorteados.
""" 
def verificar(static, numeros):
    UserNumber = [int(x) for x in static['text'].split(" ")] # Pega os inteiros dos numeros escolhidos.
    string = [x for x in UserNumber if x in numeros] # Todos os numeros acertados.
    # Salva no banco de dados. User.atual = Id do usuario, UserNumber = Numeros Escolhidos, numeros = Numeros Sorteados, len(string) = Quantidade de Numeros acertados
    banco.adicionar(User.atual, UserNumber, numeros, len(string)) 
    return f"Acertou! {len(string)} numeros!" # Retorna a quantidade Acertada.

"""Detroi a janela atual, e volta ao menu principal
    - window janela atual
"""
def logout(window):
    # Reset variaveis
    numerosEscolhidos.clear()
    botao.quantidadePressionada = 0
    # Deleta e chama o menu
    window.destroy()
    main.main()

# Classe de control de Botoes
class botao(main.Application):
    # Variavel para a quantidade de botoes pressionadas pelo usuario;
    quantidadePressionada = 0
    def __init__(self, numero, static):
        self.numero = numero+1 # Por padrao, numeros virao de 0 a 79. somamos 1 para usar o valor correto;
        self.escolhido = False # Se esse botao ja foi pressionado;
        self.control = main.Button(text=str(self.numero), width=5, command=lambda: self.press(static)) # Definição do botão;

    # Executado caso seja precionado.
    def press(self, static):
        # se ja tiver sido precionado, deve-se retirar o número e voltar o botao ao padrao;
        if self.escolhido:
            # Reset botao
            self.escolhido = False
            self.control.configure(style="TButton")
            # Retirando da lista dos selecionados e do display original
            numerosEscolhidos.remove(self.numero)
            static['text'] = ''.join(str(numerosEscolhidos).replace("[", '').replace(",", '').replace("]", ''))
            botao.quantidadePressionada -= 1
        # se nao tiver sido precionado, deve-se adicionar a lista o número do botao atual e mudar o estilo.
        else:
            # Verifica se chegou ao limite de seleção de números. 
            if botao.quantidadePressionada < 5:
                # Muda o estilo.
                self.escolhido = True
                self.control.configure(style="Press.TButton")
                # Adiciona a seleção e ao display
                numerosEscolhidos.append(self.numero)
                static['text'] = ''.join(str(numerosEscolhidos).replace("[", '').replace(",", '').replace("]", ''))
                botao.quantidadePressionada += 1

# Classe dos usuarios;
class User():
    atual = -1 # Para ser acessado por outras classes caso seja necessário. Será reescrito ao logar do usuario com o ID.
    def __init__(self, id, nome):
        # Informações do usuario
        self.nomeUsuario = nome
        self.idUsuario = id
        User.atual = self.idUsuario
