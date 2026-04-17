mediaIdade = 0
totalIdade = 0
idades = []
listaUsuarios = []
maiorIdade = float('-inf')
usuarioMaisVelho = None
idadeFeminina = 0

class Usuario:
    def __init__(self, nome, idade, sex):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


for i in range(0,4):
    nome = input ('Informe seu nome: ')
    idade = int(input("Informe sua idade: "))
    sexo= input('Informe sua sexualidade (masculino/feminino): ').lower()
    idades.append(idade)

    novoUsuario = Usuario(nome, idade, sexo)
    listaUsuarios.append(novoUsuario)

    totalIdade += idade

mediaIdade = totalIdade / 4

for usuario in listaUsuarios:
    if(usuario.sexo == 'masculino'):
        if(usuario.idade > maiorIdade):
         maiorIdade = usuario.idade
         usuarioMaisVelho = usuario
    if(usuario.sexo == 'feminino'):
        if(usuario.idade < 20):
            idadeFeminina += 1
        
print(f'A media de todas as idades é {mediaIdade} anos')
if(usuarioMaisVelho):
    print(f'esse é o homem com a maior idade {usuarioMaisVelho.nome}! Com {usuarioMaisVelho.idade} anos')
else:
    print('Não há homens registrados.')

if(idadeFeminina):
    print(f"{idadeFeminina} mulheres tem menos de 20 anos!")
else:
    print('Tdas as mulheres na lista tem mais de 20 anos!')
