import queue

##El módulo queue implementa colas multi-productor y multi-consumidor.
#Es especialmente útil en la programación en hilo cuando la información debe intercambiarse de forma segura entre varios subprocesos. 
matriz = [
    ["[]","22","11","[]","*" ],
    ["[]","##","[]","[]","[]"],
    ["[]","[]","##","##","[]"],
    [00,"[]","[]","22", "[]" ],
]   


    #En la matrix de arriba se puede visualizar como ejemplo el mapa utilizado en el proyecto en donde
    #(3,0) es la posicion inicial, los numerales son los obstaculos  y la parte superior derecha es la meta

    
rowLen = len(matriz)
colLen= len(matriz[0])
EMPTY = '[]'
GOAL = '*'
FACEWHITE = '22'
DEER = "11"
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
    BFS()
    for items in matriz: 
                rowString =''
                for item in items:
                      rowString = rowString + str(item).zfill(2) + ' ' 

                print(rowString)
        
if __name__ == "__main__":
    main()    
        
