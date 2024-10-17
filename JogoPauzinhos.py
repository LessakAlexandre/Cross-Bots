from random import randint
palitos = randint(10,20)
print(f'Restam apenas {palitos} palitos')
while palitos > 0:
    num = vencedor = 0
    while num < 1 or num > 3:
        num = int(input('Digite quantos palitos pegar(1,2 ou 3): '))
    palitos -= num
    print(f'Restam apenas {palitos} palitos')
    print('Vez do Computador...')
    #----------------Computador------------------#
    if (palitos-3)%4 == 0 or palitos-3 == 0:
        palitos -= 3
    elif (palitos-2)%4 == 0 or palitos-2 ==0:
        palitos -=2
    elif (palitos-1)%4 == 0 or palitos-1 ==0: 
        palitos -=1
    elif palitos -3 >= 4:
        palitos -= 3
    elif palitos-2 >= 4:
        palitos -= 2
    elif palitos-1 >= 4:
        palitos -=1
    else:
        print('Eu desisto')
        vencedor = 1  
        break
    print(f'Restam apenas {palitos} palitos')
if vencedor == 0:
    print('Derrota')
else:    
    print('Muito bem jogador vc venceu este duelo')