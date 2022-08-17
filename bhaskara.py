#Calculadora de bhaskara

a = float(input('Digite o coeficiente "a" da função de segundo grau:'))
b = float(input('Digite o coeficiente "b" da função de segundo grau:'))
c = float(input('Digite o coeficiente "c" da função de segundo grau:'))

delta = b**2 - 4 * a * c
raiz = float(delta) ** 0.5

if a == 0 or delta < 0:
    print ("Essa equação não possui raizes reais!")

else:
    x1 = -b + raiz/2*a
    x2 = -b - raiz/2*a
    print(f'o X1 é igual a {x1} e o X2 é igual a {x2}')
