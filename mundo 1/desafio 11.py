pre = float(input('Qual é o preço do produto?'))
des = pre - (pre*5 / 100) #<---------- entre paresenteses é considerado apenas o desconto, para parecer o valor real tem que colocar o valor ao lado.
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(pre,des))