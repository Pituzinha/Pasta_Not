#utilizando a seguinte tabela de valores possiveis:
#Valor de A:             Valor de B:              Valor de C:          Valor de D:               Valor de E:
- 1500                  - 50                     - 100                 - True                    - False
- 500                   - 20                     - 21                  - True                    - True 
- 2000                  - 30                     - 10                  - False                   - False

Expressão:
𝐴 > 1000  and 𝐵 < 𝐶  and 𝐷  or 𝐸


(1500 > 1000 ) and (50 < 100 ) and ( 𝑇𝑟𝑢𝑒) or (𝐹𝑎𝑙𝑠𝑒)
1500 > 1000 → True
50 < 100 → True
True and True → True
True and True and True → True
True or False → True
✅ Resultado: True

(500>1000) and (20<21) and (True) or (True)
500 > 1000 → False
20 < 21 → True
False and True → False
False and True and True → False
False or True → True
✅ Resultado: True

(2000>1000) and (30<10) and (False) or (False)
2000 > 1000 → True
30 < 10 → False
True and False → False
False and False → False
False or False → False
✅ Resultado: False