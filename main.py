from os import system
from time import sleep 
from scientific_notation import notationTOnumber

msgs = [
"""=========================================
     Conversor de Notação Científica
=========================================

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
>>>>>>>>>> """,

"""
Informe o número
>>>>>>>>>> """,

"""
========== Convertendo notações para números completos ==========
"""
]

system('clear')

while True:
     op = int(input(msgs[0]))

     if op == 4:
          break

     elif op == 1:
          notation = input(msgs[2])
          result = notationTOnumber(notation)

          if result != None:
               print(f"\nO resultado é: {result}")
     
     elif op == 2:
          number = input(msgs[3])

     elif op == 3:
          print(msgs[4])

     else :
          print(msgs[1])
     
     e = input('\nAperte Enter para prosseguir... ')
     system('clear')

print("\nEncerrando..."); sleep(3); system('clear')