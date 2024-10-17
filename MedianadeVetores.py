num = str(input('Digite os numeors: ')).strip()
vetor1 = (num.split(' '))
num = str(input('Digite o próximo vetor: ')).strip()
vetor2 = (num.split(' '))
mediana = []

for i in range(len(vetor1)):
    if vetor1[i] != '':
        vetor1[i] = int(vetor1[i])
        mediana.append(vetor1[i])
for c in range(len(vetor2)):
    if vetor2[c] != '':    
        vetor2[c] = int(vetor2[c])
        if vetor2[c] not in mediana:
            mediana.append(vetor2[c])
mediana.sort()
metade = len(mediana)//2
x = (mediana[metade-1]+mediana[metade])/2
if len(mediana) % 2 == 0:
    print('{}'.format(x))
else:
    print('{}'.format(mediana[metade]))
