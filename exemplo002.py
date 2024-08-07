n1 = float(input('Digite um numero: '))
n2 = float(input('Digite um numero: '))

while True:
    print('Escolha uma opção digitando o numero correspondente ')

    print('[1] - SOMAR')
    print('[2] - SUBTRAIR')
    print('[3] - MULTIPLICAR')
    print('[4] - PARA SAIR')

op = int(input('Qual a opção desejada? '))

while op < 1 or op > 4:
    op = int(input('Opção Inválida! Digite novamente... '))

    if op == 4:
        break

while op != 4:
    if op == 1:
        resultado = n1 + n2
    elif op == 2:
        resultado = n1 - n2
    elif op == 3:
        resultado = n1 * n2


    print('Resultado = {}'.format(resultado))




