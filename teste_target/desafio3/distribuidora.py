#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
# na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser
# ignorados no cálculo da média;



import json

with open("dados.json") as data:
    dados = json.load(data)

valor = []

for i in dados:
    if i['valor'] != 0.0:
        valor.append(i['valor'])

min = min(valor)
max = max(valor)
soma = sum(valor)
media = soma / len(valor)
diasMaiorMedia = 0

for x in valor:
    if x > media:
        diasMaiorMedia += 1

print("O menor faturamento em um dia foi: {}".format(min))
print("O maior faturamento em um dia foi: {}".format(max))
print("O número de dias que o faturamento foi maior que média mensal foi: {}".format(diasMaiorMedia))