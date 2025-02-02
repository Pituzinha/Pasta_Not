#Calcule o quanto um usuario gasta de energia eletrica baseada na faixa kwh e no preço por tipo de construção (residencial,comercial, industrial).

kwh = int (input ("Digite os kwh:"))
tipo = input ("Qual é o tipo (R,C ou I):")
preco = 0.0
if tipo == "R":
    if kwh <= 500:
        preco = 0.40
    else:
        preco = 0.65
elif tipo == "C":
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.60
elif kwh <= 5000:
    if kwh <= 5000:
        preco = 0.55
else:
    preco = 0.60
valor = kwh * preco
print (f"O total a pagar é R$ {valor}.")

