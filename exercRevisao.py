<<<<<<< HEAD
=======
# agenda


# criando lista 'agenda'
from pickle import FALSE


>>>>>>> 642e3072cae432a33699a6092d62051bdc5c6f75
agenda = []
alterada = False

<<<<<<< HEAD
def pede_nome(padrao=""):
    nome = input("Nome: ")
    if nome == "":
        nome = padrao
    return nome
=======

# função pede nome
# determina o padrão de nome que o usuario deve digitar
def pede_nome(padrao=""):
    nome = input("Nome: ")
    return nome or ""  # Retorna nome se não for vazio, senão retorna ""

>>>>>>> 642e3072cae432a33699a6092d62051bdc5c6f75

def pede_telefone(padrao=""):
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrao
    return telefone

def mostra_dados(nome, telefone):
    print(f"Nome: {nome} Telefone: {telefone}")

def pede_nome_arquivo():
    return input("Nome do arquivo: ")

def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
<<<<<<< HEAD
    return None
=======
        return None
>>>>>>> 642e3072cae432a33699a6092d62051bdc5c6f75

def novo():
    global agenda, alterada
    nome = pede_nome()
<<<<<<< HEAD
    telefone = pede_telefone()
    agenda.append([nome, telefone])
    alterada = True
=======
    if pesquisa(nome) is not None:
        print("Nome já existe!")
        return
        telefone = pede_telefone()
        agenda.append([nome, telefone, email, aniversario])
        alterada = True
>>>>>>> 642e3072cae432a33699a6092d62051bdc5c6f75

def confirma(operacao):
    while True:
        opcao = input(f"Confirma {operacao} (S/N)? ").upper()
        if opcao in "SN":
            return opcao == "S"
        else:
            print("Resposta inválida. Escolha S ou N.")

def apaga():
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        if confirma("apagamento"):
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")

def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print("Encontrado:")
        mostra_dados(nome, telefone)
        nome = pede_nome(nome)  # Se nada for digitado, mantém o valor
        telefone = pede_telefone(telefone)
        if confirma("alteração"):
            agenda[p] = [nome, telefone]
            alterada = True
    else:
        print("Nome não encontrado.")

def lista():
<<<<<<< HEAD
    print("\nAgenda\n\n------")
    for posicao, e in enumerate(agenda):
        print(f"Posição: {posicao} ", end="")
        mostra_dados(e[0], e[1])
    print("------\n")
=======
    print("\nAgenda\n\n\------")

    # Usamos a função enumerate para obter a posição na agenda
    for posição, e in enumerate(agenda):
        print(f"\nPosição: {posição}") # Imprimimos a posição
        mostra_dados(e[0], e[1], e[2], e[3])
        print("\------\n")

def lê_última_agenda_gravada():
    ultima = ultima_agenda()
    if ultima is not None:
        leia_arquivo(ultima)


def ultima_agenda():
    try:
        arquivo = open("ultima agenda.dat", "r", encoding="utf-8")
        ultima = arquivo.readline()[:-1]
        arquivo.close()
    except FileExistsError:
        return None
        return ultima
    

def atualiza_ultima(nome):
    arquivo = open("ultima agenda.dat", "w", encoding="utf-8")
    arquivo.write(f"{nome}\n")
    arquivo.close()


def leia_arquivo(nome_arquivo):
    global agenda, alterada
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    agenda = []

    for l in arquivo.readlines():
        nome, telefone, email, aniversário = l.strip().split("#")
        agenda.append([nome, telefone, email, aniversário])
        arquivo.close()
        alterada = False


def le():
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")

    if confirma("gravação") == "S":
        grava()
        print("Ler\n---")
        nome_arquivo = pede_nome_arquivo()
        leia_arquivo(nome_arquivo)
        atualiza_ultima(nome_arquivo)

def ordena():
    global alterada
    # Você pode ordenar a lista como mostrado no livro
    # com o método de bolhas (bubble sort)
    # Ou combinar o método sort do Python com lambdas para
    # definir a chave da lista
    # agenda.sort(key=lambda e: return e[0])

    fim = len(agenda)

    while fim > 1:
        i = 0

    trocou = False

    while i < (fim - 1):
        if agenda[i] > agenda[i + 1]:
            # Opção: agenda[i], agenda[i+1] = agenda[i+1], agenda[i]
            temp = agenda[i + 1]
            agenda[i + 1] = agenda[i]
            agenda[i] = temp
            trocou = True
            i += 1

            if not trocou:
                break
            altera = True


def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return 
        print("Gravar\n\------")
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")

    for e in agenda:
        arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}\n")
        arquivo.close()
        atualiza_ultima(nome_arquivo)
        alterada = False


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:

            print("Valor inválido, favor digitar entre {inicio} e {fim}")

def menu():
    print("""
    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Lê
    7 - Ordena por nome
    0 - Sai
    """)
    print(f"\nNomes na agenda: {len(agenda)} Alterada: {alterada}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)
    lê_última_agenda_gravada()

while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        novo()
    elif opção == 2:
        altera()
    elif opção == 3:
        apaga()
    elif opção == 4:
        lista()
    elif opção == 5:
        grava()
    elif opção == 6:
        le()
    elif opção == 7:
        ordena()

                        

>>>>>>> 642e3072cae432a33699a6092d62051bdc5c6f75

def lê_ultima_agenda_gravada():
    ultima = ultima_agenda()
    if ultima is not None:
        leia_arquivo(ultima)

def ultima_agenda():
    try:
        with open("ultima_agenda.dat", "r", encoding="utf-8") as arquivo:
            ultima = arquivo.readline().strip()
        return ultima
    except FileNotFoundError:
        return None

def atualiza_ultima(nome):
    with open("ultima_agenda.dat", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome}\n")

def leia_arquivo(nome_arquivo):
    global agenda, alterada
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        agenda = [linha.strip().split("#") for linha in arquivo.readlines()]
    alterada = False

def lê():
    global alterada
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação"):
            grava()
    print("Ler\n---")
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_ultima(nome_arquivo)

def ordena():
    global alterada
    agenda.sort(key=lambda e: e[0].lower())
    alterada = True

def grava():
    global alterada
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if not confirma("gravação"):
            return
    print("Gravar\n------")
    nome_arquivo = pede_nome_arquivo()
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        for e in agenda:
            arquivo.write(f"{e[0]}#{e[1]}\n")
    atualiza_ultima(nome_arquivo)
    alterada = False

def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

def menu():
    print("""
1 - Novo
2 - Altera
3 - Apaga
4 - Lista
5 - Grava
6 - Lê
7 - Ordena por nome
0 - Sai
""")
    print(f"\nNomes na agenda: {len(agenda)} Alterada: {alterada}\n")
    return valida_faixa_inteiro("Escolha uma opção: ", 0, 7)

lê_ultima_agenda_gravada()

while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        lê()
    elif opcao == 7:
        ordena()














