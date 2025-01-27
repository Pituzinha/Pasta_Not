print ("Olá, meu xuxuzinho!")
#Saudação
nome = input("Qual é o seu nome?")
print ("Então", nome ,"Seja muito bem vindo!")
#Calcular a idade
ano_nascimeto = int (input ("Digite o ano em que você nasceu:"))
ano_atual = int (input("Digite o ano atual:"))
idade = ano_atual - ano_nascimeto
print (f"Você tem ou fará {idade} anos de idade.")
#Formatação data de nascimento
dia = input ("Qual é o dia do seu nascimento?")
mes = input ("Qual o mês do seu nascimento?")
ano = input ("Qual é o ano do seu nascimento?")
data_nascimento = dia+ "/" +mes+ "/" +ano
print (f"Você nasceu no dia {dia}/{mes}/{ano}")

