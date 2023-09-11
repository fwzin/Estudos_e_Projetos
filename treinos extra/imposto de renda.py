dinheiro = int(input('digite sua renda mensal: '))
if dinheiro > 10000:
        imps = dinheiro * 0.1
        multa = dinheiro * 0.15
        soma = imps + multa
        restante = dinheiro - soma
#       print ('valor do imposto:', imps, 'e da multa: ', multa, 'de acordo com a sua renda de', dinheiro, 'mensais')
        print ('de acordo com sua renda mensal de {}, vc terá que pagar um imposto no valor de: {} e uma multa de {}, restando {}'.format (dinheiro, imps, multa, restante))