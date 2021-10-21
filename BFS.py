import queue

##El módulo queue implementa colas multi-productor y multi-consumidor.
#Es especialmente útil en la programación en hilo cuando la información debe intercambiarse de forma segura entre varios subprocesos. 
matriz = [
    ["3","2","1","3","*" ],
    ["3","#","0","3","3"],
    ["3","3","#","#","3"],
    ["3","3","3","2", "3" ],
]   


    #En la matrix de arriba se puede visualizar como ejemplo el mapa utilizado en el proyecto en donde
    #(3,0) es la posicion inicial, los numerales son los obstaculos  y la parte superior derecha es la meta
print(f"Matriz Inicial Amplitud : {matriz}")
    
rowLen = len(matriz)
colLen= len(matriz[0])
EMPTY = '3'
GOAL = '*'
FACEWHITE = '2'
DEER = "1"
frontier = queue.Queue()

def findStartPos(matriz):
    for row  in range(0,len(matriz)):
        for col in range(0,len(matriz[0])):
            if matriz[row][col]  == 0: 
                #print("Posicion: ",row," , ",col) 
                return (row,col)
    
    return (0,0) 

def BFS():
    currentValue = 0
    (startrow,startcol) = findStartPos(matriz)
    frontier.put([startrow,startcol])
    while frontier.not_empty:
        
        currentPosition =   frontier.get()
        row = currentPosition[0]
        col = currentPosition[1]
        
        if(col>0):
            if(matriz[row][col-1] == EMPTY):
                currentValue = currentValue 
                matriz[row][col-1] = currentValue
                frontier.put([row,col-1])
            elif(matriz[row][col-1] == FACEWHITE):
                currentValue = currentValue
                matriz[row][col-1] = currentValue
                frontier.put([row,col-1])
            elif(matriz[row][col-1] == DEER):
                currentValue = currentValue
                matriz[row][col-1] = currentValue
                frontier.put([row,col-1])
            elif ( matriz[row][col-1] == GOAL):
                currentValue = currentValue 
                matriz[row][col] = currentValue
                return currentValue

        if(row >0 ):
            if(matriz[row-1][col] == EMPTY):
                currentValue = currentValue 
                matriz[row-1][col] = currentValue
                frontier.put([row-1,col])
            elif(matriz[row-1][col] == FACEWHITE):
                currentValue = currentValue 
                matriz[row-1][col] = currentValue
                frontier.put([row-1,col])
            elif(matriz[row-1][col] == DEER):
                currentValue = currentValue 
                matriz[row-1][col] = currentValue
                frontier.put([row-1,col])
            elif ( matriz[row-1][col] == GOAL):
                currentValue = currentValue 
                matriz[row-1][col] = currentValue
                return currentValue

        if (col < colLen-1):
            if(matriz[row][col+1] == EMPTY):
                currentValue = currentValue 
                matriz[row][col+1] = currentValue
                frontier.put([row,col+1])
            elif(matriz[row][col+1] == FACEWHITE):
                currentValue = currentValue 
                matriz[row][col+1] = currentValue
                frontier.put([row,col+1])
            elif(matriz[row][col+1] == DEER):
                currentValue = currentValue 
                matriz[row][col+1] = currentValue
                frontier.put([row,col+1])
                
            elif ( matriz[row][col+1] == GOAL):
                currentValue = currentValue 
                matriz[row][col+1] = currentValue
                return currentValue

        if(row<rowLen-1):
            if(matriz[row+1][col] == EMPTY):
                currentValue = currentValue 
                matriz[row+1][col] = currentValue
                frontier.put([row+1,col])
            elif(matriz[row+1][col] == FACEWHITE):
                currentValue = currentValue 
                matriz[row+1][col] = currentValue
                frontier.put([row+1,col])
            elif(matriz[row+1][col] == DEER):
                currentValue = currentValue 
                matriz[row+1][col] = currentValue
                frontier.put([row+1,col])
                
            elif (matriz[row+1][col] == GOAL):
                currentValue = currentValue 
                matriz[row+1][col] = currentValue
                return currentValue


def main():
    lista_bfs=list()
    BFS()
    for items in matriz:
        rowString =''
        for item in items:
                rowString = rowString + str(item)

        # print(rowString)
        lista_bfs.append(rowString)
    return lista_bfs
    
if __name__ == "__main__":
    main()    