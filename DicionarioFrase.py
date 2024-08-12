# # criando dicionario 
# # A pista
# frase = {
#     "A": 1,
#     "p": 2,
#     "i": 3,
#     "s": 4,
#     "t": 5,
#     "a": 6
# }


def criar_dicionario_posicoes(frase):
  """
  Cria um dicionário onde as chaves são os caracteres da frase e os valores são as
  posições (índices) em que os caracteres aparecem pela primeira vez.

  Args:
    frase: A frase de entrada.

  Returns:
    Um dicionário com as posições dos caracteres.
  """

  dicionario_posicoes = {}
  for indice, caractere in enumerate(frase):
    if caractere not in dicionario_posicoes:
      dicionario_posicoes[caractere] = indice + 1  # +1 para começar a contagem em 1

  return dicionario_posicoes

# Exemplo de uso:
frase = input("Digite uma frase: ")
resultado = criar_dicionario_posicoes(frase)
print(resultado)

