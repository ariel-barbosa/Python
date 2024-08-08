# Verificar se uma string é uma palíndromo

import string
import time


palavra = input("Digite uma palavra qualquer: ")

inversa = palavra[::-1]

if palavra != inversa:
    print('Não é palindromo')
else:
    print('É UM PALINDROMO')

input("ENTER PARA SAIR")
