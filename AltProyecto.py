#import ---> Importa modulos
import pygame
import sys
import random
import ctypes



#Bibliografía:
def bibliografia(text):
    Bib=['[],[https://www.tutorialspoint.com/python3/number_shuffle.htm],[https://www.youtube.com/watch?v=h5hW3ynHvhM],[https://github.com/Aaron-Buckles/solitaire],[https://stackoverflow.com/questions/14895599/insert-an-element-at-specific-index-in-a-list-and-return-updated-list],[https://www.geeksforgeeks.org/python-truncate-a-list/],[https://stackoverflow.com/questions/2189800/length-of-an-integer-in-python],[https://stackoverflow.com/questions/11603222/allowing-resizing-window-pygame],[https://github.com/search?q=pygame.display.toggle_fullscreen&type=Code&l=Python],[https://www.pygame.org/wiki/tutorials/],[https://www.tutorialspoint.com/python3/python_modules.htm],[http://index-of.es/Python/Beginning.Game.Development.with.Python.and.Pygame.From.Novice.to.Professional.Will.McGugan.2007.pdf],[https://buildmedia.readthedocs.org/media/pdf/pygame/latest/pygame.pdf],[https://www.bitdegree.org/learn/python-class#:~:text=In%20short%2C%20a%20Python%20class,attributes%20the%20object%20can%20have.],[https://github.com/R0X0RE0/Dragon/blob/d7b92eee9165b65d56692fe7db5e631826785b27/Python%20Files/Dragon%20Full%20Demo/TEST_GAMES/demos/base/basescripts/engscripts/pygamebase.py],[https://stackoverflow.com/questions/39274460/pygame-fullscreen-display-flag-creates-a-game-screen-that-is-too-large-for-the-s/39298107#39298107]']

    
#Inicio de diseño de la interfaz:
pygame.init() #Inicializar pygame

#Colores:


#Resolucion: #Notar que no funciona en linux, sino unicamentye en Windows
##ctypes.windll.user32.SetProcessDPIAware() #obtine información de la resolución actualmente utilizada
##true_res = (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)) #Almacenamiento de páramentros
##pygame.display.set_mode(true_res,pygame.FULLSCREEN) #Creación de ventana
##

Wsize = (1300,700) #Tamaño de ventana
screen = pygame.display.set_mode(Wsize) #Uso provisional

bg = pygame.image.load('Fondo.png')
bg = pygame.transform.scale(bg,Wsize)

pygame.display.set_caption('Exploding Kittens') #Título
icon = pygame.image.load('inicio.jpg') #Icono
pygame.display.set_icon(icon) #Icono








#***********************************************************************************************************************

#Baraja de jugador

c_size = (105,305)#Card size
c_size_juego = (105, 550)
#Tacocat
tacoImg = pygame.image.load('TrueTacocat.png')
tacoImg = pygame.transform.scale(tacoImg,c_size)
tacoX = 570
tacoY = 75
tacoX_change = 0

#Reverso de carta
reverse= pygame.image.load("reverso.png")
reverse= pygame.transform.scale (reverso.png,c_size)

#Comunes:
#Defuse
D = pygame.image.load('DEFUSE.png')
D = pygame.transform.scale(D,c_size_juego)
Dx = 75
Dy = 0
DMx = 0
DMy = 0

#Bomb
B = pygame.image.load('BOMB.png')
B = pygame.transform.scale(B,c_size_juego)
Bx = 75
By= 0
BMx = 0
BMy = 0

#Attack
A=pygame.image.load('ATTACK.png')
A = pygame.transform.scale(A,c_size_juego)
Ax = 75
Ay = 0
AMx = 0
AMy = 0

#Shuffle
Sh = pygame.image.load('SHUFFLE.png')
Sh = pygame.transform.scale(Sh,c_size_juego)
Shy = 75
Shx = 0 
ShMx = 0
ShMy = 0

#Skip
Sk = pygame.image.load('SKIP.png')
Sk = pygame.transform.scale(Sk,c_size_juego)
Skx = 75
Sky = 0
SkMx = 0
SkMy = 0

#See the future
Sf = pygame.image.load('SEETHEFUTURE.png')
Sf = pygame.transform.scale(Sf,c_size_juego)
Sfx = 75
Sfy = 0
SfMx = 0
SfMx = 0
#Especiales:
#Favor
F = pygame.image.load('FAVOR.png')
F = pygame.transform.scale(F,c_size_juego)
Fx = 60
Fy = 0
FMx = 0
FMy = 0
#Nope
N = pygame.image.load('NOPE.png')
N = pygame.transform.scale(N,c_size_juego)
Nx = 60
Ny = 0
NMx = 0
NMy = 0
#Comodin1
C1 = pygame.image.load('COMODIN1.png')
C1 = pygame.transform.scale(C1,c_size_juego)
C1x = 60
C1y = 0
C1Mx = 0
C1My = 0
#Comodin2
C2 = pygame.image.load('COMODIN2.png')
C2 = pygame.transform.scale(C2,c_size_juego)
C2x = 60
C2y = 0
C2Mx = 0
C2My = 0
#Comodin3
C3 = pygame.image.load('COMODIN3.png')
C3 = pygame.transform.scale(C3,c_size_juego)
C3X = 60
C3y = 0
C3Mx = 0
C3My = 0
#Comodin4
C4 = pygame.image.load('COMODIN4.png')
C4 = pygame.transform.scale(C4,c_size_juego)
C4x = 55
C4y = 0
C4Mx = 0
C4My = 0
#Comodin5
C5 = pygame.image.load('COMODIN5.png')
C5 = pygame.transform.scale(C5,c_size_juego)
C5x = 50
C5y = 0
C5Mx = 0
C5My = 0

#Lista baraja central
Box = [D,B,A,] 

#Funcion de cartas en la baraja central - Animacion
class Bcentral():
    




#Funcion de ejemplo
def taco(x,y):
    screen.blit(tacoImg,(x,y))



#Funcion para insertar elementos, permite al jugador agregar la carta a la baraja central donde desee
def inserter(L,i,e): # L = List, i = Index, e = Element
    if L == []:
       return "Empty list"

    elif isinstance(e,int)==True:
        L0 = L[:] 
        L0[i-1:i-1] = [e]
        return L0
    elif isinstance(e,str)==True:
         L0 == L[:]
         L0 == L[i-1:i-1] = [e]
    else:
        L.extend(e)
        return L

# -------- Ejecucion de del juego ----------- #
run=True #Variable para regular la ejecución

while run:
    screen.fill((0,0,0)) 
    screen.blit(bg,(0,0))
    for event in pygame.event.get(): #Obtener eventos (acciones realizadas por el usuario)
        if event.type == pygame.QUIT: # Cierre del programa
            #sys.exit()
            run=False #Cambia valor de la variable
    enemigos(c_size)        
    taco(tacoX,tacoY)
    pygame.display.update() # Regula la acutalización de la ventana
pygame.quit()
quit()
