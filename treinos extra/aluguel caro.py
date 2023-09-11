# https://www.youtube.com/watch?v=H5I_U7wFQc8&t=19s

km = float(input('quantos km percorridos com o carro: '))
dias = int(input('quantos dias de aluguel: '))

km2 = km * 0.15
dias2 = dias * 60
preçodocarro = dias2 + km2

print('você tem que deverá pagar {}R$ pelo aluguel do carro'.format(preçodocarro))