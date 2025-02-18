import math
co = float(input('Comprimento do Cateto Oposto:'))
ca = float(input('Comprimento do Cateto Adjacente:'))
hi = math.hypot(co, ca)
print ('A hipotenusa é {}'.format(hi))
