caractere = input("Digite um caractere: ").lower()

if len(caractere) != 1:
    print("Digite apenas UM caractere")

else:
    if caractere.isalpha():
        if caractere in 'aeiou':
            print("Isso é uma vogal!")
        else:
            print("Isso é uma consoante!")
    else:
        print("Isso não é uma letra")
