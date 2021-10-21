import pygame
import sys
from pygame.draw import rect
from pygame.locals import *
from BFS import main as ampli
from UCS import main as costo_u
from IDFS import main as profu
from tkinter import *

matriz_bfs=ampli()
matriz_costo=costo_u()
root=Tk()

root.geometry('500x300')
root.title("Interfaz Recorridos")
root.resizable(0,0)
frame=Frame(root)
frame.pack()



def cambio_matriz(matriz):
    parte1=matriz[0]
    parte2=matriz[1]
    parte3=matriz[2]
    parte4=matriz[3]
    matriz=[]

    lista1=list(parte1)
    lista2=list(parte2)
    lista3=list(parte3)
    lista4=list(parte4)

    matriz.append(lista1)
    matriz.append(lista2)
    matriz.append(lista3)
    matriz.append(lista4)
    return matriz

def recorrrido_iterativa():
    

    matriz_recorrido=profu()
    
    ancho=500
    largo=400
    pygame.init()
    
    x=10
    y=10
    ventana=pygame.display.set_mode((ancho,largo))
    pygame.display.set_caption("Recorrido ITERATIVA")
    colorFondo=(255, 255, 255)

    monoke = pygame.image.load("monoke.png")
    ciervo = pygame.image.load("ciervo.png")
    carablanca = pygame.image.load("carablanca.png")
    monofeo = pygame.image.load("monofeo.png")

    monoke_t=pygame.transform.scale(monoke,(80,80))
    ciervo_t=pygame.transform.scale(ciervo,(80,80))
    cara_t=pygame.transform.scale(carablanca,(80,80))
    mono_t=pygame.transform.scale(monofeo,(80,80))

    colorfigura=(255 ,255 ,255)
    #variables movimiento
    velocidad=2
    direccion=True
    #COLOR LINEAS
    negro= (0,0,0)
    amarillo=(255,255,255)
    #DIBUJANDO LINEAS
    pygame.draw.line(ventana,colorfigura,(60,60),(120,60))
    while True:
        ventana.fill(colorFondo)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()


        #LINEAS HORIZONTALES
        pygame.draw.line(ventana,negro,(500,100),(0,100),5)
        pygame.draw.line(ventana,negro,(500,200),(0,200),5)
        pygame.draw.line(ventana,negro,(500,300),(0,300),5)
        #LINEAS VERTICALES
        pygame.draw.line(ventana,negro,(100,400),(100,0),5)
        pygame.draw.line(ventana,negro,(200,400),(200,0),5)
        pygame.draw.line(ventana,negro,(300,400),(300,0),5)
        pygame.draw.line(ventana,negro,(400,400),(400,0),5)
        pygame.draw.line(ventana,negro,(500,400),(500,0),5)
        
        #RECORRIDO PROFUNDIDAD
        for i,sublist in enumerate(cambio_matriz(matriz_recorrido)):
            for j,sublist in enumerate(sublist):

                if cambio_matriz(matriz_recorrido)[0][0]=="0":
                    ventana.blit(monoke_t,(x,y))
                else:
                    if cambio_matriz(matriz_recorrido)[0][0]=="3":
                        pygame.draw.rect(ventana,amarillo,(x,10,80,80))
                    if cambio_matriz(matriz_recorrido)[0][0]=="#":
                        pygame.draw.rect(ventana,negro,(x,y,80,80))
                    if cambio_matriz(matriz_recorrido)[0][0]=="2":
                        ventana.blit(ciervo_t,(x,y))
                    if cambio_matriz(matriz_recorrido)[0][0]=="1":
                        ventana.blit(ciervo_t,(x,y))
                    if cambio_matriz(matriz_recorrido)[0][0]=="2":
                        ventana.blit(cara_t,(x,y))
                    if cambio_matriz(matriz_recorrido)[0][0]=="*":
                        ventana.blit(mono_t,(x,y))


                if cambio_matriz(matriz_recorrido)[0][1]=="0":
                    ventana.blit(monoke_t,(x+100,y))

                else:
                    if cambio_matriz(matriz_recorrido)[0][1]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+100,y,80,80))
                    if cambio_matriz(matriz_recorrido)[0][1]=="#":
                        pygame.draw.rect(ventana,negro,(x+100,y,80,80))
                    if cambio_matriz(matriz_recorrido)[0][1]=="1":
                        ventana.blit(ciervo_t,(x+100,y))
                    if cambio_matriz(matriz_recorrido)[0][1]=="2":
                        ventana.blit(cara_t,(x+100,y))
                    if cambio_matriz(matriz_recorrido)[0][1]=="*":
                        ventana.blit(mono_t,(x+100,y))

                if cambio_matriz(matriz_recorrido)[0][2]=="0":
                    ventana.blit(monoke_t,(x+200,y))
                else:
                    if cambio_matriz(matriz_recorrido)[0][2]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+200,y,80,80))
                    if cambio_matriz(matriz_recorrido)[0][2]=="#":
                        pygame.draw.rect(ventana,negro,(x+200,y,80,80))
                    if cambio_matriz(matriz_recorrido)[0][2]=="1":
                        ventana.blit(ciervo_t,(x+200,y))
                    if cambio_matriz(matriz_recorrido)[0][2]=="2":
                        ventana.blit(cara_t,(x+200,y))
                    if cambio_matriz(matriz_recorrido)[0][2]=="*":
                        ventana.blit(mono_t,(x+200,y))


                if cambio_matriz(matriz_recorrido)[0][3]=="0":
                    ventana.blit(monoke_t,(x+300,y))
                else:
                    if cambio_matriz(matriz_recorrido)[0][3]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+300,y,80,80))
                    if cambio_matriz(matriz_recorrido)[0][3]=="#":
                        pygame.draw.rect(ventana,negro,(x+300,y,80,80))
                    if cambio_matriz(matriz_recorrido)[0][3]=="1":
                        ventana.blit(ciervo_t,(x+300,y))
                    if cambio_matriz(matriz_recorrido)[0][3]=="2":
                        ventana.blit(cara_t,(x+300,y))
                    if cambio_matriz(matriz_recorrido)[0][3]=="*":
                        ventana.blit(mono_t,(x+300,y))



                if cambio_matriz(matriz_recorrido)[0][4]=="0":
                    ventana.blit(monoke_t,(x+400,y))
                else:
                    if cambio_matriz(matriz_recorrido)[0][4]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+400,y,80,80))
                    if cambio_matriz(matriz_recorrido)[0][4]=="#":
                        pygame.draw.rect(ventana,negro,(x+400,y,80,80))
                    if cambio_matriz(matriz_recorrido)[0][4]=="1":
                        ventana.blit(ciervo_t,(x+400,y))
                    if cambio_matriz(matriz_recorrido)[0][4]=="2":
                        ventana.blit(cara_t,(x+400,y))
                    if cambio_matriz(matriz_recorrido)[0][4]=="*":
                        ventana.blit(mono_t,(x+400,y))



                if cambio_matriz(matriz_recorrido)[1][0]=="0":
                    ventana.blit(monoke_t,(x,y+100))
                else:
                    if cambio_matriz(matriz_recorrido)[1][0]=="3":
                        pygame.draw.rect(ventana,amarillo,(x,y+100,80,80))
                    if cambio_matriz(matriz_recorrido)[1][0]=="#":
                        pygame.draw.rect(ventana,negro,(x,y+100,80,80))
                    if cambio_matriz(matriz_recorrido)[1][0]=="1":
                        ventana.blit(ciervo_t,(x,y+100))
                    if cambio_matriz(matriz_recorrido)[1][0]=="2":
                        ventana.blit(cara_t,(x,y+100))
                    if cambio_matriz(matriz_recorrido)[1][0]=="*":
                        ventana.blit(mono_t,(x,y+100))


                if cambio_matriz(matriz_recorrido)[1][1]=="0":
                    ventana.blit(monoke_t,(x+100,y+100))
                else:
                    if cambio_matriz(matriz_recorrido)[1][1]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+100,y+100,80,80))
                    if cambio_matriz(matriz_recorrido)[1][1]=="#":
                        pygame.draw.rect(ventana,negro,(x+100,y+100,80,80))
                    if cambio_matriz(matriz_recorrido)[1][1]=="1":
                        ventana.blit(ciervo_t,(x+100,y+100))
                    if cambio_matriz(matriz_recorrido)[1][1]=="2":
                        ventana.blit(cara_t,(x+100,y+100))
                    if cambio_matriz(matriz_recorrido)[1][1]=="*":
                        ventana.blit(mono_t,(x+100,y+100))

                if cambio_matriz(matriz_recorrido)[1][2]=="0":
                    ventana.blit(monoke_t,(x+200,y+100))
                else:
                    if cambio_matriz(matriz_recorrido)[1][2]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+200,y+100,80,80))
                    if cambio_matriz(matriz_recorrido)[1][2]=="#":
                        pygame.draw.rect(ventana,negro,(x+200,y+100,80,80))
                    if cambio_matriz(matriz_recorrido)[1][2]=="1":
                        ventana.blit(ciervo_t,(x+200,y+100))
                    if cambio_matriz(matriz_recorrido)[1][2]=="2":
                        ventana.blit(cara_t,(x+200,y+100))
                    if cambio_matriz(matriz_recorrido)[1][2]=="*":
                        ventana.blit(mono_t,(x+200,y+100))





                if cambio_matriz(matriz_recorrido)[1][3]=="0":
                    ventana.blit(monoke_t,(x+300,y+100))
                else:
                    if cambio_matriz(matriz_recorrido)[1][3]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+300,y+100,80,80))
                    if cambio_matriz(matriz_recorrido)[1][3]=="#":
                        pygame.draw.rect(ventana,negro,(x+300,y+100,80,80))
                    if cambio_matriz(matriz_recorrido)[1][3]=="1":
                        ventana.blit(ciervo_t,(x+300,y+100))
                    if cambio_matriz(matriz_recorrido)[1][3]=="2":
                        ventana.blit(cara_t,(x+300,y+100))
                    if cambio_matriz(matriz_recorrido)[1][3]=="*":
                        ventana.blit(mono_t,(x+300,y+100))




                if cambio_matriz(matriz_recorrido)[1][4]=="0":
                        ventana.blit(monoke_t,(x+400,y+100))

                else:
                    if cambio_matriz(matriz_recorrido)[1][4]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+400,y+100,80,80))
                    if cambio_matriz(matriz_recorrido)[1][4]=="#":
                        pygame.draw.rect(ventana,negro,(x+400,y+100,80,80))
                    if cambio_matriz(matriz_recorrido)[1][4]=="1":
                        ventana.blit(ciervo_t,(x+400,y+100))
                    if cambio_matriz(matriz_recorrido)[1][4]=="2":
                        ventana.blit(cara_t,(x+400,y+100))
                    if cambio_matriz(matriz_recorrido)[1][4]=="*":
                        ventana.blit(mono_t,(x+400,y+100))


                if cambio_matriz(matriz_recorrido)[2][0]=="0":
                    ventana.blit(monoke_t,(x,y+200))
                else:
                    if cambio_matriz(matriz_recorrido)[2][0]=="3":
                        pygame.draw.rect(ventana,amarillo,(x,y+200,80,80))
                    if cambio_matriz(matriz_recorrido)[2][0]=="#":
                        pygame.draw.rect(ventana,negro,(x,y+200,80,80))
                    if cambio_matriz(matriz_recorrido)[2][0]=="1":
                        ventana.blit(ciervo_t,(x,y+200))
                    if cambio_matriz(matriz_recorrido)[2][0]=="2":
                        ventana.blit(cara_t,(x,y+200))
                    if cambio_matriz(matriz_recorrido)[2][0]=="*":
                        ventana.blit(mono_t,(x,y+200))

                if cambio_matriz(matriz_recorrido)[2][1]=="0":
                    ventana.blit(monoke_t,(x+100,y+200))
                else:
                    if cambio_matriz(matriz_recorrido)[2][1]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+100,y+200,80,80))
                    if cambio_matriz(matriz_recorrido)[2][1]=="#":
                        pygame.draw.rect(ventana,negro,(x+100,y+200,80,80))
                    if cambio_matriz(matriz_recorrido)[2][1]=="1":
                        ventana.blit(ciervo_t,(x+100,y+200))
                    if cambio_matriz(matriz_recorrido)[2][1]=="2":
                        ventana.blit(cara_t,(x+100,y+200))
                    if cambio_matriz(matriz_recorrido)[2][1]=="*":
                        ventana.blit(mono_t,(x+100,y+200))

                if cambio_matriz(matriz_recorrido)[2][2]=="0":
                    ventana.blit(monoke_t,(x+200,y+200))
                else:
                    if cambio_matriz(matriz_recorrido)[2][2]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+200,y+200,80,80))
                    if cambio_matriz(matriz_recorrido)[2][2]=="#":
                        pygame.draw.rect(ventana,negro,(x+200,y+200,80,80))
                    if cambio_matriz(matriz_recorrido)[2][2]=="1":
                        ventana.blit(ciervo_t,(x+200,y+200))
                    if cambio_matriz(matriz_recorrido)[2][2]=="2":
                        ventana.blit(cara_t,(x+200,y+200))
                    if cambio_matriz(matriz_recorrido)[2][2]=="*":
                        ventana.blit(mono_t,(x+200,y+200))


                if cambio_matriz(matriz_recorrido)[2][3]=="0":
                    ventana.blit(monoke_t,(x+300,y+200))
                else:
                    if cambio_matriz(matriz_recorrido)[2][3]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+300,y+200,80,80))
                    if cambio_matriz(matriz_recorrido)[2][3]=="#":
                        pygame.draw.rect(ventana,negro,(x+300,y+200,80,80))
                    if cambio_matriz(matriz_recorrido)[2][3]=="1":
                        ventana.blit(ciervo_t,(x+300,y+200))
                    if cambio_matriz(matriz_recorrido)[2][3]=="2":
                        ventana.blit(cara_t,(x+300,y+200))
                    if cambio_matriz(matriz_recorrido)[2][3]=="*":
                        ventana.blit(mono_t,(x+300,y+200))

                if cambio_matriz(matriz_recorrido)[2][4]=="0":
                    ventana.blit(monoke_t,(x+400,y+200))
                else:
                    if cambio_matriz(matriz_recorrido)[2][4]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+400,y+200,80,80))
                    if cambio_matriz(matriz_recorrido)[2][4]=="#":
                        pygame.draw.rect(ventana,negro,(x+400,y+200,80,80))
                    if cambio_matriz(matriz_recorrido)[2][4]=="1":
                        ventana.blit(ciervo_t,(x+400,y+200))
                    if cambio_matriz(matriz_recorrido)[2][4]=="2":
                        ventana.blit(cara_t,(x+400,y+200))
                    if cambio_matriz(matriz_recorrido)[2][4]=="*":
                        ventana.blit(mono_t,(x+400,y+200))

                if cambio_matriz(matriz_recorrido)[3][0]=="0":
                    ventana.blit(monoke_t,(x,y+300))
                else:
                    if cambio_matriz(matriz_recorrido)[3][0]=="3":
                        pygame.draw.rect(ventana,amarillo,(x,y+300,80,80))
                    if cambio_matriz(matriz_recorrido)[3][0]=="#":
                        pygame.draw.rect(ventana,negro,(x,y+300,80,80))
                    if cambio_matriz(matriz_recorrido)[3][0]=="1":
                        ventana.blit(ciervo_t,(x,y+300))
                    if cambio_matriz(matriz_recorrido)[3][0]=="2":
                        ventana.blit(cara_t,(x,y+300))
                    if cambio_matriz(matriz_recorrido)[3][0]=="*":
                        ventana.blit(mono_t,(x,y+300))

                if cambio_matriz(matriz_recorrido)[3][1]=="0":
                    ventana.blit(monoke_t,(x+100,y+300))
                else:
                    if cambio_matriz(matriz_recorrido)[3][1]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+100,y+300,80,80))
                    if cambio_matriz(matriz_recorrido)[3][1]=="#":
                        pygame.draw.rect(ventana,negro,(x+100,y+300,80,80))
                    if cambio_matriz(matriz_recorrido)[3][1]=="1":
                        ventana.blit(ciervo_t,(x+100,y+300))
                    if cambio_matriz(matriz_recorrido)[3][1]=="2":
                        ventana.blit(cara_t,(x+100,y+300))
                    if cambio_matriz(matriz_recorrido)[3][1]=="*":
                        ventana.blit(mono_t,(x+100,y+300))

                if cambio_matriz(matriz_recorrido)[3][2]=="0":
                    ventana.blit(monoke_t,(x+200,y+300))
                else:
                    if cambio_matriz(matriz_recorrido)[3][2]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+200,y+300,80,80))
                    if cambio_matriz(matriz_recorrido)[3][2]=="#":
                        pygame.draw.rect(ventana,negro,(x+200,y+300,80,80))
                    if cambio_matriz(matriz_recorrido)[3][2]=="1":
                        ventana.blit(ciervo_t,(x+200,y+300))
                    if cambio_matriz(matriz_recorrido)[3][2]=="2":
                        ventana.blit(cara_t,(x+200,y+300))
                    if cambio_matriz(matriz_recorrido)[3][2]=="*":
                        ventana.blit(mono_t,(x+200,y+300))

                if cambio_matriz(matriz_recorrido)[3][3]=="0":
                    ventana.blit(monoke_t,(x+300,y+300))
                else:
                    if cambio_matriz(matriz_recorrido)[3][3]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+300,y+300,80,80))
                    if cambio_matriz(matriz_recorrido)[3][3]=="#":
                        pygame.draw.rect(ventana,negro,(x+300,y+300,80,80))
                    if cambio_matriz(matriz_recorrido)[3][3]=="1":
                        ventana.blit(ciervo_t,(x+300,y+300))
                    if cambio_matriz(matriz_recorrido)[3][3]=="2":
                        ventana.blit(cara_t,(x+300,y+300))
                    if cambio_matriz(matriz_recorrido)[3][3]=="*":
                        ventana.blit(mono_t,(x+300,y+300))


                if cambio_matriz(matriz_recorrido)[3][4]=="0":
                    ventana.blit(monoke_t,(x+400,y+300))
                else:
                    if cambio_matriz(matriz_recorrido)[3][4]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+400,y+300,80,80))
                    if cambio_matriz(matriz_recorrido)[3][4]=="#":
                        pygame.draw.rect(ventana,negro,(x+400,y+300,80,80))

                    if cambio_matriz(matriz_recorrido)[3][4]=="1":
                        ventana.blit(ciervo_t,(x+400,y+300))
                    if cambio_matriz(matriz_recorrido)[3][4]=="2":
                        ventana.blit(cara_t,(x+400,y+300))
                    if cambio_matriz(matriz_recorrido)[3][4]=="*":
                        ventana.blit(mono_t,(x+400,y+300))

        pygame.display.update()


def recorrido_amplitud():
    ancho=500
    largo=400
    pygame.init()
    ventana=pygame.display.set_mode((ancho,largo))
    pygame.display.set_caption("Recorrido AMPLITUD")
    colorFondo=(255, 255, 255)

    monoke = pygame.image.load("monoke.png")
    ciervo = pygame.image.load("ciervo.png")
    carablanca = pygame.image.load("carablanca.png")
    monofeo = pygame.image.load("monofeo.png")

    monoke_t=pygame.transform.scale(monoke,(80,80))
    ciervo_t=pygame.transform.scale(ciervo,(80,80))
    cara_t=pygame.transform.scale(carablanca,(80,80))
    mono_t=pygame.transform.scale(monofeo,(80,80))

    colorfigura=(255 ,255 ,255)
    #variables movimiento
    x=10
    y=10
    #COLOR LINEAS
    negro= (0,0,0)
    amarillo=(255,255,255)
    #DIBUJANDO LINEAS
    pygame.draw.line(ventana,colorfigura,(60,60),(120,60))
    fuente=pygame.font.Font(None,20)

    while True:
        ventana.fill(colorFondo)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        #LINEAS HORIZONTALES
        pygame.draw.line(ventana,negro,(500,100),(0,100),5)
        pygame.draw.line(ventana,negro,(500,200),(0,200),5)
        pygame.draw.line(ventana,negro,(500,300),(0,300),5)
        #LINEAS VERTICALES
        pygame.draw.line(ventana,negro,(100,400),(100,0),5)
        pygame.draw.line(ventana,negro,(200,400),(200,0),5)
        pygame.draw.line(ventana,negro,(300,400),(300,0),5)
        pygame.draw.line(ventana,negro,(400,400),(400,0),5)
        pygame.draw.line(ventana,negro,(500,400),(500,0),5)

        for i,sublist in enumerate(cambio_matriz(matriz_bfs)):
            for j ,sublist in enumerate(sublist):

                if cambio_matriz(matriz_bfs)[0][0]=="0":
                    ventana.blit(monoke_t,(x,y))
                else:
                    if cambio_matriz(matriz_bfs)[0][0]=="3":
                        pygame.draw.rect(ventana,colorfigura,(x,10,80,80))
                    if cambio_matriz(matriz_bfs)[0][0]=="#":
                        pygame.draw.rect(ventana,negro,(x,y,80,80))
                    if cambio_matriz(matriz_bfs)[0][0]=="1":
                        ventana.blit(ciervo_t,(x,y))
                    if cambio_matriz(matriz_bfs)[0][0]=="2":
                        ventana.blit(cara_t,(x,y))
                    if cambio_matriz(matriz_bfs)[0][0]=="*":
                        ventana.blit(mono_t,(x,y))


                if cambio_matriz(matriz_bfs)[0][1]=="0":
                    ventana.blit(monoke_t,(x+100,y))

                else:
                    if cambio_matriz(matriz_bfs)[0][1]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+100,y,80,80))
                    if cambio_matriz(matriz_bfs)[0][1]=="#":
                        pygame.draw.rect(ventana,negro,(x+100,y,80,80))
                    if cambio_matriz(matriz_bfs)[0][1]=="1":
                        ventana.blit(ciervo_t,(x+100,y))
                    if cambio_matriz(matriz_bfs)[0][1]=="2":
                        ventana.blit(cara_t,(x+100,y))
                    if cambio_matriz(matriz_bfs)[0][1]=="*":
                        ventana.blit(mono_t,(x+100,y))

                if cambio_matriz(matriz_bfs)[0][2]=="0":
                    ventana.blit(monoke_t,(x+200,y))
                else:
                    if cambio_matriz(matriz_bfs)[0][2]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+200,y,80,80))
                    if cambio_matriz(matriz_bfs)[0][2]=="#":
                        pygame.draw.rect(ventana,negro,(x+200,y,80,80))
                    if cambio_matriz(matriz_bfs)[0][2]=="1":
                        ventana.blit(ciervo_t,(x+200,y))
                    if cambio_matriz(matriz_bfs)[0][2]=="2":
                        ventana.blit(cara_t,(x+200,y))
                    if cambio_matriz(matriz_bfs)[0][2]=="*":
                        ventana.blit(mono_t,(x+200,y))


                if cambio_matriz(matriz_bfs)[0][3]=="0":
                    ventana.blit(monoke_t,(x+300,y))
                else:
                    if cambio_matriz(matriz_bfs)[0][3]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+300,y,80,80))
                    if cambio_matriz(matriz_bfs)[0][3]=="#":
                        pygame.draw.rect(ventana,negro,(x+300,y,80,80))
                    if cambio_matriz(matriz_bfs)[0][3]=="1":
                        ventana.blit(ciervo_t,(x+300,y))
                    if cambio_matriz(matriz_bfs)[0][3]=="2":
                        ventana.blit(cara_t,(x+300,y))
                    if cambio_matriz(matriz_bfs)[0][3]=="*":
                        ventana.blit(mono_t,(x+300,y))



                if cambio_matriz(matriz_bfs)[0][4]=="0":
                    ventana.blit(monoke_t,(x+400,y))
                else:
                    if cambio_matriz(matriz_bfs)[0][4]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+400,y,80,80))
                    if cambio_matriz(matriz_bfs)[0][4]=="#":
                        pygame.draw.rect(ventana,negro,(x+400,y,80,80))
                    if cambio_matriz(matriz_bfs)[0][4]=="1":
                        ventana.blit(ciervo_t,(x+400,y))
                    if cambio_matriz(matriz_bfs)[0][4]=="2":
                        ventana.blit(cara_t,(x+400,y))
                    if cambio_matriz(matriz_bfs)[0][4]=="*":
                        ventana.blit(mono_t,(x+400,y))



                if cambio_matriz(matriz_bfs)[1][0]=="0":
                    ventana.blit(monoke_t,(x,y+100))
                else:
                    if cambio_matriz(matriz_bfs)[1][0]=="3":
                        pygame.draw.rect(ventana,amarillo,(x,y+100,80,80))
                    if cambio_matriz(matriz_bfs)[1][0]=="#":
                        pygame.draw.rect(ventana,negro,(x,y+100,80,80))
                    if cambio_matriz(matriz_bfs)[1][0]=="1":
                        ventana.blit(ciervo_t,(x,y+100))
                    if cambio_matriz(matriz_bfs)[1][0]=="2":
                        ventana.blit(cara_t,(x,y+100))
                    if cambio_matriz(matriz_bfs)[1][0]=="*":
                        ventana.blit(mono_t,(x,y+100))


                if cambio_matriz(matriz_bfs)[1][1]=="0":
                    ventana.blit(monoke_t,(x+100,y+100))
                else:
                    if cambio_matriz(matriz_bfs)[1][1]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+100,y+100,80,80))
                    if cambio_matriz(matriz_bfs)[1][1]=="#":
                        pygame.draw.rect(ventana,negro,(x+100,y+100,80,80))
                    if cambio_matriz(matriz_bfs)[1][1]=="1":
                        ventana.blit(ciervo_t,(x+100,y+100))
                    if cambio_matriz(matriz_bfs)[1][1]=="2":
                        ventana.blit(cara_t,(x+100,y+100))
                    if cambio_matriz(matriz_bfs)[1][1]=="*":
                        ventana.blit(mono_t,(x+100,y+100))

                if cambio_matriz(matriz_bfs)[1][2]=="0":
                    ventana.blit(monoke_t,(x+200,y+100))
                else:
                    if cambio_matriz(matriz_bfs)[1][2]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+200,y+100,80,80))
                    if cambio_matriz(matriz_bfs)[1][2]=="#":
                        pygame.draw.rect(ventana,negro,(x+200,y+100,80,80))
                    if cambio_matriz(matriz_bfs)[1][2]=="1":
                        ventana.blit(ciervo_t,(x+200,y+100))
                    if cambio_matriz(matriz_bfs)[1][2]=="2":
                        ventana.blit(cara_t,(x+200,y+100))
                    if cambio_matriz(matriz_bfs)[1][2]=="*":
                        ventana.blit(mono_t,(x+200,y+100))





                if cambio_matriz(matriz_bfs)[1][3]=="0":
                    ventana.blit(monoke_t,(x+300,y+100))
                else:
                    if cambio_matriz(matriz_bfs)[1][3]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+300,y+100,80,80))
                    if cambio_matriz(matriz_bfs)[1][3]=="#":
                        pygame.draw.rect(ventana,negro,(x+300,y+100,80,80))
                    if cambio_matriz(matriz_bfs)[1][3]=="1":
                        ventana.blit(ciervo_t,(x+300,y+100))
                    if cambio_matriz(matriz_bfs)[1][3]=="2":
                        ventana.blit(cara_t,(x+300,y+100))
                    if cambio_matriz(matriz_bfs)[1][3]=="*":
                        ventana.blit(mono_t,(x+300,y+100))




                if cambio_matriz(matriz_bfs)[1][4]=="0":
                        ventana.blit(monoke_t,(x+400,y+100))

                else:
                    if cambio_matriz(matriz_bfs)[1][4]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+400,y+100,80,80))
                    if cambio_matriz(matriz_bfs)[1][4]=="#":
                        pygame.draw.rect(ventana,negro,(x+400,y+100,80,80))
                    if cambio_matriz(matriz_bfs)[1][4]=="1":
                        ventana.blit(ciervo_t,(x+400,y+100))
                    if cambio_matriz(matriz_bfs)[1][4]=="2":
                        ventana.blit(cara_t,(x+400,y+100))
                    if cambio_matriz(matriz_bfs)[1][4]=="*":
                        ventana.blit(mono_t,(x+400,y+100))


                if cambio_matriz(matriz_bfs)[2][0]=="0":
                    ventana.blit(monoke_t,(x,y+200))
                else:
                    if cambio_matriz(matriz_bfs)[2][0]=="3":
                        pygame.draw.rect(ventana,amarillo,(x,y+200,80,80))
                    if cambio_matriz(matriz_bfs)[2][0]=="#":
                        pygame.draw.rect(ventana,negro,(x,y+200,80,80))
                    if cambio_matriz(matriz_bfs)[2][0]=="1":
                        ventana.blit(ciervo_t,(x,y+200))
                    if cambio_matriz(matriz_bfs)[2][0]=="2":
                        ventana.blit(cara_t,(x,y+200))
                    if cambio_matriz(matriz_bfs)[2][0]=="*":
                        ventana.blit(mono_t,(x,y+200))

                if cambio_matriz(matriz_bfs)[2][1]=="0":
                    ventana.blit(monoke_t,(x+100,y+200))
                else:
                    if cambio_matriz(matriz_bfs)[2][1]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+100,y+200,80,80))
                    if cambio_matriz(matriz_bfs)[2][1]=="#":
                        pygame.draw.rect(ventana,negro,(x+100,y+200,80,80))
                    if cambio_matriz(matriz_bfs)[2][1]=="1":
                        ventana.blit(ciervo_t,(x+100,y+200))
                    if cambio_matriz(matriz_bfs)[2][1]=="2":
                        ventana.blit(cara_t,(x+100,y+200))
                    if cambio_matriz(matriz_bfs)[2][1]=="*":
                        ventana.blit(mono_t,(x+100,y+200))

                if cambio_matriz(matriz_bfs)[2][2]=="0":
                    ventana.blit(monoke_t,(x+200,y+200))
                else:
                    if cambio_matriz(matriz_bfs)[2][2]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+200,y+200,80,80))
                    if cambio_matriz(matriz_bfs)[2][2]=="#":
                        pygame.draw.rect(ventana,negro,(x+200,y+200,80,80))
                    if cambio_matriz(matriz_bfs)[2][2]=="1":
                        ventana.blit(ciervo_t,(x+200,y+200))
                    if cambio_matriz(matriz_bfs)[2][2]=="2":
                        ventana.blit(cara_t,(x+200,y+200))
                    if cambio_matriz(matriz_bfs)[2][2]=="*":
                        ventana.blit(mono_t,(x+200,y+200))


                if cambio_matriz(matriz_bfs)[2][3]=="0":
                    ventana.blit(monoke_t,(x+300,y+200))
                else:
                    if cambio_matriz(matriz_bfs)[2][3]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+300,y+200,80,80))
                    if cambio_matriz(matriz_bfs)[2][3]=="#":
                        pygame.draw.rect(ventana,negro,(x+300,y+200,80,80))
                    if cambio_matriz(matriz_bfs)[2][3]=="1":
                        ventana.blit(ciervo_t,(x+300,y+200))
                    if cambio_matriz(matriz_bfs)[2][3]=="2":
                        ventana.blit(cara_t,(x+300,y+200))
                    if cambio_matriz(matriz_bfs)[2][3]=="*":
                        ventana.blit(mono_t,(x+300,y+200))

                if cambio_matriz(matriz_bfs)[2][4]=="0":
                    ventana.blit(monoke_t,(x+400,y+200))
                else:
                    if cambio_matriz(matriz_bfs)[2][4]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+400,y+200,80,80))
                    if cambio_matriz(matriz_bfs)[2][4]=="#":
                        pygame.draw.rect(ventana,negro,(x+400,y+200,80,80))
                    if cambio_matriz(matriz_bfs)[2][4]=="1":
                        ventana.blit(ciervo_t,(x+400,y+200))
                    if cambio_matriz(matriz_bfs)[2][4]=="2":
                        ventana.blit(cara_t,(x+400,y+200))
                    if cambio_matriz(matriz_bfs)[2][4]=="*":
                        ventana.blit(mono_t,(x+400,y+200))

                if cambio_matriz(matriz_bfs)[3][0]=="0":
                    ventana.blit(monoke_t,(x,y+300))
                else:
                    if cambio_matriz(matriz_bfs)[3][0]=="3":
                        pygame.draw.rect(ventana,amarillo,(x,y+300,80,80))
                    if cambio_matriz(matriz_bfs)[3][0]=="#":
                        pygame.draw.rect(ventana,negro,(x,y+300,80,80))
                    if cambio_matriz(matriz_bfs)[3][0]=="1":
                        ventana.blit(ciervo_t,(x,y+300))
                    if cambio_matriz(matriz_bfs)[3][0]=="2":
                        ventana.blit(cara_t,(x,y+300))
                    if cambio_matriz(matriz_bfs)[3][0]=="*":
                        ventana.blit(mono_t,(x,y+300))

                if cambio_matriz(matriz_bfs)[3][1]=="0":
                    ventana.blit(monoke_t,(x+100,y+300))
                else:
                    if cambio_matriz(matriz_bfs)[3][1]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+100,y+300,80,80))
                    if cambio_matriz(matriz_bfs)[3][1]=="#":
                        pygame.draw.rect(ventana,negro,(x+100,y+300,80,80))
                    if cambio_matriz(matriz_bfs)[3][1]=="1":
                        ventana.blit(ciervo_t,(x+100,y+300))
                    if cambio_matriz(matriz_bfs)[3][1]=="2":
                        ventana.blit(cara_t,(x+100,y+300))
                    if cambio_matriz(matriz_bfs)[3][1]=="*":
                        ventana.blit(mono_t,(x+100,y+300))

                if cambio_matriz(matriz_bfs)[3][2]=="0":
                    ventana.blit(monoke_t,(x+200,y+300))
                else:
                    if cambio_matriz(matriz_bfs)[3][2]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+200,y+300,80,80))
                    if cambio_matriz(matriz_bfs)[3][2]=="#":
                        pygame.draw.rect(ventana,negro,(x+200,y+300,80,80))
                    if cambio_matriz(matriz_bfs)[3][2]=="1":
                        ventana.blit(ciervo_t,(x+200,y+300))
                    if cambio_matriz(matriz_bfs)[3][2]=="2":
                        ventana.blit(cara_t,(x+200,y+300))
                    if cambio_matriz(matriz_bfs)[3][2]=="*":
                        ventana.blit(mono_t,(x+200,y+300))

                if cambio_matriz(matriz_bfs)[3][3]=="0":
                    ventana.blit(monoke_t,(x+300,y+300))
                else:
                    if cambio_matriz(matriz_bfs)[3][3]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+300,y+300,80,80))
                    if cambio_matriz(matriz_bfs)[3][3]=="#":
                        pygame.draw.rect(ventana,negro,(x+300,y+300,80,80))
                    if cambio_matriz(matriz_bfs)[3][3]=="1":
                        ventana.blit(ciervo_t,(x+300,y+300))
                    if cambio_matriz(matriz_bfs)[3][3]=="2":
                        ventana.blit(cara_t,(x+300,y+300))
                    if cambio_matriz(matriz_bfs)[3][3]=="*":
                        ventana.blit(mono_t,(x+300,y+300))


                if cambio_matriz(matriz_bfs)[3][4]=="0":
                    ventana.blit(monoke_t,(x+400,y+300))
                else:
                    if cambio_matriz(matriz_bfs)[3][4]=="3":
                        pygame.draw.rect(ventana,amarillo,(x+400,y+300,80,80))
                    if cambio_matriz(matriz_bfs)[3][4]=="#":
                        pygame.draw.rect(ventana,negro,(x+400,y+300,80,80))

                    if cambio_matriz(matriz_bfs)[3][4]=="1":
                        ventana.blit(ciervo_t,(x+400,y+300))
                    if cambio_matriz(matriz_bfs)[3][4]=="2":
                        ventana.blit(cara_t,(x+400,y+300))
                    if cambio_matriz(matriz_bfs)[3][4]=="*":
                        ventana.blit(mono_t,(x+400,y+300))


        pygame.display.update()


def recorrido_costo():

    ancho=500
    largo=400
    pygame.init()
    ventana=pygame.display.set_mode((ancho,largo))
    pygame.display.set_caption("Recorrido COSTO UNIFORME")
    colorFondo=(255, 255, 255)

    monoke = pygame.image.load("monoke.png")
    ciervo = pygame.image.load("ciervo.png")
    carablanca = pygame.image.load("carablanca.png")
    monofeo = pygame.image.load("monofeo.png")

    monoke_t=pygame.transform.scale(monoke,(80,80))
    ciervo_t=pygame.transform.scale(ciervo,(80,80))
    cara_t=pygame.transform.scale(carablanca,(80,80))
    mono_t=pygame.transform.scale(monofeo,(80,80))

    colorfigura=(255 ,255 ,255)
    #variables movimiento
    x=10
    y=10
    #COLOR LINEAS
    negro= (0,0,0)
    amarillo=(255,255,0)
    #DIBUJANDO LINEAS
    pygame.draw.line(ventana,colorfigura,(60,60),(120,60))
    fuente=pygame.font.Font(None,30)

    while True:
        ventana.fill(colorFondo)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()   
        
        #LINEAS HORIZONTALES
        pygame.draw.line(ventana,negro,(500,100),(0,100),5)
        pygame.draw.line(ventana,negro,(500,200),(0,200),5)
        pygame.draw.line(ventana,negro,(500,300),(0,300),5)
        #LINEAS VERTICALES
        pygame.draw.line(ventana,negro,(100,400),(100,0),5)
        pygame.draw.line(ventana,negro,(200,400),(200,0),5)
        pygame.draw.line(ventana,negro,(300,400),(300,0),5)
        pygame.draw.line(ventana,negro,(400,400),(400,0),5)
        pygame.draw.line(ventana,negro,(500,400),(500,0),5)
        for i, sublist in enumerate(cambio_matriz(matriz_costo)):
            for j , sublist in enumerate(sublist):
                
                if cambio_matriz(matriz_costo)[0][0]=="0":
                        ventana.blit(monoke_t,(x,y)) 
                if cambio_matriz(matriz_costo)[0][0]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x,10,80,80))
                if cambio_matriz(matriz_costo)[0][0]=="#":
                    pygame.draw.rect(ventana,negro,(x,y,80,80))
                if cambio_matriz(matriz_costo)[0][0]=="1":
                    ventana.blit(ciervo_t,(x,y))
                if cambio_matriz(matriz_costo)[0][0]=="/":
                    ventana.blit(cara_t,(x,y))
                if cambio_matriz(matriz_costo)[0][0]=="*":
                    ventana.blit(mono_t,(x,y))
                if cambio_matriz(matriz_costo)[0][0]!="0" and cambio_matriz(matriz_costo)[0][0]!="e" and cambio_matriz(matriz_costo)[0][0]!="#" and cambio_matriz(matriz_costo)[0][0]!="d" and cambio_matriz(matriz_costo)[0][0]!="/" and cambio_matriz(matriz_costo)[0][0]!="*":
                    text=cambio_matriz(matriz_costo)[0][0]
                    ventana.blit(monoke_t,(x,y))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x, y))

                if cambio_matriz(matriz_costo)[0][1]=="0":
                        ventana.blit(monoke_t,(x+100,y)) 
                if cambio_matriz(matriz_costo)[0][1]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+100,10,80,80))
                if cambio_matriz(matriz_costo)[0][1]=="#":
                    pygame.draw.rect(ventana,negro,(x+100,y,80,80))
                if cambio_matriz(matriz_costo)[0][1]=="d":
                    ventana.blit(ciervo_t,(x+100,y))
                if cambio_matriz(matriz_costo)[0][1]=="/":
                    ventana.blit(cara_t,(x+100,y))
                if cambio_matriz(matriz_costo)[0][1]=="*":
                    ventana.blit(mono_t,(x+100,y))
                if cambio_matriz(matriz_costo)[0][1]!="0" and cambio_matriz(matriz_costo)[0][1]!="e" and cambio_matriz(matriz_costo)[0][1]!="#" and cambio_matriz(matriz_costo)[0][1]!="d" and cambio_matriz(matriz_costo)[0][1]!="/" and cambio_matriz(matriz_costo)[0][1]!="*":
                    text=cambio_matriz(matriz_costo)[0][1]
                    ventana.blit(monoke_t,(x+100,y))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+100, y))

                if cambio_matriz(matriz_costo)[0][2]=="0":
                        ventana.blit(monoke_t,(x+200,y)) 
                if cambio_matriz(matriz_costo)[0][2]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+200,10,80,80))
                if cambio_matriz(matriz_costo)[0][2]=="#":
                    pygame.draw.rect(ventana,negro,(x+200,y,80,80))
                if cambio_matriz(matriz_costo)[0][2]=="d":
                    ventana.blit(ciervo_t,(x+200,y))
                if cambio_matriz(matriz_costo)[0][2]=="/":
                    ventana.blit(cara_t,(x+200,y))
                if cambio_matriz(matriz_costo)[0][2]=="*":
                    ventana.blit(mono_t,(x+200,y))
                if cambio_matriz(matriz_costo)[0][2]!="0" and cambio_matriz(matriz_costo)[0][2]!="e" and cambio_matriz(matriz_costo)[0][2]!="#" and cambio_matriz(matriz_costo)[0][2]!="d" and cambio_matriz(matriz_costo)[0][2]!="/" and cambio_matriz(matriz_costo)[0][2]!="*":
                    text=cambio_matriz(matriz_costo)[0][2]
                    ventana.blit(monoke_t,(x+200,y))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+200, y))

                if cambio_matriz(matriz_costo)[0][3]=="0":
                        ventana.blit(monoke_t,(x+300,y)) 
                if cambio_matriz(matriz_costo)[0][3]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+300,10,80,80))
                if cambio_matriz(matriz_costo)[0][3]=="#":
                    pygame.draw.rect(ventana,negro,(x+300,y,80,80))
                if cambio_matriz(matriz_costo)[0][3]=="d":
                    ventana.blit(ciervo_t,(x+300,y))
                if cambio_matriz(matriz_costo)[0][3]=="/":
                    ventana.blit(cara_t,(x+300,y))
                if cambio_matriz(matriz_costo)[0][3]=="*":
                    ventana.blit(mono_t,(x+300,y))
                if cambio_matriz(matriz_costo)[0][3]!="0" and cambio_matriz(matriz_costo)[0][3]!="e" and cambio_matriz(matriz_costo)[0][3]!="#" and cambio_matriz(matriz_costo)[0][3]!="d" and cambio_matriz(matriz_costo)[0][3]!="/" and cambio_matriz(matriz_costo)[0][3]!="*":
                    text=cambio_matriz(matriz_costo)[0][3]
                    ventana.blit(monoke_t,(x+300,y))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+300, y))


                if cambio_matriz(matriz_costo)[0][4]=="0":
                        ventana.blit(monoke_t,(x+400,y)) 
                if cambio_matriz(matriz_costo)[0][4]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+400,10,80,80))
                if cambio_matriz(matriz_costo)[0][4]=="#":
                    pygame.draw.rect(ventana,negro,(x+400,y,80,80))
                if cambio_matriz(matriz_costo)[0][4]=="d":
                    ventana.blit(ciervo_t,(x+400,y))
                if cambio_matriz(matriz_costo)[0][4]=="/":
                    ventana.blit(cara_t,(x+400,y))
                if cambio_matriz(matriz_costo)[0][4]=="*":
                    ventana.blit(mono_t,(x+400,y))
                if cambio_matriz(matriz_costo)[0][4]!="0" and cambio_matriz(matriz_costo)[0][4]!="e" and cambio_matriz(matriz_costo)[0][4]!="#" and cambio_matriz(matriz_costo)[0][4]!="d" and cambio_matriz(matriz_costo)[0][4]!="/" and cambio_matriz(matriz_costo)[0][4]!="*":
                    text=cambio_matriz(matriz_costo)[0][4]
                    ventana.blit(monoke_t,(x+400,y))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+400,y))


                if cambio_matriz(matriz_costo)[1][0]=="0":
                        ventana.blit(monoke_t,(x,y+100)) 
                if cambio_matriz(matriz_costo)[1][0]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x,y+100,80,80))
                if cambio_matriz(matriz_costo)[1][0]=="#":
                    pygame.draw.rect(ventana,negro,(x,y+100,80,80))
                if cambio_matriz(matriz_costo)[1][0]=="d":
                    ventana.blit(ciervo_t,(x,y+100))
                if cambio_matriz(matriz_costo)[1][0]=="/":
                    ventana.blit(cara_t,(x,y+100))
                if cambio_matriz(matriz_costo)[1][0]=="*":
                    ventana.blit(mono_t,(x,y+100))
                if cambio_matriz(matriz_costo)[1][0]!="0" and cambio_matriz(matriz_costo)[1][0]!="e" and cambio_matriz(matriz_costo)[1][0]!="#" and cambio_matriz(matriz_costo)[1][0]!="d" and cambio_matriz(matriz_costo)[1][0]!="/" and cambio_matriz(matriz_costo)[1][0]!="*":
                    text=cambio_matriz(matriz_costo)[1][0]
                    ventana.blit(monoke_t,(x,y+100))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x,y+100))


                if cambio_matriz(matriz_costo)[1][1]=="0":
                        ventana.blit(monoke_t,(x+100,y+100)) 
                if cambio_matriz(matriz_costo)[1][1]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+100,y+100,80,80))
                if cambio_matriz(matriz_costo)[1][1]=="#":
                    pygame.draw.rect(ventana,negro,(x+100,y+100,80,80))
                if cambio_matriz(matriz_costo)[1][1]=="d":
                    ventana.blit(ciervo_t,(x+100,y+100))
                if cambio_matriz(matriz_costo)[1][1]=="/":
                    ventana.blit(cara_t,(x+100,y+100))
                if cambio_matriz(matriz_costo)[1][1]=="*":
                    ventana.blit(mono_t,(x+100,y+100))
            
                if cambio_matriz(matriz_costo)[1][1]!="0" and cambio_matriz(matriz_costo)[1][1]!="e" and cambio_matriz(matriz_costo)[1][1]!="#" and cambio_matriz(matriz_costo)[1][1]!="d" and cambio_matriz(matriz_costo)[1][1]!="2" and cambio_matriz(matriz_costo)[1][1]!="*":
                    text=cambio_matriz(matriz_costo)[1][1]
                    ventana.blit(monoke_t,(x+100,y+100))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+100,y+100))

                if cambio_matriz(matriz_costo)[1][2]=="0":
                        ventana.blit(monoke_t,(x+200,y+100)) 
                if cambio_matriz(matriz_costo)[1][2]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+200,y+100,80,80))
                if cambio_matriz(matriz_costo)[1][2]=="#":
                    pygame.draw.rect(ventana,negro,(x+200,y+100,80,80))
                if cambio_matriz(matriz_costo)[1][2]=="d":
                    ventana.blit(ciervo_t,(x+200,y+100))
                if cambio_matriz(matriz_costo)[1][2]=="/":
                    ventana.blit(cara_t,(x+200,y+100))
                if cambio_matriz(matriz_costo)[1][2]=="*":
                    ventana.blit(mono_t,(x+200,y+100))
            
                if cambio_matriz(matriz_costo)[1][2]!="0" and cambio_matriz(matriz_costo)[1][2]!="e" and cambio_matriz(matriz_costo)[1][2]!="#" and cambio_matriz(matriz_costo)[1][2]!="d" and cambio_matriz(matriz_costo)[1][2]!="2" and cambio_matriz(matriz_costo)[1][2]!="*":
                    text=cambio_matriz(matriz_costo)[1][2]
                    ventana.blit(monoke_t,(x+200,y+100))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+200,y+100))


                if cambio_matriz(matriz_costo)[1][3]=="0":
                        ventana.blit(monoke_t,(x+300,y+100)) 
                if cambio_matriz(matriz_costo)[1][3]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+300,y+100,80,80))
                if cambio_matriz(matriz_costo)[1][3]=="#":
                    pygame.draw.rect(ventana,negro,(x+300,y+100,80,80))
                if cambio_matriz(matriz_costo)[1][3]=="d":
                    ventana.blit(ciervo_t,(x+300,y+100))
                if cambio_matriz(matriz_costo)[1][3]=="/":
                    ventana.blit(cara_t,(x+300,y+100))
                if cambio_matriz(matriz_costo)[1][3]=="*":
                    ventana.blit(mono_t,(x+300,y+100))
            
                if cambio_matriz(matriz_costo)[1][3]!="0" and cambio_matriz(matriz_costo)[1][3]!="e" and cambio_matriz(matriz_costo)[1][3]!="#" and cambio_matriz(matriz_costo)[1][3]!="d" and cambio_matriz(matriz_costo)[1][3]!="2" and cambio_matriz(matriz_costo)[1][3]!="*":
                    text=cambio_matriz(matriz_costo)[1][3]
                    ventana.blit(monoke_t,(x+300,y+100))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+300,y+100))



                if cambio_matriz(matriz_costo)[1][4]=="0":
                        ventana.blit(monoke_t,(x+400,y+100)) 
                if cambio_matriz(matriz_costo)[1][4]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+400,y+100,80,80))
                if cambio_matriz(matriz_costo)[1][4]=="#":
                    pygame.draw.rect(ventana,negro,(x+400,y+100,80,80))
                if cambio_matriz(matriz_costo)[1][4]=="d":
                    ventana.blit(ciervo_t,(x+400,y+100))
                if cambio_matriz(matriz_costo)[1][4]=="/":
                    ventana.blit(cara_t,(x+400,y+100))
                if cambio_matriz(matriz_costo)[1][4]=="*":
                    ventana.blit(mono_t,(x+400,y+100))
            
                if cambio_matriz(matriz_costo)[1][4]!="0" and cambio_matriz(matriz_costo)[1][4]!="e" and cambio_matriz(matriz_costo)[1][4]!="#" and cambio_matriz(matriz_costo)[1][4]!="d" and cambio_matriz(matriz_costo)[1][4]!="2" and cambio_matriz(matriz_costo)[1][4]!="*":
                    text=cambio_matriz(matriz_costo)[1][4]
                    ventana.blit(monoke_t,(x+400,y+100))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+400,y+100))




                if cambio_matriz(matriz_costo)[2][0]=="0":
                        ventana.blit(monoke_t,(x,y+200)) 
                if cambio_matriz(matriz_costo)[2][0]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x,y+200,80,80))
                if cambio_matriz(matriz_costo)[2][0]=="#":
                    pygame.draw.rect(ventana,negro,(x,y+200,80,80))
                if cambio_matriz(matriz_costo)[2][0]=="d":
                    ventana.blit(ciervo_t,(x,y+200))
                if cambio_matriz(matriz_costo)[2][0]=="/":
                    ventana.blit(cara_t,(x,y+200))
                if cambio_matriz(matriz_costo)[2][0]=="*":
                    ventana.blit(mono_t,(x,y+200))
                if cambio_matriz(matriz_costo)[2][0]!="0" and cambio_matriz(matriz_costo)[2][0]!="e" and cambio_matriz(matriz_costo)[2][0]!="#" and cambio_matriz(matriz_costo)[2][0]!="d" and cambio_matriz(matriz_costo)[2][0]!="/" and cambio_matriz(matriz_costo)[2][0]!="*":
                    text=cambio_matriz(matriz_costo)[2][0]
                    ventana.blit(monoke_t,(x,y+200))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x,y+200))



                if cambio_matriz(matriz_costo)[2][1]=="0":
                        ventana.blit(monoke_t,(x+100,y+200)) 
                if cambio_matriz(matriz_costo)[2][1]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+100,y+200,80,80))
                if cambio_matriz(matriz_costo)[2][1]=="#":
                    pygame.draw.rect(ventana,negro,(x+100,y+200,80,80))
                if cambio_matriz(matriz_costo)[2][1]=="d":
                    ventana.blit(ciervo_t,(x+100,y+200))
                if cambio_matriz(matriz_costo)[2][1]=="/":
                    ventana.blit(cara_t,(x+100,y+200))
                if cambio_matriz(matriz_costo)[2][1]=="*":
                    ventana.blit(mono_t,(x+100,y+200))
                if cambio_matriz(matriz_costo)[2][1]!="0" and cambio_matriz(matriz_costo)[2][1]!="e" and cambio_matriz(matriz_costo)[2][1]!="#" and cambio_matriz(matriz_costo)[2][1]!="d" and cambio_matriz(matriz_costo)[2][1]!="/" and cambio_matriz(matriz_costo)[2][1]!="*":
                    text=cambio_matriz(matriz_costo)[2][1]
                    ventana.blit(monoke_t,(x+100,y+200))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+100,y+200))


                if cambio_matriz(matriz_costo)[2][2]=="0":
                        ventana.blit(monoke_t,(x+200,y+200)) 
                if cambio_matriz(matriz_costo)[2][2]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+200,y+200,80,80))
                if cambio_matriz(matriz_costo)[2][2]=="#":
                    pygame.draw.rect(ventana,negro,(x+200,y+200,80,80))
                if cambio_matriz(matriz_costo)[2][2]=="d":
                    ventana.blit(ciervo_t,(x+200,y+200))
                if cambio_matriz(matriz_costo)[2][2]=="/":
                    ventana.blit(cara_t,(x+200,y+200))
                if cambio_matriz(matriz_costo)[2][2]=="*":
                    ventana.blit(mono_t,(x+200,y+200))
                if cambio_matriz(matriz_costo)[2][2]!="0" and cambio_matriz(matriz_costo)[2][2]!="e" and cambio_matriz(matriz_costo)[2][2]!="#" and cambio_matriz(matriz_costo)[2][2]!="d" and cambio_matriz(matriz_costo)[2][2]!="/" and cambio_matriz(matriz_costo)[2][2]!="*":
                    text=cambio_matriz(matriz_costo)[2][2]
                    ventana.blit(monoke_t,(x+200,y+200))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+200,y+200))

                if cambio_matriz(matriz_costo)[2][3]=="0":
                        ventana.blit(monoke_t,(x+300,y+200)) 
                if cambio_matriz(matriz_costo)[2][3]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+300,y+200,80,80))
                if cambio_matriz(matriz_costo)[2][3]=="#":
                    pygame.draw.rect(ventana,negro,(x+300,y+200,80,80))
                if cambio_matriz(matriz_costo)[2][3]=="d":
                    ventana.blit(ciervo_t,(x+300,y+200))
                if cambio_matriz(matriz_costo)[2][3]=="/":
                    ventana.blit(cara_t,(x+300,y+200))
                if cambio_matriz(matriz_costo)[2][3]=="*":
                    ventana.blit(mono_t,(x+300,y+200))
                if cambio_matriz(matriz_costo)[2][3]!="0" and cambio_matriz(matriz_costo)[2][3]!="e" and cambio_matriz(matriz_costo)[2][3]!="#" and cambio_matriz(matriz_costo)[2][3]!="d" and cambio_matriz(matriz_costo)[2][3]!="/" and cambio_matriz(matriz_costo)[2][3]!="*":
                    text=cambio_matriz(matriz_costo)[2][3]
                    ventana.blit(monoke_t,(x+300,y+200))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+300,y+200))


                if cambio_matriz(matriz_costo)[2][4]=="0":
                        ventana.blit(monoke_t,(x+400,y+200)) 
                if cambio_matriz(matriz_costo)[2][4]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+400,y+200,80,80))
                if cambio_matriz(matriz_costo)[2][4]=="#":
                    pygame.draw.rect(ventana,negro,(x+400,y+200,80,80))
                if cambio_matriz(matriz_costo)[2][4]=="d":
                    ventana.blit(ciervo_t,(x+400,y+200))
                if cambio_matriz(matriz_costo)[2][4]=="/":
                    ventana.blit(cara_t,(x+400,y+200))
                if cambio_matriz(matriz_costo)[2][4]=="*":
                    ventana.blit(mono_t,(x+400,y+200))
                if cambio_matriz(matriz_costo)[2][4]!="0" and cambio_matriz(matriz_costo)[2][4]!="e" and cambio_matriz(matriz_costo)[2][4]!="#" and cambio_matriz(matriz_costo)[2][4]!="d" and cambio_matriz(matriz_costo)[2][4]!="/" and cambio_matriz(matriz_costo)[2][4]!="*":
                    text=cambio_matriz(matriz_costo)[2][4]
                    ventana.blit(monoke_t,(x+400,y+200))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+400,y+200))


                if cambio_matriz(matriz_costo)[3][0]=="0":
                        ventana.blit(monoke_t,(x,y+300)) 
                if cambio_matriz(matriz_costo)[3][0]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x,y+300,80,80))
                if cambio_matriz(matriz_costo)[3][0]=="#":
                    pygame.draw.rect(ventana,negro,(x,y+300,80,80))
                if cambio_matriz(matriz_costo)[3][0]=="d":
                    ventana.blit(ciervo_t,(x,y+300))
                if cambio_matriz(matriz_costo)[3][0]=="/":
                    ventana.blit(cara_t,(x,y+300))
                if cambio_matriz(matriz_costo)[3][0]=="*":
                    ventana.blit(mono_t,(x,y+300))
                if cambio_matriz(matriz_costo)[3][0]!="0" and cambio_matriz(matriz_costo)[3][0]!="e" and cambio_matriz(matriz_costo)[3][0]!="#" and cambio_matriz(matriz_costo)[3][0]!="d" and cambio_matriz(matriz_costo)[3][0]!="/" and cambio_matriz(matriz_costo)[3][0]!="*":
                    text=cambio_matriz(matriz_costo)[3][0]
                    ventana.blit(monoke_t,(x,y+300))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x,y+300))

                if cambio_matriz(matriz_costo)[3][1]=="0":
                        ventana.blit(monoke_t,(x+100,y+300)) 
                if cambio_matriz(matriz_costo)[3][1]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+100,y+300,80,80))
                if cambio_matriz(matriz_costo)[3][1]=="#":
                    pygame.draw.rect(ventana,negro,(x+100,y+300,80,80))
                if cambio_matriz(matriz_costo)[3][1]=="d":
                    ventana.blit(ciervo_t,(x+100,y+300))
                if cambio_matriz(matriz_costo)[3][1]=="/":
                    ventana.blit(cara_t,(x+100,y+300))
                if cambio_matriz(matriz_costo)[3][1]=="*":
                    ventana.blit(mono_t,(x+100,y+300))
                if cambio_matriz(matriz_costo)[3][1]!="0" and cambio_matriz(matriz_costo)[3][1]!="e" and cambio_matriz(matriz_costo)[3][1]!="#" and cambio_matriz(matriz_costo)[3][1]!="d" and cambio_matriz(matriz_costo)[3][1]!="/" and cambio_matriz(matriz_costo)[3][1]!="*":
                    text=cambio_matriz(matriz_costo)[3][1]
                    ventana.blit(monoke_t,(x+100,y+300))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+100,y+300))

                if cambio_matriz(matriz_costo)[3][2]=="0":
                        ventana.blit(monoke_t,(x+200,y+300)) 
                if cambio_matriz(matriz_costo)[3][2]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+200,y+300,80,80))
                if cambio_matriz(matriz_costo)[3][2]=="#":
                    pygame.draw.rect(ventana,negro,(x+200,y+300,80,80))
                if cambio_matriz(matriz_costo)[3][2]=="d":
                    ventana.blit(ciervo_t,(x+200,y+300))
                if cambio_matriz(matriz_costo)[3][2]=="/":
                    ventana.blit(cara_t,(x+200,y+300))
                if cambio_matriz(matriz_costo)[3][2]=="*":
                    ventana.blit(mono_t,(x+200,y+300))
                if cambio_matriz(matriz_costo)[3][2]!="0" and cambio_matriz(matriz_costo)[3][2]!="e" and cambio_matriz(matriz_costo)[3][2]!="#" and cambio_matriz(matriz_costo)[3][2]!="d" and cambio_matriz(matriz_costo)[3][2]!="/" and cambio_matriz(matriz_costo)[3][2]!="*":
                    text=cambio_matriz(matriz_costo)[3][2]
                    ventana.blit(monoke_t,(x+200,y+300))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+200,y+300))

                if cambio_matriz(matriz_costo)[3][3]=="0":
                        ventana.blit(monoke_t,(x+300,y+300)) 
                if cambio_matriz(matriz_costo)[3][3]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+300,y+300,80,80))
                if cambio_matriz(matriz_costo)[3][3]=="#":
                    pygame.draw.rect(ventana,negro,(x+300,y+300,80,80))
                if cambio_matriz(matriz_costo)[3][3]=="d":
                    ventana.blit(ciervo_t,(x+300,y+300))
                if cambio_matriz(matriz_costo)[3][3]=="/":
                    ventana.blit(cara_t,(x+300,y+300))
                if cambio_matriz(matriz_costo)[3][3]=="*":
                    ventana.blit(mono_t,(x+300,y+300))
                if cambio_matriz(matriz_costo)[3][3]!="0" and cambio_matriz(matriz_costo)[3][3]!="e" and cambio_matriz(matriz_costo)[3][3]!="#" and cambio_matriz(matriz_costo)[3][3]!="d" and cambio_matriz(matriz_costo)[3][3]!="/" and cambio_matriz(matriz_costo)[3][3]!="*":
                    text=cambio_matriz(matriz_costo)[3][3]
                    ventana.blit(monoke_t,(x+300,y+300))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+300,y+300))

                if cambio_matriz(matriz_costo)[3][4]=="0":
                        ventana.blit(monoke_t,(x+400,y+300)) 
                if cambio_matriz(matriz_costo)[3][4]=="e":
                    pygame.draw.rect(ventana,colorfigura,(x+400,y+300,80,80))
                if cambio_matriz(matriz_costo)[3][4]=="#":
                    pygame.draw.rect(ventana,negro,(x+400,y+300,80,80))
                if cambio_matriz(matriz_costo)[3][4]=="d":
                    ventana.blit(ciervo_t,(x+400,y+300))
                if cambio_matriz(matriz_costo)[3][4]=="/":
                    ventana.blit(cara_t,(x+400,y+300))
                if cambio_matriz(matriz_costo)[3][4]=="*":
                    ventana.blit(mono_t,(x+400,y+300))
                if cambio_matriz(matriz_costo)[3][4]!="0" and cambio_matriz(matriz_costo)[3][4]!="e" and cambio_matriz(matriz_costo)[3][4]!="#" and cambio_matriz(matriz_costo)[3][4]!="d" and cambio_matriz(matriz_costo)[3][4]!="/" and cambio_matriz(matriz_costo)[3][4]!="*":
                    text=cambio_matriz(matriz_costo)[3][4]
                    ventana.blit(monoke_t,(x+400,y+300))
                    mensaje = fuente.render(text, 1, (negro))
                    ventana.blit(mensaje, (x+400,y+300))
        pygame.display.update()

# print(f"Iterativa : {cambio_matriz(matriz_recorrido)}")
# print(f"Amplitud : {cambio_matriz(matriz_bfs)}")
# print(f"Costo Uniforme : {cambio_matriz(matriz_costo)}")



me="Mostramos una pequeña Interfaz de los recorridos\n de los agentes en las matrices probadas"
Label(frame,text=me,font=("Arial",12)).grid(row=0,column=1,columnspan=3,pady=30)

btn_profundidad=Button(frame,text="Recorrido Iterativa",width=20,font=("Arial",12),command=lambda:recorrrido_iterativa())
btn_profundidad.grid(row=1,column=1,pady=20,padx=20)

btn_amplitud=Button(frame,text="Recorrido Amplitud",width=20,font=("Arial",12),command=lambda:recorrido_amplitud())
btn_amplitud.grid(row=1,column=2,pady=20,padx=20)

btn_costo=Button(frame,text="Recorrido Costo Uniforme",width=20,font=("Arial",12),command=lambda:recorrido_costo())
btn_costo.grid(row=2,column=1,pady=20,padx=20,columnspan=3)
root.mainloop()
