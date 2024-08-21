"""
Fatiamento de strings
 012345678
 Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd 
de caracteres da str
"""
variavel = 'Olá mundo'
frase = 'Alguém um dia me disse que o tempo é um predador que nos vigia. Mas eu acho que o tempo é um companheiro que viaja conosco, nos lembrando de aproveitar cada momento, porque eles são únicos e não voltam mais.'
print(variavel[4:])
print(variavel[4:6])
print(variavel[:6])
print(variavel[:-6])
print(variavel[-8:-2])
print(variavel[::-1])
print(len(variavel))
print(variavel[0:len(variavel):2])
print(frase[::-1])