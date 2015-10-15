matriz= [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
num = 3
print ("Enter numbers in array: ")
for i in range(len(matriz)):
    for j in range(len(matriz)):
        n = input("Numero :")
        matriz[i][j] = n + matriz[i][j]
        
        
print ("Matriz: ",matriz)