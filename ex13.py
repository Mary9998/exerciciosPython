peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura (em metros): "))

imc = peso / (altura * altura)

if ( imc < 18.5):
    print("Abaixo do Peso")
elif(imc <= 24.9):
    print("Você está com o peso normal")
elif(imc <= 29.9):
    print("Você está com sobrepeso")
else:
    print("Você está obeso")