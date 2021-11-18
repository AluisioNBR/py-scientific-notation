from os import system
from time import sleep 
from scientific_notation import notationTOnumber

msgs = [
"""
=========================================
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
====== Convertendo notações para números completos ======

Existem algumas formas de escrever sua notação, o recomendável é que sejam escritas nos formatos:

2.3*10²
3*10-²
4*-10²

Também é aceitável que sejam escritas nestes formatos:

2x10³
4.5x10-²
68X-10³
""",

"""
O sistema tolera alguns espaços, mas é recomendado que as notações sejam escritas sem eles para evitar possíveis erros. Ex:

50 * 10²
1890 x 10 -³
5 X -10²

O resultado pode não vir inteiro a depender do tamanho do número. Caso o número completo seja grande demais, o resultado pode chegar no formato:

2e+32
"""
]

system('clear')

while True:
     op = int(input(msgs[0]))
     system('clear')

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

          e = input('\nAperte Enter para prosseguir... ')
          system('clear')
          
          print(msgs[5])

     else :
          print(msgs[1])
     
     e = input('\nAperte Enter para prosseguir... ')
     system('clear')

print("\nEncerrando..."); sleep(3); system('clear')