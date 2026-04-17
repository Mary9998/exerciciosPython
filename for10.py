
somaMaiorIdade = 0
somaMenorIdade = 0

for i in range(0,7):
    idade = int(input('Informe sua idade: '))
    
    if(idade >= 18):
        somaMaiorIdade += 1
        
    else: 
        somaMenorIdade += 1
print(f'essa quantidade {somaMenorIdade} é menor idade')
print(f'essa quantidade {somaMaiorIdade} é maior idade')