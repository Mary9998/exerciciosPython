mes = int(input("Digite o número de um mês: "))

if mes in [1, 3, 5, 7, 8, 10, 12]:
    print("Esse mês tem 31 dias!")
elif mes in(4, 6, 9, 11):
    print("Esse mês possui 30 dias!")
elif(mes == 2):
    print("Esse mẽs possui 28 dias!")
else:
    print("Não há um mês com esse número")