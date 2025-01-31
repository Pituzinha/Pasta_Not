#Lê um número e compara
x = int (input ("Digite um número:"))
if x > 100 :
    print ("Número maior que 100 !!!") 
print("Fim do Programa")

#Lê dois números e compara
x = int (input ("Digite um número: "))
y = int (input ("Digite um número: "))
if x > y:
    print ("O primeiro número é maior:")
if y > x:
    print ("O segundo número é maior: ")

#Verifica idades
a = int (input ("Digite a sua idade: "))
if a >= 18:
    print ("Você é maior de idade")
    print ("Já pode dirigir")
else:
    print ("Você é menor de idade")

#Faixa etária
a = int (input ("Digite a sua idade:"))
if a > 18:
    print ("Adulto")
else:
    if a >= 12:
        print ("Adolescente")
    else:
        print ("Criança")         

#Faixa etária
a = int (input ("Digite a sua idade:"))
if a > 18:
    print ("Adulto")
elif a >= 12:
    print ("Adolescente")
else:
    print ("Criança")

#Calcule o quanto um usuario gasta de energia baseada na faixa kwh e no preço por tipo de construção

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

