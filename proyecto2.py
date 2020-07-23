#import ---> Importa modulos
import pygame
import sys
import random
import ctypes

#Bibliografía:
def bibliografia(text):
    Bib=['[https://stackoverflow.com/questions/11603222/allowing-resizing-window-pygame],[https://github.com/search?q=pygame.display.toggle_fullscreen&type=Code&l=Python],[https://www.pygame.org/wiki/tutorials/],[https://www.tutorialspoint.com/python3/python_modules.htm],[http://index-of.es/Python/Beginning.Game.Development.with.Python.and.Pygame.From.Novice.to.Professional.Will.McGugan.2007.pdf],[https://buildmedia.readthedocs.org/media/pdf/pygame/latest/pygame.pdf],[https://www.bitdegree.org/learn/python-class#:~:text=In%20short%2C%20a%20Python%20class,attributes%20the%20object%20can%20have.],[https://github.com/R0X0RE0/Dragon/blob/d7b92eee9165b65d56692fe7db5e631826785b27/Python%20Files/Dragon%20Full%20Demo/TEST_GAMES/demos/base/basescripts/engscripts/pygamebase.py],[https://stackoverflow.com/questions/39274460/pygame-fullscreen-display-flag-creates-a-game-screen-that-is-too-large-for-the-s/39298107#39298107]']



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


#Baraja de jugador







c_size = (105,305)#Card size
c_size_juego = (105, 550)
#Tacocat
tacoImg = pygame.image.load('TrueTacocat.png')
tacoImg = pygame.transform.scale(tacoImg,c_size)
tacoX = 570
tacoY = 75
tacoX_change = 0

#Comunes:
#
D = pygame.image.load('DEFUSE.png')
D = pygame.transform.scale(D,c_size_juego)
#Bomb
B = pygame.image.load('BOMB.png')
B = pygame.transform.scale(B,c_size_juego)
def Bomb(x,y,h,w,"At")

A=pygame.image.load('ATTACK.png')
A = pygame.transform.scale(A,c_size_juego)
#Shuffle
Sh = pygame.image.load('SHUFFLE.png')
Sh = pygame.transform.scale(Sh,c_size_juego)
#Skip
Sk = pygame.image.load('SKIP.png')
Sk = pygame.transform.scale(Sk,c_size_juego)
#See the future
Sf = pygame.image.load('SEETHEFUTURE.png')
Sf = pygame.transform.scale(Sf,c_size_juego)
#Especiales:
#Favor
F = pygame.image.load('FAVOR.png')
F = pygame.transform.scale(F,c_size_juego)
#Nope
N = pygame.image.load('NOPE.png')
N = pygame.transform.scale(N,c_size_juego)
#Comodin1
C1 = pygame.image.load('COMODIN1.png')
C1 = pygame.transform.scale(C1,c_size_juego)
#Comodin2
C2 = pygame.image.load('COMODIN2.png')
C2 = pygame.transform.scale(C2,c_size_juego)
#Comodin3
C3 = pygame.image.load('COMODIN3.png')
C3 = pygame.transform.scale(C3,c_size_juego)
#Comodin4
C4 = pygame.image.load('COMODIN4.png')
C4 = pygame.transform.scale(C4,c_size_juego)
#Comodin5
C5 = pygame.image.load('COMODIN5.png')
C5 = pygame.transform.scale(C5,c_size_juego)

def taco(x,y):
    screen.blit(tacoImg,(x,y))
def acciones(A,x,y,w,h,action=None):
    click = pygame.mouse.get_pressed()
    print click()
        if click[] ==[1] and action !=None:
            if action == "At":
                Atttack()
            elif action == "Def":
                Defuse()
            elif action == "Shuf":
                Shuffle()
            elif action == "Ski":
                skip()
            elif action == "StF":
                Seethefuture()
            elif action == "Fav":
                Favor()
            elif action == "Nop":
                Nope()
            elif action== "bomb":
                Bomb()
            
                
            
            
        



# -------- Ejecucion de del juego ----------- #
run=True #Variable para regular la ejecución

while run:
    screen.fill((0,0,0)) 
    screen.blit(bg,(0,0))
    for event in pygame.event.get(): #Obtener eventos (acciones realizadas por el usuario)
        if event.type == pygame.QUIT: # Cierre del programa
            #sys.exit()
            run=False #Cambia valor de la variable
            
    taco(tacoX,tacoY)
    pygame.display.update() # Regula la acutalización de la ventana
pygame.quit()
quit()
