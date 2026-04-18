s = input('Informe seu sexo [M/F]: ').upper().strip()
while s != 'M' and s != 'F':
    s = input('Sexo inválido! Digite novamente: ').upper().strip()
print("Muito bem!")