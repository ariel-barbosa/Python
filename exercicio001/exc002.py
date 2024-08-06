# Somar os digítos de um número menor que 100

num = int(input("Digite um numero menor que 100: "))
if num >= 100:
    print("Deve ser menor que 100.")

else:
    dezena = num // 10
    unidade = num % 10

soma = dezena + unidade
print("soma: ", soma)