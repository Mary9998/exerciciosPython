pesoMaior = float('-inf')
pesoMenor = float('inf')


for i in range(1, 6):
    peso = float(input("Digite seu peso: "))

    if( peso > pesoMaior):
        pesoMaior = peso
    elif( peso < pesoMenor):
        pesoMenor = peso

print(f'O maior peso é {pesoMaior}')
print(f'O menor peso é {pesoMenor}')