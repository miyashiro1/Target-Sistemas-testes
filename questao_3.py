import json

# Comando para ler o arquivo json
with open('dados.json') as f:
    data = json.load(f)

# Calcular o faturamento total e os dias para tirar a média
total = 0.0
dias = 0

for item in data:
    if item['valor'] > 0:
        total += item['valor']
        dias += 1

# Média do mes
media = total / dias

# Variável para guardar o maior e menor valor
menor = data[0]['valor']
maior = data[0]['valor']


for item in data:
    if item['valor'] > 0 and item['valor'] < menor:
        menor = item['valor']
    elif item['valor'] > maior:
        maior = item['valor']

# Variável para guardar os dias com o faturamento maior que a média mensal
maior_media_mensal_dias = 0
for item in data:
    if item['valor'] > media:
        maior_media_mensal_dias += 1

print(f"Menor faturamento, {menor}")
print(f"Maior faturamento, {maior}")
print(f"Número de dias com faturamento maior que a média mensal, {maior_media_mensal_dias}")