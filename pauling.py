z = int(input("Digite o número eletrônico: "))

eletronsz = list()
diagrama = list()

config = list()

diagrama = ('1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d')
eletrons = (2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10)

for x in eletrons:
    while sum(eletronsz) < z:
        eletronsz.append(x)
        break
    
    
idx = len(eletronsz) - 1
if sum(eletronsz)> z:
    while sum(eletronsz)> z:
        eletronsz[idx] -= 1
        
diagramaz = diagrama [0:idx+1]


for x,y in zip(diagramaz, eletronsz):
    config.append(x + str(y))


print('Configuração eletronica:' , end= ' ')

for x in config:
    print(x, end=' ')
    
print(' ')
