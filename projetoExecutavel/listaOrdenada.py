# intercalar duas listas

#EXEMPLO
# numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# numeros_ordenados = sorted(numeros)
# print(numeros_ordenados)

# entrada de dados lista 1



lista1 = list() # sem argumentos cria uma lista vazia

i = 1
while i <= 10:
    elemento = int(input("Digite um elemento da lista 1: "))
    lista1.append(elemento) # o .append acrescenta um elemento ao fim da lista
    i+=1

print(lista1)

# Ordena a Lista 1
lista1_ordenada = sorted(lista1)
print(lista1) # printa a lista 1 ordenada

# entrada de dados da lista 2
lista2 = list()
i = 1

while i <= 10:
    elemento = int(input("Digite um elemento da lista 2: "))
    lista2.append(elemento)
    i+=1

print(lista2)

# Ordena a Lista 2
lista2_ordenada = sorted(lista2)
print(lista2_ordenada) # printa a lista 1 ordenada

# Listas intercaladas
intercalada = []

i = j = 0
while i < len(lista1_ordenada) and j < len(lista2_ordenada):
    if lista1_ordenada[i] < lista2_ordenada[j]:
        intercalada.append(lista1_ordenada[i])
        i += 1
    else:
        intercalada.append(lista2_ordenada[j])
        j += 1
        intercalada += lista1_ordenada[i:]
        intercalada += lista2_ordenada[j:]

print("Listas Intercaladas: \n")
print(intercalada)

input("::::: ENTER para sair :::::")