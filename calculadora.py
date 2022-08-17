  #Desenvol uma calculadora rudimentar onde o usuário deve informar: qual operação ele deseja realizar, quais os valores para a realização do cálculo (apenas dois valores) e o resultado da operação solução



operações = input ('''
Digite qual operação gostaria de fazer: 
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')



a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))



#adição

if operações == '+':
    print ('{} + {}'.format(a,b))
    print (a+b)

#subtração
elif operações == "-":
  print('{} - {}'.format(a,b))
  print(a-b)

#multiplicação 
elif operações == "*":
  print('{}*{}'.format(a,b))
  print(a*b)

#divisão
elif operações == "/":
  print('{}/{}'.format(a,b))
  print(a/b)

else:
    print ("Por favor, escolha uma operação para calcular :)")
