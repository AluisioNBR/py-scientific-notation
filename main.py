from time import sleep 
from scientific_notation import notationTOnumber

msgs = [
"""=========================================
     Conversor de Notação Científica
=========================================
""",

"""
Qual operação deseja realizar ?

1 - Notação científica >>>> Numérico
2 - Numérico >>>> Notação científica
3 - Como utilizar
4 - Sair

>>>>>>>>>> """,

"""
      OPÇÃO INVÁLIDA!!

Tente novamente...""",

"""
Informe a notação:
>>>>>>>>>> """
]

print(msgs[0])

while True:
     op = int(input(msgs[1]))

     if op == 4:
          break

     elif op == 1:
          # Código...
          print(msgs[3])
     
     elif op == 2:
          # Código...
          print()

     elif op == 3:
          # Código...
          print()

     else :
          print(msgs[2])

print("\nEncerrando...\n"); sleep(3)