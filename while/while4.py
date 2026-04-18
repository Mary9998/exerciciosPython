
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

op = 0

while op != 5:
   print('''
    ---- MENU DE OPERAÇÕES ----
    [ 1 ] Somar Números
    [ 2 ] Multiplicar
    [ 3 ] maior numero
    [ 4 ] Novos numeros       
    [ 5 ] Sair do Programa
    ---------------------------
    ''')
   
   op = int(input('Informe a opçaõ acima: '))

   if op == 1:
      soma = valor1 + valor2
      print(f'''
 A soma dos valores {valor1} e {valor2} = {soma}
''')
      input('''
 Pressione ENTER para continuar..
            ''')
      
   elif op == 2:
      mult = valor1 * valor2
      print(f'''
 A multiplicação dos valores {valor1} e {valor2} = {mult}
''')
      input('''
 Pressione ENTER para continuar..
            ''')
      
   elif op == 3:
      if(valor1 > valor2):
         print(f"Valor {valor1} é maior que {valor2}")
      elif(valor2 > valor1):
         print(f'Valor {valor2} é maior que {valor1}')
      else:
         print('Os dois valores são iguais!')
