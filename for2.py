n = int(input("Digite o incio da contagem: ")) 
f = int(input("Digite o final da contagem: "))
p = int(input("Digite o passo desa contagem: "))

for i in range(n, f+1, p):
    print(i)

s = 0
for i in range(0,3):
    n = int(input("Digite um numero: "))
    s += n

print(f"O somatório de todos os numeros foi {s}!")