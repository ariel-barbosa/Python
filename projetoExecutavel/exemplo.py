# Ler 10 números e imprimir a soma, o maior e o menor
# import math

numeros = []
for i in range(10):
    num = int(input('Digite um número: '))
    numeros.append(num)

soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)
print('Soma:', soma)
print('Maior:', maior)
print('Menor:', menor)