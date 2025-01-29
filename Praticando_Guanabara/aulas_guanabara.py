#1 - Crie um script que leia o nome de uma pessoa e mostre uma mensagem de boas vindas de acordo com valores digitados. Qual é o seu nome? Olá, Gustavo! Prazer em conhece-ló.
nome = input ("Qual é o seu nome?")
print (f"Olá {nome} ! Prazer em conhece-ló") 

#2- Crie um script que leia dia, mês e ano de nascimento de uma pessoa e mostre uma mensagem com data formatada.
dia = input ("Qual é o dia do seu nascimento?")
mes = input ("Qual é o mês do seu nascimento?")
ano = input ("Qual é o ano do seu nascimento?")
data_nascimento = (f"{dia}/{mes}/{ano}")
print (f"Você nasceu em {data_nascimento}!")

#3 - Crie um script que leia dois números e mostre a soma entre eles.
n1 = input ("Digite um número:")
n2 = input ("Digite um número:")
n1 = int (n1)
n2 = int (n2)
soma = n1 + n2
print (f"A soma de {n1} e {n2} é a {soma}")

#Crie um progra que escreva Olá, mundo! na tela.
print ("Olá, mundo!")

#Faça um programa que leia o nome da pessoa e mostre uma mensagem de boas-vindas.
nome = input("Qual é o seu nome?")
print ("É um prazer em conhece-lo")

#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.
a= input("Digite algo:")
print (" O tipo primitivo desse valor é", type (a))
print ( "Só tem espaços?" a.isspace())
print ("É um número?" a.isnumeric())
print ("É um alfabetico?" a.isalpha())
print ("É um alfanumerico?" a.isalnum())
print ("Esta em maiuscula?" a.iseipper())
print ("Esta em minuscula?" a.islower())
print ("Esta  capitalizado?" a.istitle())

#5 - Faça um programa que leia um número  inteiro e mostre na tela o seu sucessor e o seu antecessor.
numero = int(input("Digite um número:"))
antecessor = numero - 1
sucessor = numero + 2
print (f"O antecessor de {numero} é {antecessor} e o seu sucessor é {sucessor}")

#6 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#7 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
nota 1 = float (input("Digite a nota"))
nota 2 = float (input ("Digite a nota"))
media = (nota 1 + nota 2) / 2 
print(f"A média do aluno é {media:.2f}")

#8 - Escreva um programa que leia o valor um metro e exiba convertido em centimetro e milimetro.
metros = float (input ("Digite o valor em metros"))
centimetros = metros * 100
milimetros = metros * 1000
print (f"{metros} metros equivalem a {centimetros:.of} centimetros e {milimetros:.of} ilimetros.")

#9 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
numero= int (input)("Digite um número:")
print (f"Tabuada do {numero}:.")
for i in range (1,11)
resultado = numero * 1
print (f"{numero} * {i} = {resultado}")

#10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ele pode comprar. Considere US$ 1.00 = R$ 3,27.
reais = float (input("Quanto de dinheiro você tem na carteira ?"))
taxa_cambio = 3,27
dolares = reais / taxa_cambio
print (f"com R$ {reais:.2f}, você pode comprar US$ {dolares:.2f}")

#11 - Faça um programa que leia a largura e altura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-lo, sabendo que cada litro de tinta pinta uma area de 2m².
largura = float (input("Digite a largura da parede (metros):"))
altura = float (input("Digite a altura da parede (metros):"))
area = largura * altura
litros_tinta = area / 2
print ("/n=== Resultado ===")

#12 - Faça algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#13 - Faça um algoritmo aue leia o sálario de um funcionario e mostre seu novo salario, com 15% de aumento.
