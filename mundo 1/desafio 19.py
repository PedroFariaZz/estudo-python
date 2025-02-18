import random
n1 = str(input('Primeira pessoa:'))
n2 = str(input('Segunda pessoa:'))
n3 = str(input('Terceira pessoa:'))
n4 = str(input('Quarta pessoa:'))
lista = [n1, n2, n3, n4]
re = random.shuffle(lista)

print('A ordem da lista é:')
print(lista)
      
      