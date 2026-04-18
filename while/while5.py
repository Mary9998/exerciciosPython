n = int(input("Informe um numero para descobrir o seu fatorial: "))
fatorial = 1
auxiliar = n
while auxiliar > 1:
    print(f"Multiplicando {fatorial} por {auxiliar}")
    fatorial *= auxiliar
    auxiliar -= 1

print((fatorial))