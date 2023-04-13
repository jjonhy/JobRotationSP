import json

# carrega os dados do arquivo json
with open('dados.json') as f:
    data = json.load(f)

# inicializa as variáveis para o menor e maior valor de faturamento
min_faturamento = data[0]['valor']
max_faturamento = data[0]['valor']

# inicializa as variáveis para a soma e contagem dos valores de faturamento
soma_faturamento = 0
num_dias_faturamento = 0

# loop para percorrer os valores do json
for dia in data:
    valor = dia['valor']
    if valor > 0:
        # atualiza as variáveis para o menor e maior valor de faturamento
        if valor < min_faturamento:
            min_faturamento = valor
        if valor > max_faturamento:
            max_faturamento = valor

        # adiciona o valor de faturamento à soma e aumenta a contagem de dias com faturamento
        soma_faturamento += valor
        num_dias_faturamento += 1

# calcula a média dos valores de faturamento, apenas com os dias com faturamento maior que zero
media_faturamento = soma_faturamento / num_dias_faturamento

# imprime os resultados
print("Menor valor de faturamento: R$ {:.2f}".format(min_faturamento))
print("Maior valor de faturamento: R$ {:.2f}".format(max_faturamento))
print("Número de dias com faturamento maior que a média: {}".format(
    sum(1 for dia in data if dia['valor'] > media_faturamento)))
