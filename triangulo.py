#Fazer um programa para ler as medidas da base e altura de um triângulo. Em seguida, mostrar o valor
#da área, perímetro e diagonal deste triângulo, com quatro casas decimais.

base = float(input('Digite o valor da base do triângulo:'))
altura = float(input('Digite a altura do triângulo:'))
area = base * altura/2
perimetro = base + altura*2
diagonal = base**2 + altura**2
d = float(diagonal)**0.5

print (f'''Base = {base:.2f}
Altura = {altura:.2f}
''')

print (f'''A area do triângulo é igual a {area:.4f}.
O perímetro é igual a {perimetro:.4f}. 
A diagonal é igual a {d:.4f}.''')
