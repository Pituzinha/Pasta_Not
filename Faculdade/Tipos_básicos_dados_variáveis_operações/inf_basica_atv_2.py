#utilizando a seguinte tabela de valores possiveis:
#Valor de A:             Valor de B:              Valor de C:          Valor de D:               Valor de E:
#- 1500                  - 50                     - 100                 - True                    - False
#- 500                   - 20                     - 21                  - True                    - True 
#- 2000                  - 30                     - 10                  - False                   - False

#Expressão:
#𝐴 > 1000  and 𝐵 < 𝐶  and 𝐷  or 𝐸

# Definição dos conjuntos de valores
valores = [
    {"A": 1500, "B": 50, "C": 100, "D": True, "E": False},
    {"A": 500, "B": 20, "C": 21, "D": True, "E": True},
    {"A": 2000, "B": 30, "C": 10, "D": False, "E": False},
]

# Expressão lógica aplicada a cada conjunto de valores
for i, v in enumerate(valores, 1):
    resultado = (v["A"] > 1000 and v["B"] < v["C"] and v["D"]) or v["E"]
    print(f"Conjunto {i}: {resultado}")
