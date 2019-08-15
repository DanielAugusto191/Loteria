import DB
from matplotlib import pyplot as plt
import estatisticas
banco = DB.Banco()

# Gera os graficos Geral e de Usuario
def graficoDeAcertos(sql):
    result = list(banco.selecionar(sql)[0]) # Retorna o numero de acertos
    # Porcentagem
    soma = sum(result)
    percentage = [round((x/soma*100), 2) for x in result]
    
    # Configurações
    labels = ['Unos', 'Duques', 'Ternos', 'Quadras', 'Quinas']
    colors = [(0.3,1,0.95), (0.25, 0.6, 1), (0.22, 0.73, 0.9), (0.22, 0.9, 0.65), (0.25, 1, 0.5)]
    ax = plt.subplot()
    rects = ax.barh(labels, result) # Grafico em Barras Horizontal
    
    # Configurando Cada Barra
    for x in range(len(rects)):
        # Para que o label de porcentagem não ultrapasse a linha do grafico.
        if percentage[x] > 80:
            width = int(rects[x].get_width()) - 2
        else:
            width = int(rects[x].get_width())
        height = rects[x].get_y() + rects[x].get_height()/2

        # Adicionando Porcentagem e cor da barra
        ax.annotate(f"{percentage[x]}", xy=(width, height))
        rects[x].set_color(colors[x])
    
    # Labels
    ax.set_xlabel("Quantidade")
    ax.set_ylabel("Acertos")
    plt.title("Porcetagem entre acertos\n(Soma de acertos, nao inclue vezes em que nao há acertos!)")
    # Plot
    plt.show()

# Geral
# Retorna o numero mais jogado entre todos os jogadores
def mostPlayedNumber():
    sql = "select numero, max(vezesJogadas) from numeros"
    result = banco.selecionar(sql)[0] # [0] = Numero, [1] = Vezes Jogadas
    return f"{result[0]} | Sendo jogado {result[1]} vezes!"

# Retorna o numero mais sorteado entre todos os jogadores
def mostDrawNumber():
    sql = "select numero, max(vezesSorteadas) from numeros"
    result = banco.selecionar(sql)[0] # [0] = Numero, [1] = Vezes Sorteadas
    return f"{result[0]} | Sendo sorteado {result[1]} vezes!"

# Retorna a quantidade de vezes em que o numero "X" foi Jogado por todos os jogadores.
def timePlayX(x):
    sql = f"select vezesJogadas from numeros where numero= {x}"
    result = banco.selecionar(sql)[0][0]
    estatisticas.mb.showinfo("Loteria", f"O Número {x} foi jogado {result} vezes!")

# Retorna a quantidade de vezes em que o nuemro "X" foi Sorteado por todos os jogadores.
def timeDrawX(x):
    sql = f"select vezesSorteadas from numeros where numero = {x}"
    result = banco.selecionar(sql)[0][0]
    return f'O Número {x} foi sorteado {result} vezes!'

# Grafico de Acertos por todos os jogadores.
def percentageTotalHits():
    sql = "select sum(Unos), sum(Duques), sum(Ternos), sum(Quadras), sum(Quinas) from acertos;"
    graficoDeAcertos(sql)

# Usuario
# Retorna o numero mais jogado pelo jogador atual
def userMostPlayedNumber(_id):
    sql = f"select numero, max(vezesJogadas) from numeros where user_ID = {_id}"
    result = banco.selecionar(sql)[0]
    return f'{result[0]} | Sendo jogado {result[1]} vezes!'

# Retorna o numero mais sorteado pelo jogador atual
def userMostDrawNumber(_id):
    sql = f"select numero, max(vezesSorteadas) from numeros where user_ID = {_id}"
    result = banco.selecionar(sql)[0]
    return f'{result[0]} | Sendo sorteado {result[1]} vezes!'

# Retorna a quantidade de vezes em que o jogado atual jogou o numero "X"
def userTimePlayX(x, _id):
    sql = f"select vezesJogadas from numeros where numero={x} and user_ID = {_id}"
    result = banco.selecionar(sql)[0][0]
    return f'Você jogou o numero {x}, {result} vezes!'

# Retorna a quantidade de vezes em que o jogador atual sorteou o numero "X"
def userDrawPlayX(x, _id):
    sql = f"select vezesSorteadas from numeros where numero={x} and user_ID = {_id}"
    result = banco.selecionar(sql)[0][0]
    return f'Você Sorteou o numero {x}, {result} vezes!'

# Grafico de acertos do jogador atual
def userPercentageTotalHits(_id):
    sql = f"select sum(Unos), sum(Duques), sum(Ternos), sum(Quadras), sum(Quinas) from acertos where id_User = {_id};"
    graficoDeAcertos(sql)
