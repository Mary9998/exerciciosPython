n = int(input('Informe um numero: '))
i = 0
soma = 0

while i < n:
    i += 1
    if i % 2 == 0:
        soma = soma + 1
print(f'Existe {soma} numeros pares até esse numero!')