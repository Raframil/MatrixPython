matrizA = [[0, 1, 4], [-3, 5, 7], [8, -2, 3]]

print ("Matriz A = ")
for r in matrizA:
    print(r)
print("")
matrizB = [[5, 3, 1], [-1, 4, 3], [7, 0, 2]]

print ("Matriz B = ")
for r in matrizB:
    print(r)

matrizC = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #matriz resultante inicializada com 0

print("")

#soma das matrizes A+B
for i in range(len(matrizA)):
    for j in range(len(matrizA[0])):
        matrizC[i][j] = matrizA[i][j] + matrizB[i][j]
print("A+B = ")

for r in matrizC:
    print(r)
#fim da soma A+B

print("")
print("A-2B = ")

# subtração A-2B
for i in range(len(matrizB)):
    for j in range(len(matrizB[0])):
        matrizB[i][j] = matrizB[i][j] * 2
        matrizC[i][j] = matrizA[i][j] -  matrizB[i][j]

for r in matrizC:
    print(r) 
#fim

print("") 
print("A*B = ")

#multiplicação A*B
matrizB = [[5, 3, 1], [-1, 4, 3], [7, 0, 2]]
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(matrizA)):
    for j in range(len(matrizB[0])):
        for k in range(len(matrizB)):
            result[i][j] += matrizA[i][k] * matrizB[k][j]
for r in result:
    print(r)
#fim

print("")

#A+Bt
X = [[5, 3, 1], [-1, 4, 3], [7, 0, 2]] #matriz B
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))] #transposta de B
for i in range(len(matrizA)):
    for j in range(len(matrizA[0])):
        matrizC[i][j] = matrizA[i][j] + result[i][j]

print("A+Bt = ")
for r in matrizC:
    print(r)
#fim A+Bt

print("")

#At-B
X = [[0, 1, 4], [-3, 5, 7], [8, -2, 3]] #matriz A
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))] #transposta de A
for i in range(len(matrizA)):
    for j in range(len(matrizA[0])):
        matrizC[i][j] = result[i][j] - matrizB[i][j]

print("At-B = ")
for r in matrizC:
    print(r)
#fim At-B


