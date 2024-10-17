def criarmatriz(tamanho):
    matriz = []
    for i in range(tamanho):
        vetor = []
        for j in range(tamanho):
            num = int(input(f'Digite um número para a linha {i+1} e coluna {j+1}: '))
            vetor.append(num)
        matriz.append(vetor)
    print('Matriz Criada')
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(f'{matriz[i][j]}',end=' ')
            if j == len(matriz[0])-1:
                print()
    return matriz
def checagem():
    resultado = True
    for i in range(len(vetorL)):
        if vetorL[0] != vetorL[i]:
            resultado = False
        if vetorC[0] != vetorC[i]:
            resultado = False
    if vetorL[0] != vetorC[0]:
        resultado = False
    if vetorL[0] != diagonalP:
        resultado = False
    if vetorL[0] != diagonalS:
        resultado = False 
    return resultado
#------------------------------Variáveis------------------------------------#

tam = diagonalP = diagonalS= 0
vetorL = []
vetorC = []
#------------------------------Código Principal------------------------------#
while tam < 2 or tam > 10:
    tam = int(input('Digite a ordem do quadro magico: '))
matriz = criarmatriz(tam)

for i in range(len(matriz)):                           
    linha = 0
    coluna = 0
    for j in range(len(matriz[0])):
        linha += matriz[i][j]
        coluna += matriz[j][i]
        if i == j :
            diagonalP += matriz[i][j]
    diagonalS += matriz[i][len(matriz[0])-i-1]
    vetorL.append(linha)
    vetorC.append(coluna)

resultado = checagem()
if resultado == True:
    print('A matriz é um quadrado magico e a soma magica é: {}'.format(vetorC[0]))
else:
    print('a matriz não é um quadrado magico')


