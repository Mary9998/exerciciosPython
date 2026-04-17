number_1 = int(input("Informe o primeiro numero: "))
number_2 = int(input("Informe o segundo numero: "))
operacao = input("Escolha uma operação ( +, -, *, /): ")

if operacao == '+':
    resultado = number_1 + number_2
    print(f"{number_1} + {number_2} = {resultado}")
elif (operacao == '-'):
    resultado = number_1 - number_2
    print(f"{number_1} - {number_2} = {resultado}")
elif operacao == '*':
    resultado = number_1 * number_2
    print(f"{number_1} * {number_2} = {resultado}")
elif operacao == '/':
    if number_2 != 0:
       resultado = number_1 / number_2 
       print(f"{number_1} / {number_2} = {resultado}")
    else:
        print("Não é possivel dividir por zero!")
else:
    print("Opção inválida!")