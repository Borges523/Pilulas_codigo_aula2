import math
import random
cotacao = float(input('cotacao atual do dolar'))
variacao = random.uniform(-0.015, 0.015)
nova_cotacao = cotacao * (1 + variacao)
print (f'Variacao simulada: {variacao: .3%}')
print(f'nova cotacao: {nova_cotacao:.2f}')
