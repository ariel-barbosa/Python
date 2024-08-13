#  receber uma lista de inteiros 
# e separar os números positivos e 
# negativos da lista

# recebendo valores

lista = []
i = 1


while i <= 6: 
    valor = int(input("Digite um valor positivo ou negativo: "))
    lista.append(valor)
    i+=1
print("Lista original \n", lista)


# Função que retorna True se o valor for positivo, False caso contrário
def e_positivo(valor):
    return valor > 0
def e_negativo(valor):
    return valor < 0



lista_positivos = list(filter(e_positivo, lista))
lista_negativos = list(filter(e_negativo, lista))

print("Positivos: ", lista_positivos)
print("Positivos: ", lista_negativos)