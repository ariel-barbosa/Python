# agenda 

agenda = []

alterada = False # Variável para marcar uma alteração na agenda

# função pede nome
# determina o padrão de nome que o usuario deve digitar
def pede_nome(padrão = ""):
    nome = input("Nome: ")

if nome == "":
    nome = padrão
    return nome


# determina o padrão de telefone que o usuario deve digitar
def pede_telefone(padrão = ""):
    telefone = input("Telefone: ")

if telefone == "":
    telefone = padrão
    return telefone



# determina o padrão de email que o usuario deve digitar
def pede_email(padrão=""):
    email = input("Email: ")

if email == "":
    email = padrão
    return email



# determina o padrão de aniversario que o usuario deve digitar
def pede_aniversário(padrão=""):
    aniversário = input("Data de aniversário: ")

if aniversário == "":
    aniversário = padrão
    return aniversario


# mostra os dados do usuario
def mostra_dados(nome, telefone, email, aniversario):
    print(
        f"Nome: {nome}\nTelefone: {telefone}\n"
        f"Email: {email}\nAniversário: {aniversario}\n"
    )

