#calculando uma média a partir de uma lista predefinida de temperaturas


temperaturas = [25, 18, 12, 22]
tamanho = len (temperaturas)
soma = 0
for t in temperaturas:
    soma += t
media = soma / tamanho
print (f"A média é : {media}.")



#calculando a média a partir de entradas do usuário


Temperaturas = []
while True:
    T = int ( input ("Digite uma temperatura:"))
    if T == 0:
        break
temperaturas. append(T)
tamanho = len(temperaturas)
soma = 0 
for T in temperaturas:
    soma += T
media = soma / tamanho
print (f"A média é: {media}.")

