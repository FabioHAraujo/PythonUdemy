concatenada = 'A' + 'B' + 'C'
print(concatenada)

def multiplica_string(string, quantidade):
  print(string*quantidade)

multiplica_string('Salve', 15)

# PRECEDÊNCIA:
# 1 - () - PARÊNTESES
# 2 - ** - EXPONENCIAÇÃO
# 3 - *, /, //, % - OPERADORES DE MULTIPLICAÇÃO E DIVISÃO
# 4 - + E - SOMA E DIVISÃO

# Exemplo bobinho:
print(1+1**5+5) # Objetivo do autor era dar 1024, por matemática simples, resultado será 7

# Corrigido: 
print((1+1)**(5+5)) # Agora os parênteses garantem a integridade do resultado


