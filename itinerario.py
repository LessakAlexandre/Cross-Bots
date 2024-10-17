def criarmatriz(tamanho):
    matriz = []
    for i in range(tamanho):
        vetor = []
        for j in range(tamanho):
            if j != i:    
                num = int(input(f'Distacia da cidade{i+1} para cidade {j+1}: '))
            else:
                num = 0
            vetor.append(num)
        matriz.append(vetor)
    print('Matriz Criada')
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'{matriz[i][j]}',end=' ')
            if j == len(matriz[0])-1:
                print()
    return matriz

def viagens(matriz):
    cidadePartida = distancia = 0
    viagem = cidadeChegada = 1

    while cidadeChegada != 0:
        cidadeChegada = -1
        while cidadeChegada > num or cidadeChegada < 0:
            cidadeChegada = int(input('Qual cidade deseja ir: '))
        print(f'{viagem}° viagem, distância: {matriz[cidadePartida][cidadeChegada]}')
        viagem+=1
        distancia += matriz[cidadePartida][cidadeChegada]
        cidadePartida = cidadeChegada
    print(f'total de percorrido {distancia}')


    


#---------------------------------------Pricipal--------------------#

num = int(input('Digite o quantas cidades estão no projeto: '))

matriz = criarmatriz(num)
viagens(matriz)
