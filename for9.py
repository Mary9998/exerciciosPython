idades = []
novaIdade = 0

for i in range(0,7):
    novaIdade = int(input('Informe sua idade: '))
    idades.append(novaIdade)
    

for idade in idades:
    if(idade >= 18):
     print(f'você  é maior de idade')
    else: 
     print(f'Você não é maior de idade')