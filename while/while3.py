import random
import time

secretNumber = random.randint(1,10)
attempts = 0

print("Eu estou pensando em um numero..")
time.sleep(2)

attempts = int(input("Adivinhe o numero que eu pensei: "))

while attempts != secretNumber:
    attempts = int(input("Tente de novo: "))

    if(attempts > secretNumber):
        print("Tente mais baixo..")
    elif(attempts < secretNumber):
        print("Tente maisn alto!")
print(f"Você acertou, o número é {secretNumber}!")