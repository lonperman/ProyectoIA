import heapq

""" matriz = [
    ["[]","EL","VE","[]","*" ],
    ["[]","##",00,"[]","[]"],
    ["[]","[]","##","##","[]"],
    [ "[]","[]","[]","EL","[]" ],
] """   


""" matriz = [
    ["[]","EL","VE","[]",00],
    ["[]","##","[]","[]","[]"],
    ["[]","[]","##","##","[]"],
    [ "*","[]","[]","EL","[]" ],
] """   


matriz = [
    ["[]","EL","VE","[]","*" ],
    ["[]","##","[]","[]","[]"],
    ["[]","[]","##","##","[]"],
    [ 00,"[]","[]","EL","[]" ],
]

columnaLen = len(matriz)
filaLen= len(matriz[0])
EMPTY = '[]'
META = '*'
ELEMENTAL = "EL"
VENADO = "VE"
costo = 0

#Busca el punto de inicio donde debe arrancar el recorrido
def BusquedaPosicionInicial(matriz):
    for j  in range(0,len(matriz)):
        for i in range(0,len(matriz[0])):
            if matriz[j][i]  == 0:
                #print("PuntoInicio:", j, i)
                return (j,i)
    
    return (0,0)

def UCS():
    tienevenado = 0
    costoxmovimiento = 2
    heap = []
    (startj,starti) = BusquedaPosicionInicial(matriz)
    heapq.heappush(heap,(costo,tienevenado,(startj,starti)))
    while(len(heap) > 0):
        
        #Saca el de menor costo del arbol
        print("Heap:", heap)
        currentPosition = heapq.heappop(heap)
        currentcosto = currentPosition[0]
        currentcosto2 = currentPosition[0]
        currentcosto3 = currentPosition[0]
        currentcosto4 = currentPosition[0]
        j = currentPosition[2][0]
        print("j:", j)
        i = currentPosition[2][1]
        print("i:", i)
        tienevenado = currentPosition[1]

        #Se asegura de que si paso por un venado, cambio el costo de los elementales
        print("costo movimiento: ", currentPosition[1])
        if (currentPosition[1] == 1):
            costoxmovimiento = 1
        else: costoxmovimiento = 2

            
        if(i>0):
            print("entre al primer if i>0")
            if(matriz[j][i-1] == EMPTY):
                currentcosto = currentcosto + 1
                matriz[j][i-1] = currentcosto
                heapq.heappush(heap,(currentcosto,tienevenado,(j,i-1)))
                heapq.heapify(heap)
                #print(matriz) 
            
            elif(matriz[j][i-1] == ELEMENTAL):
                print("ENTRE AL VALIDADOR DEL ELEMENTAL1")
                currentcosto = currentcosto + costoxmovimiento
                matriz[j][i-1] = currentcosto
                heapq.heappush(heap,(currentcosto,tienevenado,(j,i-1)))
                heapq.heapify(heap)
                #print(matriz)

            elif(matriz[j][i-1] == VENADO):
                print("PASE POR UN VENADO1")
                currentcosto = currentcosto + 1
                matriz[j][i-1] = currentcosto
                tienevenado = 1
                heapq.heappush(heap,(currentcosto,tienevenado,(j,i-1)))
                heapq.heapify(heap)
                #print(matriz)
            
            elif ( matriz[j][i-1] == META):
                currentcosto = currentcosto + 1
                matriz[j][i] = currentcosto
                return tienevenado, currentcosto
                
        if(j >0 ):
            print("entre al segundo if j>0")
            if(matriz[j-1][i] == EMPTY):
                currentcosto2 = currentcosto2 + 1
                matriz[j-1][i] = currentcosto2
                heapq.heappush(heap,(currentcosto2,tienevenado,(j-1,i)))
                heapq.heapify(heap)
                
            
            elif(matriz[j-1][i] == ELEMENTAL):
                print("ENTRE AL VALIDADOR DEL ELEMENTAL2")
                currentcosto2 = currentcosto2 + costoxmovimiento
                matriz[j-1][i] = currentcosto2
                heapq.heappush(heap,(currentcosto2,tienevenado,(j-1,i)))
                heapq.heapify(heap)
                #print(matriz)

            elif(matriz[j-1][i] == VENADO):
                print("PASE POR UN VENADO2")
                currentcosto2 = currentcosto2 + 1
                matriz[j-1][i] = currentcosto2
                tienevenado = 1
                heapq.heappush(heap,(currentcosto2,tienevenado,(j-1,i)))
                heapq.heapify(heap)
                #print(matriz)
                
            elif ( matriz[j-1][i] == META):
                currentcosto2 = currentcosto2 + 1
                matriz[j-1][i] = currentcosto2
                return tienevenado, currentcosto2

        if (i < filaLen-1):
            print("entre al tercer if i>filaLen-1")
            if(matriz[j][i+1] == EMPTY):
                currentcosto3 = currentcosto3 + 1
                matriz[j][i+1] = currentcosto3
                heapq.heappush(heap,(currentcosto3,tienevenado,(j,i+1)))
                heapq.heapify(heap)
                #print(matriz)

            elif(matriz[j][i+1] == ELEMENTAL):
                print("ENTRE AL VALIDADOR DEL ELEMENTAL3")
                currentcosto3 = currentcosto3 + costoxmovimiento
                matriz[j][i+1] = currentcosto3
                print("aqui que hay tiene venado?: ",tienevenado)
                heapq.heappush(heap,(currentcosto3,tienevenado,(j,i+1)))
                heapq.heapify(heap)
                #print(matriz)

            elif(matriz[j][i+1] == VENADO):
                print("PASE POR UN VENADO3")
                currentcosto3 = currentcosto3 + 1
                matriz[j][i+1] = currentcosto3
                tienevenado = 1
                heapq.heappush(heap,(currentcosto3,tienevenado,(j,i+1)))
                heapq.heapify(heap)
                #print(matriz)
                
            elif ( matriz[j][i+1] == META):
                currentcosto3 = currentcosto3 + 1
                matriz[j][i+1] = currentcosto3
                return tienevenado, currentcosto3

        if(j<columnaLen-1):
            print("entre al cuarto if j>columnaLen-1")
            if(matriz[j+1][i] == EMPTY):
                currentcosto4 = currentcosto4 + 1
                matriz[j+1][i] = currentcosto4
                heapq.heappush(heap,(currentcosto4,tienevenado,(j+1,i)))
                heapq.heapify(heap)
                #print(matriz)

            elif(matriz[j+1][i] == ELEMENTAL):
                print("ENTRE AL VALIDADOR DEL ELEMENTAL4")
                currentcosto4 = currentcosto4 + costoxmovimiento
                matriz[j+1][i] = currentcosto4
                heapq.heappush(heap,(currentcosto4,tienevenado,(j+1,i)))
                heapq.heapify(heap)
                #print(matriz)

            elif(matriz[j+1][i] == VENADO):
                print("PASE POR UN VENADO4")
                currentcosto4 = currentcosto4 + 1
                matriz[j+1][i] = currentcosto4
                tienevenado = 1
                heapq.heappush(heap,(currentcosto4,tienevenado,(j+1,i)))
                heapq.heapify(heap)
                #print(matriz)
                
            elif (matriz[j+1][i] == META):
                currentcosto4 = currentcosto4 + 1
                matriz[j+1][i] = currentcosto4
                return  tienevenado, currentcosto4

def main():
    UCS()
    for items in matriz:
                jString =''
                for item in items:
                      jString = jString + str(item).zfill(2) + ' ' 

                print(jString)
        
        
if __name__ == "__main__":
    main()         

    