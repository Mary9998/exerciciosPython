num = float(input("Informe um numero: "))
mult = 0

for i in range(1, 11):
    mult = num * i
    print(f'{num} x {i} = {mult}')
