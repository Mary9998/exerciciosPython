salario = float(input('Informe seu salário: '))

porcentagemMaior = 27.5
porcentagemMenor = 15

salarioMaior = salario * (porcentagemMaior / 100)
salarioMenor = salario * (porcentagemMenor / 100)

descontoFinalMaior = salarioMaior
descontoFinalMenor = salarioMenor

if(salario > 5000):
    print(f'Seu desconto é de {descontoFinalMaior}!')
elif(salario > 2000):
    print(f'Seu desconto é de {descontoFinalMenor}')
else:
    print('Você nn possui desconto')