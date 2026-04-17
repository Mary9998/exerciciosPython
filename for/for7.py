soma = 0

for i in range(0, 6):
    num = int(input("Digite um numero inteiro: "))

    if (num % 2 ==0):
        soma += num
print(f"O valor da soma dos numeros pares é {soma}")

