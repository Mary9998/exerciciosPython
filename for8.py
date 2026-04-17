frase = input("Digite uma frase: ").lower()

fraseLimpa = frase.replace(" ", "")
fraseInvertida = ""

for i in range(len(fraseLimpa) -1, -1, -1):
    fraseInvertida += fraseLimpa[i]
if (fraseLimpa == fraseInvertida):
    print('É um palíndromo')
else:
    print("Não é um palíndromo")
