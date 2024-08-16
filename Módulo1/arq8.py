nome = input('Qual seu nome? ')

print(f'Bem vindo {nome}')

# Útil pra coisas simples e debugs
print(f'Bem vindo, seu {nome = }')

# isso quebra o programa se não receber um inteiro
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))

print(f'A soma dos números é: {numero_1 + numero_2}')

numero_3 = input('Digite o terceiro número: ')
numero_4 = input('Digite o quarto número: ')


# Quebra no type casting, mas futuramnete será útil para verificação anterior ao casting
int_numero3 = int(numero_3)
int_numero4 = int(numero_4)

print(f'A soma dos números é: {int_numero3 + int_numero4}')