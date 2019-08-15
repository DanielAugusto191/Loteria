import sqlite3

# Classe que se comunica com o Banco de Dados.
class Banco():
    def __init__(self):
        pass
    # Caso não possua o banco de dados, crie as tabelas.
    def NotHasDB(self):
        # Caso não tenha o banco, crie o banco com as tabelas abaixo:
        sql = ["""CREATE TABLE IF NOT EXISTS Usuario(
                id INTEGER primary key AUTOINCREMENT UNIQUE,
                nome varchar(45),
                password varchar(45)
                );""",
                """ CREATE TABLE IF NOT EXISTS Numeros(
                id INTEGER primary key AUTOINCREMENT UNIQUE,
                user_ID INTEGER,
                numero INTEGER,
                vezesJogadas INTEGER DEFAULT 0,
                vezesSorteadas INTEGER DEFAULT 0, 
                foreign key(user_ID) references Usuario(id)
                );""",
                """CREATE TABLE IF NOT EXISTS Acertos(
                id INTEGER primary key AUTOINCREMENT UNIQUE,
                id_User INTEGER,
                Unos INTEGER DEFAULT 0,
                Duques INTEGER DEFAULT 0,
                Ternos INTEGER DEFAULT 0,
                Quadras INTEGER DEFAULT 0,
                Quinas INTEGER DEFAULT 0
                );"""
               ]
        self.create(sql)
    # Cria o banco de dados e as tabelas definidas em {sql}.
    def create(self, sql):
        try:
            conn = sqlite3.connect("BancoDeDados/estatisticas.db") # Tenta conectar, se não conseguir cria o banco
            cursor = conn.cursor()
            for x in sql:
                cursor.execute(x)
                conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error {e}")
    # Adiciona no banco os números jogados e sorteados.
    def adicionar(self, id, listaJogada, listaSorteada, acertos):
        try:
            conn = sqlite3.connect("BancoDeDados/estatisticas.db")
            cursor = conn.cursor()
            # Faz com que seja adicionado 1 ao numero de vezes dos números jogadas
            for x in listaJogada:
                sql = f"UPDATE Numeros SET vezesJogadas = vezesJogadas+1 where user_ID = {id} and numero={x}"
                cursor.execute(sql)
                conn.commit()
            
            # Faz com que seja adicionado 1 ao numero de vezes dos números sorteados
            for x in listaSorteada:
                sql = f"UPDATE Numeros SET vezesSorteadas = vezesSorteadas+1 where user_ID = {id} and numero={x}"
                cursor.execute(sql)
                conn.commit()
            
            # Se acertou adicione quantos numeros acertou ao banco de dados.
            if acertos:
                possibilidadesDeAcertos = ['Unos', 'Duques', 'Ternos', 'Quadras', 'Quinas']
                sql = f"UPDATE Acertos set {possibilidadesDeAcertos[acertos-1]} = {possibilidadesDeAcertos[acertos-1]}+1 where id_User = {id}"
                cursor.execute(sql)
                conn.commit()
            conn.close()
            return 1
        except Exception as e:
            print((f"Error {e}"))
            return 0
    # Adiciona ao banco Novos Usuarios
    def adicionarUsuario(self, nome, password):
        sql = f"INSERT INTO Usuario (nome, password) values ('{nome}', '{password}');"
        try:
            conn = sqlite3.connect("BancoDeDados/estatisticas.db")
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            sql = f"SELECT id from Usuario where nome='{nome}' and password='{password}'"
            cursor.execute(sql)
            _id = cursor.fetchall()
            _id = _id[0][0]

            # Cria o número de vezes que esse usuario adicionou o número.
            for x in range(80):
                sql = f"INSERT INTO Numeros (user_ID, numero) values ({_id}, {x+1})"
                conn.execute(sql)
                conn.commit()
                
            # Cria os campos de acertos desse usuario
            sql = f"INSERT INTO Acertos (id_User) values ({_id})"
            conn.execute(sql)
            conn.commit()
            conn.close()
            return 1
        except Exception as e:
            print((f"Error {e}"))
            return 0
        pass
    # Dados a {sql} busque os dados no banco e retorne
    def selecionar(self, sql):
        try:
            conn = sqlite3.connect("BancoDeDados/estatisticas.db")
            cursor = conn.cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()
            conn.close()
            return resultado
        except Exception as e:
            print(f"Error {e}")

    # Logar com usuario e Senha
    def verificarLogin(self, user, senha):
        sql = f"SELECT id from Usuario where nome = '{user}' and password = '{senha}'"
        try:
            conn = sqlite3.connect("BancoDeDados/estatisticas.db")
            cursor = conn.cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()
            conn.close()
            return resultado
        except Exception as e:
            print(f"Error {e}")
