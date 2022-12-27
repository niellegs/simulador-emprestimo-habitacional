print('\033[31m-=-\033[m'*15)
print('\033[33m SIMULADOR DE EMPRÉSTIMO \033[m')
print('\033[31m-=-\033[m'*15)
casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento?'))
mensal = casa / (anos * 12)
limite = salario * 0.30
if mensal < limite:
    print('Para pagar uma casa de R${:.2f} em {:.2f} anos a prestação será de R${:.2f}. Seu limite é {:.2f}. Empréstimo APROVADO! ' .format(casa, anos, mensal, limite))
elif mensal > limite:
    print('Para pagar uma casa de R${:.2f} em {:.2f} anos a prestação será de R${:.2f}. Seu limite é {:.2f}. Empréstimo NEGADO! ' .format(casa, anos, mensal, limite))
