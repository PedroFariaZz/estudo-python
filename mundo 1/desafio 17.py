import math
an = float(input('Digite o ângulo que você deseja:'))
se = math.sin(math.radians(an))
co = math.cos(math.radians(an))
ta = math.tan(math.radians(an))
print('O angulo de {} tem o SENO de {:.2F}'.format(an, se))
print(' O angulo de {} tem o COSSENO de {:.2F}'.format(an, co))
print(' O angulo de {} tem a TANGENTE de {:.2F}'.format(an, ta))