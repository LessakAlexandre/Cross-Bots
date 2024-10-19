num = str(input('Digite os numeros do primeiro vetor(separe somente com espaçoe): ')).strip()
vetor1 = (num.split(' '))
num = str(input('Digite o próximo vetor(separe somente com espaçoe)): ')).strip()
vetor2 = (num.split(' '))
mediana = []

for i in range(len(vetor1)):
    if vetor1[i] != '':
        vetor1[i] = int(vetor1[i])
        if vetor1[i] not in mediana:
            mediana.append(vetor1[i])
for c in range(len(vetor2)):
    if vetor2[c] != '':    
        vetor2[c] = int(vetor2[c])
        if vetor2[c] not in mediana:
            mediana.append(vetor2[c])
mediana.sort()
metade = len(mediana)//2
print(metade)
if len(mediana) % 2 == 0:
    print('A mediana encontrada para os vetores foi de {}'.format((mediana[metade-1]+mediana[metade])/2))
else:
    print('A mediana encontrada para os vetores foi de {}'.format(mediana[metade]))
print(mediana)
