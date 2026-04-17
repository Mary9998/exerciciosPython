num = float(input("Informe sua idade: "))


if (num < 18):
    print("Você é menor de idade!")
elif (num >= 18 and num <= 60):
    print("Você é um adulto")
else:
    print("Você é idoso")