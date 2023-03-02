#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.


sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
soma = sp + rj + mg + es + outros

spPercentual = sp / (soma / 100)
rjPercentual = rj / (soma / 100)
mgPercentual = mg / (soma / 100)
esPercentual = es / (soma / 100)
outrosPercentual = outros / (soma / 100)

print("A participação em percentual foi: SP - {}, RJ - {}, MG - {}, ES - {}, Outros - {}". format(round(spPercentual, 2), round(rjPercentual, 2), round(mgPercentual, 2), round(esPercentual, 2), round(outrosPercentual, 2)))