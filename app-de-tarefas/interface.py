import PySimpleGUI as sg
import bancodedados
from datetime import datetime

data_taf = datetime.now().strftime("%d-%m-%Y %H:%M")


# -------------------------- TELA INICIAL
tela_inicio = [
    [sg.Text("Lista de tarefas", font="Arial 25")],
    [
        sg.Column(
            [
                [
                    sg.Button("Tarefas", size=12, font="Arial 15"),
                    sg.Button("Consultar", size=12, font="Arial 15"),
                    sg.Button("Outros", size=12, font="Arial 15"),
                ]
            ]
        )
    ],
]

# ---------------------------TELA TAREFAS
tela_taf = [
    [sg.Text("Lista de tarefas", font="Arial 25")],
    [sg.Text("Clique na opção desejada", font="Arial 20")],
    [
        sg.Button("Add tarefa", size=12, font="Arial 15"),
        sg.Button("Exc tarefa", size=12, font="Arial 15"),
    ],
]

tela_add = [
    [sg.Text("Adicionar tarefas", font="Arial 25")],
    [sg.Text("Nome da tarefa", font="Arial 15")],
    [sg.Input(key="nome_taf", size=20, font="Arial 15")],
    [sg.Text("Prioridade", font="Arial 15")],
    [sg.Input(key="prio_taf", size=20, font="Arial 15")],
    [sg.Text("Descrição", font="Arial 15")],
    [sg.Input(key="desc_taf", size=20, font="Arial 15")],
    [
        sg.Button("Enviar", size=10, font="Arial 15"),
        sg.Button("Limpar", size=10, font="Arial 15"),
    ],
]

tela_exc = [
    [sg.Text("Excluir tarefa", font="Arial 25")],
    [sg.Text("Nome da tarefa", font="Arial 15")],
    [sg.Input(key="nome_exc", size=20, font="Arial 15")],
    [
        sg.Button("Enviar", size=10, font="Arial 15"),
        sg.Button("Limpar", size=10, font="Arial 15"),
    ],
]

# -----------------------------TELA VISUALIZAR

tela_cons = [
    [sg.Text("Consultar tarefas", font="Arial 25")],
    [sg.Button("Consultar", size=10, font="Arial 15")],
    [sg.Text('',font='Arial 15',key='alterar')]


]

# tela_cons_prio = []

# tela_cons_data = []

# -----------------------------TELA OUTROS

# só o adm pode gerenciar o BD
# criar a senha e o login do ADM, as funções no BD e outros.


tela_outros = [
    [sg.Text("Outros", font="Arial 25")],
    [sg.Text("Usuario ADM", font="Arial 15")],
    [sg.Input(key="user_adm", size=20, font="Arial 15")],
    [sg.Text("Senha", font="Arial 15")],
    [sg.Input(key="senha_adm", size=20, font="Arial 15")],
    [
        sg.Button("Enviar", size=10, font="Arial 15"),
        sg.Button("Limpar", size=10, font="Arial 15"),
    ],
]

# ---------------------------------------------

jan_taf = False
jan_taf_add = False
jan_taf_exc = False
jan_outros = False
jan_cons = False


# cria a janela
janela_inicio = sg.Window(
    "Tela Inicial", layout=tela_inicio, element_justification="center"
)
janela_taf = sg.Window(
    "Tela de Tarefas", layout=tela_taf, element_justification="center"
)
janela_add = sg.Window(
    "Tela Add Tarefas", layout=tela_add, element_justification="center"
)
janela_exc = sg.Window(
    "Tela Exc Tarefas", layout=tela_exc, element_justification="center"
)
janela_o = sg.Window(
    "Tela Outros", layout=tela_outros, element_justification="center"
)
janela_cons = sg.Window(
    "Tela de Consulta", layout=tela_cons, element_justification="center"
)


# -------------------------JANELAS
while True:
    evento, valor = janela_inicio.read()
    if evento == sg.WIN_CLOSED:
        break

    elif evento == "Tarefas":
        janela_inicio.close()
        jan_taf = True
        janela_inicio.close()
        jan_taf = True

    elif evento == "Consultar":
        janela_inicio.close()
        jan_cons = True
        

    elif evento == "Outros":
        janela_inicio.close()
        jan_outros = True

if jan_taf:
    while True:
        evento, valor = janela_taf.read()
        if evento in [sg.WIN_CLOSED, "Fim"]:
            break
        elif evento == "Add tarefa":
            janela_taf.close()
            jan_taf_add = True
        elif evento == "Exc tarefa":
            janela_taf.close()
            jan_taf_exc = True

if jan_taf_add:
    while True:
        evento, valor = janela_add.read()
        if evento in [sg.WIN_CLOSED, "Fim"]:
            break
        elif evento == "Limpar":
            janela_add["nome_taf"].update("")
            janela_add["prio_taf"].update("")
            janela_add["desc_taf"].update("")

        elif evento == "Enviar":
            nome = valor["nome_taf"]
            prio = valor["prio_taf"]
            desc = valor["desc_taf"]
            data_taf = datetime.now().strftime("%Y-%m-%d %H:%M")

            bd_tarefa = bancodedados.Bd_tarefas()
            bd_tarefa.incluir_taf(nome, prio, desc, data_taf)
            bd_tarefa.fechar()
            sg.popup("Tarefa adicionada com sucesso")
            janela_add.close()

if jan_taf_exc:
    while True:
        evento, valor = janela_exc.read()
        if evento in [sg.WIN_CLOSED, "Fim"]:
            break
        elif evento == "Limpar":
            janela_add["nome_taf"].update("")

        elif evento == "Enviar":
            nome_exc = valor['nome_exc']

            bd_tarefa = bancodedados.Bd_tarefas()
            bd_tarefa.excluir_taf(nome_exc)
            bd_tarefa.fechar()
            sg.popup("Tarefa removida com sucesso!")
            janela_exc.close()         

if jan_outros:
    while True:
        evento, valor = janela_o.read()
        if evento in [sg.WIN_CLOSED, "Fim"]:
            break
        elif evento == "Limpar":
            janela_o["user_adm"].update("")
            janela_o["senha_adm"].update("")

        elif evento == "Enviar":
            pass


# ------------------------------------ Só ta apareendo uma atualização
if jan_cons:
    while True:

        evento, valor = janela_cons.read()
        if evento in [sg.WIN_CLOSED, "Fim"]:
            break

        elif evento == 'Consultar':
            
            lista = []
            bd_tarefa = bancodedados.Bd_tarefas()
            tarefas = bd_tarefa.consultar_taf()
            bd_tarefa.fechar()

            resposta = ''

            for tarefa in tarefas:
                resposta = f'''
                Nome: {tarefa[0]}
                Prioridade: {tarefa[1]}
                Descrição: {tarefa[2]}
                Data: {tarefa[3]}
                '''
            lista.append(resposta)
            janela_cons['alterar'].update(lista)
            