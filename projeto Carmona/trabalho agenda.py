agenda = []  # Lista que armazena os contatos da agenda (nome, telefone, endereco, uf, cidade)
alterada = False  # Variável global que marca se a agenda foi alterada

def pede_nome(padrao=""):
    # Solicita ao usuário um nome. Se o usuário não fornecer, retorna o valor padrão.
    nome = input("Nome: ")
    if nome == "":
        nome = padrao
    return nome

def pede_telefone(padrao=""):
    # Solicita ao usuário um telefone. Se o usuário não fornecer, retorna o valor padrão.
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrao
    return telefone

def pede_endereco(padrao=""):
    endereco = input("Endereco: ")
    if endereco == "":
        endereco = padrao
    return endereco

def pede_uf(padrao=""):
    uf = input("UF: ")
    if uf == "":
        uf = padrao
    return uf

def pede_cidade(padrao=""):
    cidade = input("Cidade: ")
    if cidade == "":
        cidade = padrao
    return cidade

def mostra_dados(nome, telefone, endereco, uf, cidade):
    # Exibe o nome e telefone fornecidos na tela.
    print(f"Nome: {nome} Telefone: {telefone} Endereco: {endereco} UF: {uf} Cidade: {cidade}")

def pede_nome_arquivo():
    # Solicita ao usuário o nome de um arquivo.
    return input("Nome do arquivo: ")

def pesquisa(nome):
    # Pesquisa na agenda pelo nome (case-insensitive). Retorna o índice do contato se encontrado, caso contrário, retorna None.
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

def novo():
    global agenda, alterada
    # Adiciona um novo contato na agenda, marcando a agenda como alterada.
    nome = pede_nome()
    if pesquisa(nome) is not None:
        print("Nome já existente na agenda.")
        return
    telefone = pede_telefone()
    endereco = pede_endereco()
    uf = pede_uf()
    cidade = pede_cidade()
    agenda.append([nome, telefone, endereco, uf, cidade])
    alterada = True

def confirma(operacao):
    # Solicita ao usuário a confirmação de uma operação (S para sim, N para não).
    while True:
        opcao = input(f"Confirma {operacao} (S/N)? ").upper()
        if opcao in "SN":
            return opcao
        else:
            print("Resposta inválida. Escolha S ou N.")

def apaga():
    global agenda, alterada
    # Apaga um contato da agenda após a confirmação do usuário.
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        if confirma("apagamento") == "S":
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")

def altera():
    global alterada
    # Altera os dados de um contato existente, permitindo que o usuário mantenha os dados atuais se preferir.
    nome = pede_nome()
    p = pesquisa(nome)
    if p is not None:
        print("Encontrado:")
        mostra_dados(*agenda[p])  # Desempacota a lista para passar os valores individualmente
        nome = pede_nome(agenda[p][0])  # Se nada for digitado, mantém o valor original
        telefone = pede_telefone(agenda[p][1])
        endereco = pede_endereco(agenda[p][2])
        uf = pede_uf(agenda[p][3])
        cidade = pede_cidade(agenda[p][4])
        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone, endereco, uf, cidade]
            alterada = True
    else:
        print("Nome não encontrado.")

def lista():
    # Exibe todos os contatos da agenda com suas posições.
    print("\nAgenda\n" + "-" * 20)
    for posicao, e in enumerate(agenda):
        print(f"Posição: {posicao} ", end="")
        mostra_dados(*e)  # Desempacota a lista para passar os valores individualmente
    print("-" * 20 + "\n")

def lê_última_agenda_gravada():
    # Lê a última agenda gravada se houver um registro dela.
    ultima = ultima_agenda()
    if ultima is not None:
        leia_arquivo(ultima)

def ultima_agenda():
    # Retorna o nome do último arquivo de agenda utilizado, se houver.
    # Caso o arquivo "ultima_agenda.dat" não exista, retorna None.
    try:
        arquivo = open("ultima_agenda.dat", "r", encoding="utf-8")
        ultima = arquivo.readline()[:-1]  # Lê o nome do arquivo, removendo o caractere de nova linha
        arquivo.close()
        return ultima
    except FileNotFoundError:
        return None

def atualiza_ultima(nome):
    # Atualiza o registro do último arquivo de agenda utilizado.
    arquivo = open("ultima_agenda.dat", "w", encoding="utf-8")
    arquivo.write(f"{nome}\n")
    arquivo.close()

def leia_arquivo(nome_arquivo):
    global agenda, alterada
    # Lê um arquivo de agenda e carrega seus dados na lista 'agenda'. Marca a agenda como não alterada.
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    agenda = []
    for l in arquivo.readlines():
        nome, telefone, endereco, uf, cidade = l.strip().split("#")
        agenda.append([nome, telefone, endereco, uf, cidade])
    arquivo.close()
    alterada = False

def lê():
    global alterada
    # Lê uma nova agenda de um arquivo, perguntando antes se deseja salvar as alterações feitas na agenda atual.
    if alterada:
        print("Você não salvou a lista desde a última alteração. Deseja gravá-la agora?")
        if confirma("gravação") == "S":
            grava()
    print("Ler\n" + "-" * 20)
    nome_arquivo = pede_nome_arquivo()
    leia_arquivo(nome_arquivo)
    atualiza_ultima(nome_arquivo)

def ordena():
    global alterada
    # Ordena os contatos na agenda em ordem alfabética pelo nome.
    agenda.sort(key=lambda x: x[0].lower())  # Ordena pelo nome em minúsculas
    alterada = True

def grava():
    global alterada
    # Grava a agenda em um arquivo especificado pelo usuário.
    # Pergunta ao usuário se ele deseja gravar mesmo sem alterações.
    if not alterada:
        print("Você não alterou a lista. Deseja gravá-la mesmo assim?")
        if confirma("gravação") == "N":
            return
    print("Gravar\n" + "-" * 20)
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo, "w", encoding="utf-8")
    for e in agenda:
        arquivo.write(f"{e[0]}#{e[1]}#{e[2]}#{e[3]}#{e[4]}\n")
    arquivo.close()
    atualiza_ultima(nome_arquivo)
    alterada = False

def valida_faixa_inteiro(pergunta, inicio, fim):
    # Solicita ao usuário um número inteiro dentro de uma faixa especificada (inicio a fim).
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f"Valor inválido, favor digitar entre {inicio} e {fim}")

def menu():
    # Exibe o menu principal com as opções de operações disponíveis. Retorna a escolha do usuário.
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

lê_última_agenda_gravada()  # Tenta carregar a última agenda utilizada ao iniciar o programa

while True:
    # Loop principal que exibe o menu e executa as operações escolhidas pelo usuário.
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