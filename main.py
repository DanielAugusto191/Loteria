#!/usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import control
import estatisticas

""" Essa classe contém todo escopo visual do programa principal. """
class Application:
    def __init__(self, window, User):
        # Tamanhos
        self.larguraDaJanela = 800
        self.alturaDaJanela = 450
        # Cores
        self.quinaCores = "#5300FF"
        self.visualCores = "#5C53FF"
        self.rodapeCores = "#6D1AEB"
        # Estilos
        # |- Estilo do Botao Generico
        self.botaoStyle = Style()
        self.botaoStyle.configure("TButton", background="#FFF", borderwidth=0)
        # |- Estilo do Botao Pressionado
        self.botaoPressStyke = Style()
        self.botaoPressStyke.configure("Press.TButton", background="green")
        self.botaoPressStyke.map("Press.TButton", background = [('active', 'green')])
        # |- Estilo do Label Genico
        self.labelStyle = Style()
        self.labelStyle.configure("TLabel", background=self.quinaCores, foreground="white")
        # |- Estilo do Label Titulo
        self.mainLabelStyle = Style()
        self.mainLabelStyle.configure("mainLabel.TLabel", font=("Arial", 24))

        # Configurações da Janela
        window.geometry(f"{self.larguraDaJanela}x{self.alturaDaJanela}")
        window.resizable(0, 0)
        window.title("Quina")
        window['background'] = self.quinaCores

        # Numeros Escolhidos - Label onde vai mostrar quais número ja foram selecionados
        self.numerosEscolhidos = Label(window, text="", font=("Arial", 20))
        self.numerosEscolhidos.grid(row=2, column=10)

        # Botões - Coloca e Posiciona 80 botoes numeros de 1 a 80, onde o usuario vai escolher quais deseja jogar.
        self.botoes = [] # Essa lista armazena os botões.
        for x in range(80):
            self.botoes.append(control.botao(x, self.numerosEscolhidos))
        for x in range(8):
            for y in range(10):
                # pass
                self.botoes[y+x*10].control.grid(row=x, column=y, padx=3, pady=12)

        # Visualizando
        # |- Titulo
        self.Title = Label(window, text="QUINA", foreground="#FFF", style="mainLabel.TLabel")
        self.Title.grid(row=0, column=10, padx=80)
        # |- Mostra o nome do usúario logado.
        self.Nick = Label (window, text=User.nomeUsuario, foreground="#FFF", font=("Arial", 18))
        self.Nick.grid(row=1, column=10)

        # Começar - Executa a função que vai gerar numeros aleatórios para o jogo e dizer quantas acertou
        self.botaoComecar = Button(window, text="Verificar", command=lambda: control.sortear(self.numerosSorteados, self.status, self.numerosEscolhidos))
        self.botaoComecar.grid(row=3, column=10)

        # Numeros Sorteados - Label onde vai mostrar quais números foram sorteados
        self.numerosSorteados = Label(window, text="", font=("Arial", 20))
        self.numerosSorteados.grid(row=4, column=10)

        # Label Status - Mensagens para o usuario, como: Quantas acertou, falta numeros a escolher, ou erros internos.
        self.status = Label(window, text="", font=("Arial", 12))
        self.status.grid(row=5, column=10)

        # Página com estatisticas
        self.estatisticas = Button(window, text="Estatisticas", command=lambda: estatisticas.chamaEstatisticas(User.idUsuario))
        self.estatisticas.grid(row=6, column=10)

        # Logout
        self.quit = Button(window, text="Sair", command=lambda: control.logout(window))
        self.quit.grid(row=7, column=10)

""" Essa classe contém todo escopo visual do Menu inicial, onde ha o cadastro e o login."""
class mainmenu:
    def __init__(self, window):
        window.title("Menu Quina")

        # Definindo Seções
        # |- Login
        self.lf_Login = LabelFrame(window, text="Login")
        self.lf_Login.grid(row=0, column=0, padx=10, pady=10, ipadx=10)
        # |- Cadastro
        self.lf_Cadastro = LabelFrame(window, text="Cadastro")
        self.lf_Cadastro.grid(row=0, column=1, padx=10, pady=10, ipadx=10)

        # Login
        # |- Nome
        self.lb_loginNome = Label(self.lf_Login, text="Nome: ")
        self.lb_loginNome.grid(row=0, column=0, padx=10, pady=15)
        self.En_loginNome = Entry(self.lf_Login)
        self.En_loginNome.grid(row=0, column=1, pady=15)
        # |- Senha
        self.lb_loginSenha = Label(self.lf_Login, text="Senha: ")
        self.lb_loginSenha.grid(row=1, column=0, pady=15)
        self.En_loginSenha= Entry(self.lf_Login, show="*")
        self.En_loginSenha.grid(row=1, column=1, pady=15)
        # |- Logar
        self.Btn_Login = Button(self.lf_Login, text="Logar", command=lambda: control.controlMainMenu.Login(self.En_loginNome, self.En_loginSenha, window))
        self.Btn_Login.grid(row=2, column=0, columnspan=2, pady=15)

        # Cadastro
        # |- Nome
        self.lb_cadastroNome = Label(self.lf_Cadastro, text="Nome: ")
        self.lb_cadastroNome.grid(row=0, column=2, padx=10, pady=15)
        self.En_cadastroNome = Entry(self.lf_Cadastro)
        self.En_cadastroNome.grid(row=0, column=3, pady=15)
        # |- Senha
        self.lb_cadastroSenha = Label(self.lf_Cadastro, text="Senha: ")
        self.lb_cadastroSenha.grid(row=1, column=2, pady=15)
        self.En_cadastroSenha = Entry(self.lf_Cadastro, show="*")
        self.En_cadastroSenha.grid(row=1, column=3, pady=15)
        # |- Cadastrar
        self.Btn_Cadastro = Button(self.lf_Cadastro, text="Cadastrar", command=lambda: control.controlMainMenu.Cadastro(self.En_cadastroNome, self.En_cadastroSenha))
        self.Btn_Cadastro.grid(row=2, column=2, columnspan=2, pady=15)

""" Caso necessário chamar a aplicação de outro arquivo."""
def main():
    root = Tk()
    mainmenu(root)
    root.mainloop()

# Inicia o programa, depois de Logado.
def start_Application(nome, id):
    rootApp = Tk()
    User = control.User(id, nome)
    Application(rootApp, User)
    rootApp.mainloop()



if __name__ == "__main__":
    main()

