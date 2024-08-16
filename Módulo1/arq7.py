from datetime import datetime

## Fstrings e Format:

# Primeiro as fstrings:

preco_do_pastel = 5.85
quantidade_do_pedido = 15
mesa = 14
valor_coca_cola = 12.00
data_do_pedido = datetime.now()
cliente="José Carlos Carluxo"

print('Feito com fstring:')
print(f'O cliente {cliente} comprou {quantidade_do_pedido} pastéis à {preco_do_pastel}')
print(f'Para beber, consumirão uma Coca Cola 2L no valor de {valor_coca_cola}')
print(f'Pedido à ser entregue na mesa {mesa}, junto da conta no valor de R$ {(preco_do_pastel*quantidade_do_pedido):.2f}')
print(f'Pedido Realizado em: {data_do_pedido.date()}')

# Agora usando Format:

print('\nFeito com format:')
print('O cliente {} comprou {} pastéis à {}'.format(cliente, quantidade_do_pedido, preco_do_pastel))
print('Para beber, consumirão uma Coca Cola 2L no valor de {}'.format(valor_coca_cola))
print('Pedido à ser entregue na mesa {}, junto da conta no valor de R$ {:.2f}'.format(mesa, preco_do_pastel*quantidade_do_pedido))
print('Pedido Realizado em: {}'.format(data_do_pedido.date()))

# Só para demonstrar o uso de índices em format:

print('Aqui vai o argumento 3: {2}, aqui o 1: {0} e aqui o 2: {1}'.format(8,5,4))

# Uso de parâmetros nomeados:

print('Aqui vai o argumento 3: {terceiro}, aqui o 1: {0} e aqui o 2: {1}'.format(8,5,terceiro=4))

# print(terceiro) - não funciona, devido ao escopo, pois a nomeação não declara uma variável para fora do format.