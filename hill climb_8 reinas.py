import random
from tkinter import ttk
from tkinter import * 
# función uno: el parámetro es el estado de diseño de tablero de ajedrez actual, 
# y el logaritmo de reina de los conflictos de diseño de ocho reinas actuales se juzga de acuerdo con el diseño.
def conflictos(posicion):
        num = 0
        for i in range(len(posicion)):
                for j in range(i + 1,len(posicion)):
 
                        if posicion[i] == posicion[j]:
                                num += 1
                        offset = j - i
                        if abs(posicion[i]-posicion[j]) == offset:
                                num += 1
        return num
#función dos: el parámetro es el estado actual del diseño del tablero de ajedrez, 
#utilizando el método de escalada para seleccionar el mejor diseño del estado vecino y regresar
def  hill_climbing(posicion):
        convert = {}
        length = len(posicion)
        for columna in range(length):
                best_move = posicion[columna]
                for fila in range(length):
                        if posicion[columna] == fila:
                                continue
                        posicion_copy = list(posicion)
                        posicion_copy[columna] = fila
                        convert[(columna,fila)] = conflictos(posicion_copy)
 
        fitness = [] # 
        conflict_now = conflictos(posicion) # logaritmo actual del conflicto de la reina
 
        
        # Almacene todos los diccionarios sucesores posibles para encontrar el mejor sucesor
        for aux1,aux2 in convert.items():
                if aux2 < conflict_now:
                        conflict_now = aux2
        for aux1,aux2 in convert.items():
                if aux2 == conflict_now:
                        fitness.append(aux1)
 
        #Si el mejor elemento del conjunto sucesor es mayor que uno, seleccione uno al azar
        if len(fitness) > 0:
                x = random.randint(0,len(fitness)-1)
                columna = fitness[x][0]
                fila = fitness[x][1]
                posicion[columna] = fila
 
        return posicion
# función tres: encuentre una solución para que las ocho reinas satisfagan el número de conflicto de 0 y 
#recorra el conjunto posterior de cada paso hasta que no haya prisa> repentino 
def reinas():
        posicion = [0,1,2,3,4,5,6,7] # estado inicial, todas las reinas están en diagonal
 
        #Cuando el número de conflictos es mayor que 0, el bucle resuelve el mejor sucesor hasta encontrar la solución de ocho reinas.
        while conflictos(posicion) > 0:
                posicion = hill_climbing(posicion)
                print (posicion)
                print (conflictos(posicion))
        print ("La fitness optima es: ")
        print (posicion)
        return posicion


def mostrarTablero(posicion):
        raiz = Tk()
        raiz.geometry('560x560') # anchura x altura
        raiz.title('Aplicación')
        i=0
        x=0
        img='1'
        imagenes=[]
        while(i<8):
                posReina=posicion[i]
                j=0
                y=0
                while(j<8):
                        if(posReina==j):
                                imagen=PhotoImage(file="assets/cuadro"+img+"-reina.png")
                                imagenes.append(imagen)
                                Label(raiz,image=imagen).place(x=x,y=y)
                        else:
                                imagen=PhotoImage(file="assets/cuadro"+img+".png")
                                imagenes.append(imagen)
                                Label(raiz,image=imagen).place(x=x,y=y)
                        if(img=='1'):
                                img='2'
                        else:
                                img='1'
                        y+=70
                        j+=1
                if(img=='1'):
                        img='2'
                else:
                        img='1'
                x+=70
                i+=1
        raiz.mainloop()

        return 0
 
if __name__ == '__main__':
        posicion=reinas()
        mostrarTablero(posicion)
