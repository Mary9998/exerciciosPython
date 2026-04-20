notas = []
soma = 0
media = 0
nota = 0

while nota != -1:
    nota = float(input('Digite uma nota: '))
    if(nota != -1):
        notas.append(nota)
        soma += nota
        media = soma / len(notas)
print(soma)
print(media)

