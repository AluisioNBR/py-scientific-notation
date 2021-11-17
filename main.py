from time import sleep 

msgs = [
"""=========================================
     Conversor de Notação Científica
=========================================
""",

"""
Qual operação deseja realizar ?

1 - Notação científica >>>> Numérico
2 - Numérico >>>> Notação científica
3 - Sair

>>>>>>>>>> """,

"""
      OPÇÃO INVÁLIDA!!

Tente novamente..."""
]

print(msgs[0])

while True:
     op = int(input(msgs[1]))

     if op == 3:
          break

     elif op == 1:
          # Código...
          print()
     
     elif op == 2:
          # Código...
          print()

     else :
          print(msgs[2])

print("\nEncerrando...\n", end=""); sleep(3)