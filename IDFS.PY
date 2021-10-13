import stack
maze = [
    ["[]","[]","[]","[]","*" ],
    ["[]","##","[]","[]","[]"],
    ["[]","[]","##","##","[]"],
    ["[]","[]","[]","[]", 00 ],
]   



    
rowLen = len(maze)
colLen= len(maze[0])
EMPTY = '[]'
BLOCKED = '##'
GOAL = "*"






class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []
         
     def size(self):
         return len(self.items)    

     def push(self, item):
         self.items.append(item)
         

     def pop(self):
         return self.items.pop()

def INIT():
    for columna in range(len(maze[0])):
        for fila in range(len(maze)):
            if(maze[fila - (columna % 2) * (fila + fila + 1)][columna] == 00):
                posicion = [fila,columna]
                #print("Posicion: ", startrow, startcol)
            #else:
             #   print(maze[fila - (columna % 2) * (fila + fila + 1)][columna], end=" ")
            #print()

    
    return(posicion)


def IDFS(limit, currentPosition):
    #print("Posiciones IDFS: ", startrow,startcol)
    currentValue = 0
    currentDepth = 0
    frontier = Stack()
    frontier.push([(startrow,startcol),currentDepth])
    while (frontier.size()) != 0:
        
        currentPosition =   frontier.pop()
        row = currentPosition[0][0]
        col = currentPosition[0][1]
        currentDepth = currentPosition[1]
        if(currentDepth == limit):
            continue

        if(col>0):
            if(maze[row][col-1] == EMPTY):
                currentValue = currentValue
                maze[row][col-1] = currentValue
                frontier.push([(row,col-1),currentDepth+1])
            
            elif ( maze[row][col-1] == GOAL):
                currentValue = currentValue 
                maze[row][col] = currentValue
                return (currentValue,True)
            elif ( maze[row][col-1] != BLOCKED):
                frontier.push([(row,col-1),currentDepth+1])

        if(row >0 ):
            if(maze[row-1][col] == EMPTY):
                currentValue = currentValue 
                maze[row-1][col] = currentValue
                frontier.push([(row-1,col),currentDepth+1])           
            elif ( maze[row-1][col] == GOAL):
                currentValue = currentValue 
                maze[row-1][col] = currentValue
                return (currentValue,True)
            elif ( maze[row-1][col] != BLOCKED):
                    frontier.push([(row-1,col),currentDepth+1])

        if (col < colLen-1):
            if(maze[row][col+1] == EMPTY):
                currentValue = currentValue 
                maze[row][col+1] = currentValue
                frontier.push([(row,col+1),currentDepth+1])
            elif ( maze[row][col+1] == GOAL):
                currentValue = currentValue 
                maze[row][col+1] = currentValue
                return (currentValue,True)
            elif ( maze[row][col+1] != BLOCKED):
                frontier.push([(row,col+1),currentDepth+1])

        if(row<rowLen-1):
            if(maze[row+1][col] == EMPTY):
                currentValue = currentValue 
                maze[row+1][col] = currentValue
                frontier.push([(row+1,col),currentDepth+1])
            elif (maze[row+1][col] == GOAL):
                currentValue = currentValue 
                maze[row+1][col] = currentValue
                return (currentValue,True)
            elif ( maze[row+1][col] != BLOCKED):
                frontier.push([(row+1,col),currentDepth+1])
        print("Limite: ",limit)
        print("---------------------------------------------------------------")
        print(maze)
       
    return (currentPosition,False) 


def main():
    global startrow
    global startcol
    posicion = INIT()
    startrow = posicion[0]
    startcol = posicion[1]
    #print("Posiciones: ", startrow,startcol)
    currentPosition =0  
    for limit in range(1,(rowLen*colLen)):
        (currentPosition,ret) = IDFS(limit,currentPosition)
        #print("Elementos de current: ", currentPosition, " Ret: ", ret, " Limit: " , limit)
        if(ret):
            for items in maze:
                rowString =''
                for item in items:
                      rowString = rowString + str(item).zfill(2) + ' ' 

                print(rowString)

            return

        
        
if __name__ == "__main__":
    main()
   
        


   
        
