import main
import DB

# Controle de Login
def Login(En_user, En_senha, window):
    user = En_user.get() # Armazena o Usuario
    senha = En_senha.get() # Armazena a senha

    if user == "" or senha == "": # Se nao forem digitados
        main.messagebox.showerror("Campos Vazios", "Preencha seu nome de usuario senha!")
    else:
        # Se tiver sucesso, VerificarLogin retornará o id do usuario, se não retornará Null
        id = VerificarLogin(user, senha)
        if id:
            window.destroy()
            main.start_Application(user, id[0][0])
        else:
            print("Password ou Senha incorretos")
            
# Cadastro de novos usuarios
def Cadastro(En_user, En_senha):
    user = En_user.get() # Armazena o usuario
    senha = En_senha.get() # Armazena a senha

    if user == "" or senha == "": # Se não forem digitados
        main.messagebox.showerror("Campos Vazios", "Preencha seu nome de usuario senha!")
    else: 
        if VerificarCadastro(user): # Se ja está cadastrado
            main.messagebox.showerror("Usuario", "Usuario já cadastrado!")
        else:
            banco = DB.Banco()
            resposta = banco.adicionarUsuario(user, senha)
            if resposta:
                main.messagebox.showinfo("Sucesso!", "Cadastrado com Sucesso!")
                En_user.delete(0, "end")
                En_senha.delete(0, "end")
            else:
                main.messagebox.showerror("Error", "Erro ao cadastrar, contate o desenvolvedor")

# Ver se login e senha estão corretos.
def VerificarLogin(user, senha):
    banco = DB.Banco()
    dados = banco.verificarLogin(user, senha)
    return dados

# Ver se o usuario, já foi cadastrado
def VerificarCadastro(user):
    banco = DB.Banco()
    sql = f"SELECT * from Usuario where nome = '{str(user)}'"
    dados = banco.selecionar(sql)
    return 1 if dados else 0
