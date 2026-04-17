#estrutura de repetição while
'''
for i in range(1,11):
    print(i)
print('Fim')
'''

'''
i = 1
while i <= 10:
    print(i)
    i += 1
print ('Fim!')
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um numero: '))
    if (n != 0):
        if (n % 2 == 0):
            par += 1
        else: 
            impar += 1
print(f"Vc digitou {par} numeros pares e {impar} numeros impares!" )


'''
r = "S"
while r == 'S':
    question = int(input('Informe um valor: '))
    r = str(input('Quer continuar? [S/N]: ').upper())
print('Fim')
'''