n = int(input("Digite um número para descobrir seu fatorial: "))
fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f'O fatorial desse número é {fatorial}')