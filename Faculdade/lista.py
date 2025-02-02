lista = [40, 20, 60,10]
valor = int(input("Qual número você quer buscar ?"))
achou = valor in lista
if achou :
    print ("Valor encontrado.") 
else:
    print ("Valor não encontrado.")
    

arroz = ["arroz", 5,8.5] 
feijão = ["feijão", 1,12.40]
print (arroz)
print (feijão)
compras = [arroz, feijão]
print (compras)
print (compras[0])
print (compras [1])
print (compras[0][2])
print (compras [1] [0])


arroz = ["arroz", 5, 8.50]
feijão = ["feijão", 1,12.40]
print(arroz)
print(feijão)
compras = [arroz, feijão]
for item in compras:
    print (f"Produto:{item[0]}")
    print (f"Quantidade:{item[1]}")
    print (f"Valor:{item[2]}")

#Alocação e varredura de elementos de uma matriz
linhas = 2
colunas = 2 
matriz = []
for l in range(linhas):
    linhas_aloc = [0] * colunas
    matriz.append (linhas_aloc)
for l in range (linhas):
    for c in range (colunas):
        print (f"Linhas {l}, Colunas: {c}")
