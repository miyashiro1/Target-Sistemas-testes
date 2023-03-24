# Primeiro transformamos em um dicionário e somamos tudo. Podemos utilizar o comando sum(faturamento_mensal.values()
# ou utilizar um loop
faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Soma dos faturamentos
total = 0
for i in faturamento_mensal:
    total += (faturamento_mensal[i])

# calcula o percentual de cada estado
for estado, valor in faturamento_mensal.items():
    percentual = (valor/total) * 100
    print(f'{estado}: {percentual:.2f}%')