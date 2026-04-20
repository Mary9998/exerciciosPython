'''
a = 0  # Primeiro número
b = 1  # Segundo número

print(a)
print(b)

for i in range(10): # Gera os próximos 10 números
    proximo = a + b
    print(proximo)
    
    # A mágica da atualização:
    a = b        # 'a' recebe o valor do antigo 'b'
    b = proximo  # 'b' recebe o valor do novo número gerado
'''

a = 0
b = 1
i = 0
numero = int(input('Informe até o lugar vai a sequencia: '))

print(a)
print(b)
while True:

    if i >= numero - 2:
        break

    proximo = a + b
    print(proximo)
    a = b
    b = proximo

    i += 1

