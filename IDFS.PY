import stack
import pygame
import sys
from pygame.draw import rect
from pygame.locals import *
# Caso 1
matriz = [
    ["3","2","1","3","*"],
    ["3","#","3","3","3"],
    ["3","3","#","#","3"],
    [0,"3","3","2","3"],
] 

# # #Caso 2
# matriz = [
#     ["3","2","1","3","*"],
#     ["3","#",0,"3","3"],
#     ["3","3","#","#","3"],
#     ["3","3","3","2","3"],
# ]   

print(f"Matriz Inicial Iterativa : {matriz}")

    
rowLen = len(matriz)
colLen= len(matriz[0])
EMPTY = '3'
BLOCKED = '#'
FACEWHITE = '2'
DEER = "1"
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
    for columna in range(len(matriz[0])):
        for fila in range(len(matriz)):
            if(matriz[fila - (columna % 2) * (fila + fila + 1)][columna] == 00):
                posicion = [fila,columna]

    return(posicion)


def IDFS(limit, currentPosition):
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
            if(matriz[row][col-1] == EMPTY):
                currentValue = currentValue
                matriz[row][col-1] = currentValue
                frontier.push([(row,col-1),currentDepth+1])
            elif(matriz[row][col-1] == FACEWHITE):
                # print("True - Fila 1 ",matriz[row][col-1])
                currentValue = currentValue
                matriz[row][col-1] = currentValue
                frontier.push([(row,col-1),currentDepth+1])
            elif(matriz[row][col-1] == DEER):
                # print("True - Fila 1 ",matriz[row][col-1])
                currentValue = currentValue
                matriz[row][col-1] = currentValue
                frontier.push([(row,col-1),currentDepth+1])
            elif ( matriz[row][col-1] == GOAL):
                currentValue = currentValue 
                matriz[row][col] = currentValue
                return (currentValue,True)
            elif ( matriz[row][col-1] != BLOCKED):
                frontier.push([(row,col-1),currentDepth+1])
            # print("---------------------------------------------------------------")
            # print("Limite: ",limit, " Fila: 1 ", " Coordenadas: ", row,",",col , " Casilla: ",matriz[row][col-1])  
            # print(matriz)

        if(row >0 ):
            if(matriz[row-1][col] == EMPTY):
                currentValue = currentValue 
                matriz[row-1][col] = currentValue
                frontier.push([(row-1,col),currentDepth+1])
            elif(matriz[row-1][col] == FACEWHITE):
                #print("True - Columna 1 ",matriz[row-1][col])
                currentValue = currentValue 
                matriz[row-1][col] = currentValue
                frontier.push([(row-1,col),currentDepth+1])
            elif(matriz[row-1][col] == DEER):
                # print("True - Columna 1 ",matriz[row-1][col])
                currentValue = currentValue 
                matriz[row-1][col] = currentValue
                frontier.push([(row-1,col),currentDepth+1])                 
            elif ( matriz[row-1][col] == GOAL):
                currentValue = currentValue 
                matriz[row-1][col] = currentValue
                return (currentValue,True)
            elif ( matriz[row-1][col] != BLOCKED):
                    frontier.push([(row-1,col),currentDepth+1])
            # print("---------------------------------------------------------------")
            # print("Limite: ",limit, " Colum: 1", " Coordenadas: ", row,",",col, " Casilla: ", matriz[row-1][col])  
            # print(matriz)


        if (col < colLen-1):
            if(matriz[row][col+1] == EMPTY):
                currentValue = currentValue 
                matriz[row][col+1] = currentValue
                frontier.push([(row,col+1),currentDepth+1])
            elif(matriz[row][col+1] == FACEWHITE):
                # print("True - Fila 2 ",matriz[row][col+1])
                currentValue = currentValue 
                matriz[row][col+1] = currentValue
                frontier.push([(row,col+1),currentDepth+1])
            elif(matriz[row][col+1] == DEER):
                # print("True - Fila 2 ",matriz[row][col+1])
                currentValue = currentValue 
                matriz[row][col+1] = currentValue
                frontier.push([(row,col+1),currentDepth+1])
            elif ( matriz[row][col+1] == GOAL):
                currentValue = currentValue 
                matriz[row][col+1] = currentValue
                return (currentValue,True)
            elif ( matriz[row][col+1] != BLOCKED):
                frontier.push([(row,col+1),currentDepth+1])

            # print("---------------------------------------------------------------")
            # print("Limite: ",limit, " Fila: 2", " Coordenadas: ", row,",",col, " Casilla: ", matriz[row][col+1])  
            # print(matriz)

        if(row<rowLen-1):
            if(matriz[row+1][col] == EMPTY):
                currentValue = currentValue 
                matriz[row+1][col] = currentValue
                frontier.push([(row+1,col),currentDepth+1])
            elif(matriz[row+1][col] == FACEWHITE):
                currentValue = currentValue 
                matriz[row+1][col] = currentValue
                frontier.push([(row+1,col),currentDepth+1])
            elif(matriz[row+1][col] == DEER):
                currentValue = currentValue 
                matriz[row+1][col] = currentValue
                frontier.push([(row+1,col),currentDepth+1])
            elif (matriz[row+1][col] == GOAL):
                currentValue = currentValue 
                matriz[row+1][col] = currentValue
                return (currentValue,True)
            elif ( matriz[row+1][col] != BLOCKED):
                frontier.push([(row+1,col),currentDepth+1])
            # print("---------------------------------------------------------------")
            # print("Limite: ",limit, " Colum: 2", " Coordenadas: ", row,",",col, " Casilla: ", matriz[row+1][col])  
            # print(matriz)
       
    return (currentPosition,False) 


def main():
    global startrow
    global startcol
    posicion = INIT()
    startrow = posicion[0]
    startcol = posicion[1]
    currentPosition =0  
    lista_terminal=list()
    for limit in range(1,(rowLen*colLen)):
        (currentPosition,ret) = IDFS(limit,currentPosition)
        #print("Elementos de current: ", currentPosition, " Ret: ", ret, " Limit: " , limit)
        if(ret):
            for items in matriz:
                rowString =''
                for item in items:
                      rowString = rowString + str(item) 
                lista_terminal.append(rowString)
                # print(rowString)

            return lista_terminal

   
        
if __name__ == "__main__":
    main()
   
