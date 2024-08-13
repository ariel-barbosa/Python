# agenda
import nome

# criando lista 'agenda'
agenda = []

# Variável para marcar uma alteração na agenda
alterada = False


# função pede nome
# determina o padrão de nome que o usuario deve digitar
def pede_nome(padrao = ""):
    nome = input("Nome: ")
    if nome == "":
        nome = padrao
        return nome

# determina o padrão de telefone que o usuario deve digitar
def pede_telefone(padrao = ""):
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrao
        return telefone

# determina o padrão de email que o usuario deve digitar
def pede_email(padrao = ""):
    email = input("Email: ")
    if email == "":
        email = padrao
        return email


# determina o padrão de aniversario que o usuario deve digitar
def pede_aniversário(padrao=""):
    aniversario = input("Data de aniversário: ")
    if aniversario == "":
        aniversário = padrao
        return aniversario


# mostra os dados do usuario
def mostra_dados(nome, telefone, email, aniversario):
    print(
        f"Nome: {nome}\nTelefone: {telefone}\n"
        f"Email: {email}\nAniversário: {aniversario}\n"
    )

# funcao que pede o nome do arquivo
def pede_nome_arquivo():
    return input("Nome do Arquivo: ")

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
            return None

def novo():
    global agenda, alterada
    nome = pede_nome()
    if pesquisa() is not None:
        print("Nome já existe!")
        return
        telefone = pede_telefone()
        agenda.append([nome, telefone, email, aniversario])
        alterada = True

def confirma(operacao):
    while True:
        opcao = input(f"Confirma {operacao} (S/N)? ").upper()
        if opcao in "SN":
            return opcao
        else:
            print("Resposta invalida. Escolha S ou N. ")

def apaga():
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None and confirma("apagamento") == "S":
        del agenda[p]
        alterada = True
    else:
        print("Nome não encontrado... ")

def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        email = agenda[p][2]
        aniversário = agenda[p][3]
        print("Encontrado:")
        mostra_dados(nome, telefone, email, aniversário)
        nome = pede_nome(nome)  # Se nada for digitado, mantém o valor
        telefone = pede_telefone(telefone)
        email = pede_email(email)
        aniversário = pede_aniversário(aniversário)

        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone, email, aniversário]
            alterada = True
        else:
            print("Nome não encontrado.")


def lista():
    print("\nAgenda\n\n\------")

    # Usamos a função enumerate para obter a posição na agenda
    for posicao, 















