from random import randint

def numero_aleatorio():
    
    a = randint(1,10)
    chute = 0
    
    while a != chute:
        chute = int(input("Digite um número de 1 a 10:"))
        
        if a == chute:
            print("Parabéns, você acertou!!")
        else:
            print("Tente novamente")
        
numero_aleatorio()
