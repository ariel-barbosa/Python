# Criptografia utilizando a cifra de César

msg = input("Digite a mensagem a ser criptografada: ")

criptografada = ''

i = len(msg) - 1 # para pegar o ultimo elemento da mensagem

while (i >= 0):
    criptografada = criptografada + msg[i]
    i -= 1

print("Mensagem Criptografada: ", criptografada)

input("::::::: ENTER para sair :::::::::")
