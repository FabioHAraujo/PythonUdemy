"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{variavel:$^10}.')
print(f'{10000.654687654654846889:.3f}')
print(f'{-10000.654687654654846889:+.3f}') # FORÇA MOSTRAR SE É POSITIVO OU NEGATIVO
print(f'{10000.654687654654846889:+.3f}') # FORÇA MOSTRAR SE É POSITIVO OU NEGATIVO
print(f'{10000.654687654654846889:0>+15.3f}') # FORÇA AS CASAS TOTAIS PARA O NUMERO, MAS FICA ESTRANHO O SINAL
print(f'{10000.654687654654846889:0=+15.3f}') # CONSERTA O DE CIMA
print(f'{-10000.654687654654846889:0=+15.3f}') # NEGATIVO
print(f'O hexadecimal de 1500 é {1500:08X}') # HEXA
print(f'{variavel!r}')