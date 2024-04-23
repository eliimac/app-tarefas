import sqlite3

class Bd_tarefas:
    def __init__(self) -> None:
        self.conexao = sqlite3.connect('bd_tarefas.sqlite')
        self.cursor = self.conexao.cursor()

    def fechar(self):
        self.conexao.close()

    def criar_tabela(self):
        cmdSQL = '''
                CREATE TABLE tarefas(
                    nome_tarefa varchar(30) primary key,
                    prioridade int not null,
                    descricao varchar(100),
                    data datetime                   
                )
        ''' 
        self.cursor.execute(cmdSQL)

    def incluir_taf(self,nome,prio,desc,data):
        cmdSQL = '''
                INSERT INTO tarefas (
                    nome_tarefa,prioridade,descricao,data
                )
                VALUES (?,?,?,?)
        '''
        self.cursor.execute(cmdSQL,(nome,prio,desc,data))
        self.conexao.commit()

    def excluir_taf(self,nome):
        cmdSQL = '''
                DELETE FROM tarefas
                WHERE nome_tarefa = ?   
        '''
        self.cursor.execute(cmdSQL,(nome,))
        self.conexao.commit()
    
    def consultar_taf(self):
        cmdSQL = '''
                SELECT nome_tarefa,prioridade,descricao,data
                FROM tarefas
        '''
        self.cursor.execute(cmdSQL)
        resposta = self.cursor.fetchall()
        return resposta

    # def consultar_taf_prio(self,prio):
    #     cmdSQL = '''
    #             SELECT nome_tarefa,prioridade,descricao,data
    #             FROM tarefas 
    #             WHERE prioridade = ?
    #     '''
    #     self.cursor.execute(cmdSQL,(prio,))
    #     resposta = self.cursor.fetchall()
    #     return resposta
    
    # def consultar_taf_data(self,data):
    #     cmdSQL = '''
    #             SELECT nome_tarefa,prioridade,descricao,data
    #             FROM tarefas 
    #             WHERE data = ?
    #     '''
    #     self.cursor.execute(cmdSQL,(data,))
    #     resposta = self.cursor.fetchall()
    #     return resposta        