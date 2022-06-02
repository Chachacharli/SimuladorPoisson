from tkinter import *
from tkinter import ttk
from lib2to3.pgen2.pgen import generate_grammar
from matplotlib import pyplot as plt
from scipy import stats
import statistics
import numpy
import warnings
warnings.filterwarnings('ignore')
import random


from matplotlib.pyplot import text
#Constantes
OptionList = [
"Inserte dato",
"Lona Azul",
"Lona Blanca",
"Lona Gris",
"Lona Negra",
"Lona Roja"
]
vrAzul = [7,3,2,4,0,7,2,3,1,1,1,1,3,2,3,1,1,1,3,4,3,4,4,1,2,5,4,4,3,3]
vrBlanco =[2,1,1,2,2,4,1,1,4,3,2,0,1,1,0,2,2,2,2,3,5,3,6,3,4,6,0,4,1,6]
vrGris = [0,0,1,0,0,0,0,0,1,3,0,2,3,0,0,1,3,1,0,1,1,1,0,2,2,2,1,1,1,1]
vrnegro = [2,0,0,0,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1,1,2,0,0,0,2,4,1,2,0,1]
vrRojo = [0,0,1,1,0,0,0,0,0,1,0,1,1,4,0,0,0,0,0,0,0,0,1,1,2,2,2,2,1,2]
data = []


#Ventana principal
root = Tk()
root.geometry('350x230')
root.title('SIMULADOR MR. LONAS')
root.resizable(width=False, height=False)

#variables
datoLona = StringVar(root)
datoLona.set(OptionList[0])
datoDias = IntVar()
datoStock = IntVar()



#Definir funciones



def ventanaNueva():
    lonasVendidas = 0
    tiempoMuerto = 0
    valorDias=datoDias.get()
    valorStock = datoStock.get()
    valorLona = datoLona.get()
    
    stockRestante = valorStock

    if(valorLona == 'Lona Azul'):

        for i in range(valorDias):
            data.append(random.choice(vrAzul))

        norm = stats.poisson.rvs(mu=statistics.mean(vrAzul), size=valorDias)
        norm= numpy.ndarray.tolist(norm)

        for i in range(valorDias):
            if stockRestante < norm[i]:
                tiempoMuerto += 1
                stockRestante = stockRestante + valorStock
            else:
               stockRestante = stockRestante - norm[i]
               stockRestante = stockRestante + valorStock
               lonasVendidas = lonasVendidas + norm[i]
         

        win = Toplevel()
        win.geometry('600x350')
        win.title('Resultados')
        
        frm2 = LabelFrame(win,text = 'Resultados',padx=50, pady=30)
        frm2.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)
        ttk.Label(frm2,text="El total de dias es de: " + str(valorDias)).grid(column=0, row=0)
        ttk.Label(frm2,text="El total de stock inicial es: " + str(valorStock)).grid(column=0, row=1)
        ttk.Label(frm2,text="La lona estimada es: " + str(valorLona)).grid(column=0, row=2)

        ttk.Label(frm2,text="Lonas estimadas:  " + str(sum(norm))).grid(column=0, row=3)
        ttk.Label(frm2,text= norm).grid(column=0, row=4)
        ttk.Label(frm2,text="Lonas vendidas: " + str(lonasVendidas)).grid(column=0, row=5)
        ttk.Label(frm2,text="Stock Restante: " + str(stockRestante)).grid(column=0, row=6)
        ttk.Label(frm2,text="Tiempo muerto: " + str(tiempoMuerto)).grid(column=0, row=7)

        win = Toplevel()
        win.geometry('600x350')
        win.title('Valores aleatorios generados')
        frm2 = LabelFrame(win,text = 'Datos  del generador aleatorio.',padx=50, pady=30)
        frm2.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)
        ttk.Label(frm2,text="Valores generados aleatoriamente:  ").grid(column=0, row=1)
        ttk.Label(frm2,text= norm).grid(column=0, row=2)
        ttk.Label(frm2,text="Cantidad de valores aleatorios generados:  "+str(len(norm))).grid(column=0, row=3)
        ttk.Label(frm2,text="Valor lambda usado para generar los datos: "+str(statistics.mean(vrAzul))).grid(column=0, row=4)
    elif(valorLona == "Lona Blanca"):
        for i in range(valorDias):
            data.append(random.choice(vrBlanco))

        norm = stats.poisson.rvs(mu=statistics.mean(vrBlanco), size=valorDias)
        norm= numpy.ndarray.tolist(norm)

        for i in range(valorDias):
            if stockRestante < norm[i]:
                tiempoMuerto += 1
                stockRestante = stockRestante + valorStock
            else:
               stockRestante = stockRestante - norm[i]
               stockRestante = stockRestante + valorStock
               lonasVendidas = lonasVendidas + norm[i]

        win = Toplevel()
        win.geometry('600x350')
        win.title('Resultados')
        
        frm2 = LabelFrame(win,text = 'Resultados',padx=50, pady=30)
        frm2.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)
        ttk.Label(frm2,text="El total de dias es de: " + str(valorDias)).grid(column=0, row=0)
        ttk.Label(frm2,text="El total de stock inicial es: " + str(valorStock)).grid(column=0, row=1)
        ttk.Label(frm2,text="La lona estimada es: " + str(valorLona)).grid(column=0, row=2)

        ttk.Label(frm2,text="Lonas estimadas:  " + str(sum(norm))).grid(column=0, row=3)
        ttk.Label(frm2,text= norm).grid(column=0, row=4)
        ttk.Label(frm2,text="Lonas vendidas: " + str(lonasVendidas)).grid(column=0, row=5)
        ttk.Label(frm2,text="Stock Restante: " + str(stockRestante)).grid(column=0, row=6)
        ttk.Label(frm2,text="Tiempo muerto: " + str(tiempoMuerto)).grid(column=0, row=7)

        win = Toplevel()
        win.geometry('600x350')
        win.title('Valores aleatorios generados')
        frm2 = LabelFrame(win,text = 'Datos  del generador aleatorio.',padx=50, pady=30)
        frm2.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)
        ttk.Label(frm2,text="Valores generados aleatoriamente:  ").grid(column=0, row=1)
        ttk.Label(frm2,text= norm).grid(column=0, row=2)
        ttk.Label(frm2,text="Cantidad de valores aleatorios generados:  "+str(len(norm))).grid(column=0, row=3)
        ttk.Label(frm2,text="Valor lambda usado para generar los datos: "+str(statistics.mean(vrBlanco))).grid(column=0, row=4)

    elif(valorLona == 'Lona Gris'):
        for i in range(valorDias):
            data.append(random.choice(vrGris))

        norm = stats.poisson.rvs(mu=statistics.mean(vrGris), size=valorDias)
        norm= numpy.ndarray.tolist(norm)

        for i in range(valorDias):
            if stockRestante < norm[i]:
                tiempoMuerto += 1
                stockRestante = stockRestante + valorStock
            else:
               stockRestante = stockRestante - norm[i]
               stockRestante = stockRestante + valorStock
               lonasVendidas = lonasVendidas + norm[i]

        win = Toplevel()
        win.geometry('600x350')
        win.title('Resultados')
        
        frm2 = LabelFrame(win,text = 'Resultados',padx=50, pady=30)
        frm2.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)
        ttk.Label(frm2,text="El total de dias es de: " + str(valorDias)).grid(column=0, row=0)
        ttk.Label(frm2,text="El total de stock inicial es: " + str(valorStock)).grid(column=0, row=1)
        ttk.Label(frm2,text="La lona estimada es: " + str(valorLona)).grid(column=0, row=2)

        ttk.Label(frm2,text="Lonas estimadas:  " + str(sum(norm))).grid(column=0, row=3)
        ttk.Label(frm2,text= norm).grid(column=0, row=4)
        ttk.Label(frm2,text="Lonas vendidas: " + str(lonasVendidas)).grid(column=0, row=5)
        ttk.Label(frm2,text="Stock Restante: " + str(stockRestante)).grid(column=0, row=6)
        ttk.Label(frm2,text="Tiempo muerto: " + str(tiempoMuerto)).grid(column=0, row=7)

        win = Toplevel()
        win.geometry('600x350')
        win.title('Valores aleatorios generados')
        frm2 = LabelFrame(win,text = 'Datos  del generador aleatorio.',padx=50, pady=30)
        frm2.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)
        ttk.Label(frm2,text="Valores generados aleatoriamente:  ").grid(column=0, row=1)
        ttk.Label(frm2,text= norm).grid(column=0, row=2)
        ttk.Label(frm2,text="Cantidad de valores aleatorios generados:  "+str(len(norm))).grid(column=0, row=3)
        ttk.Label(frm2,text="Valor lambda usado para generar los datos: "+str(statistics.mean(vrGris))).grid(column=0, row=4)

    elif(valorLona == 'Lona Negra'):
        for i in range(valorDias):
            data.append(random.choice(vrnegro))

        norm = stats.poisson.rvs(mu=statistics.mean(vrnegro), size=valorDias)
        norm= numpy.ndarray.tolist(norm)

        for i in range(valorDias):
            if stockRestante < norm[i]:
                tiempoMuerto += 1
                stockRestante = stockRestante + valorStock
            else:
               stockRestante = stockRestante - norm[i]
               stockRestante = stockRestante + valorStock
               lonasVendidas = lonasVendidas + norm[i]

        win = Toplevel()
        win.geometry('600x350')
        win.title('Resultados')
        
        frm2 = LabelFrame(win,text = 'Resultados',padx=50, pady=30)
        frm2.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)
        ttk.Label(frm2,text="El total de dias es de: " + str(valorDias)).grid(column=0, row=0)
        ttk.Label(frm2,text="El total de stock inicial es: " + str(valorStock)).grid(column=0, row=1)
        ttk.Label(frm2,text="La lona estimada es: " + str(valorLona)).grid(column=0, row=2)

        ttk.Label(frm2,text="Lonas estimadas:  " + str(sum(norm))).grid(column=0, row=3)
        ttk.Label(frm2,text= norm).grid(column=0, row=4)
        ttk.Label(frm2,text="Lonas vendidas: " + str(lonasVendidas)).grid(column=0, row=5)
        ttk.Label(frm2,text="Stock Restante: " + str(stockRestante)).grid(column=0, row=6)
        ttk.Label(frm2,text="Tiempo muerto: " + str(tiempoMuerto)).grid(column=0, row=7)

        win = Toplevel()
        win.geometry('600x350')
        win.title('Valores aleatorios generados')
        frm2 = LabelFrame(win,text = 'Datos  del generador aleatorio.',padx=50, pady=30)
        frm2.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)
        ttk.Label(frm2,text="Valores generados aleatoriamente:  ").grid(column=0, row=1)
        ttk.Label(frm2,text= norm).grid(column=0, row=2)
        ttk.Label(frm2,text="Cantidad de valores aleatorios generados:  "+str(len(norm))).grid(column=0, row=3)
        ttk.Label(frm2,text="Valor lambda usado para generar los datos: "+str(statistics.mean(vrnegro))).grid(column=0, row=4)


    elif(valorLona == 'Lona Roja'):
        for i in range(valorDias):
            data.append(random.choice(vrRojo))

        norm = stats.poisson.rvs(mu=statistics.mean(vrRojo), size=valorDias)
        norm= numpy.ndarray.tolist(norm)

        for i in range(valorDias):
            if stockRestante < norm[i]:
                tiempoMuerto += 1
                stockRestante = stockRestante + valorStock
            else:
               stockRestante = stockRestante - norm[i]
               stockRestante = stockRestante + valorStock
               lonasVendidas = lonasVendidas + norm[i]

        win = Toplevel()
        win.geometry('600x350')
        win.title('Resultados')
        
        frm2 = LabelFrame(win,text = 'Resultados',padx=50, pady=30)
        frm2.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)
        ttk.Label(frm2,text="El total de dias es de: " + str(valorDias)).grid(column=0, row=0)
        ttk.Label(frm2,text="El total de stock inicial es: " + str(valorStock)).grid(column=0, row=1)
        ttk.Label(frm2,text="La lona estimada es: " + str(valorLona)).grid(column=0, row=2)

        ttk.Label(frm2,text="Lonas estimadas:  " + str(sum(norm))).grid(column=0, row=3)
        ttk.Label(frm2,text= norm).grid(column=0, row=4)
        ttk.Label(frm2,text="Lonas vendidas: " + str(lonasVendidas)).grid(column=0, row=5)
        ttk.Label(frm2,text="Stock Restante: " + str(stockRestante)).grid(column=0, row=6)
        ttk.Label(frm2,text="Tiempo muerto: " + str(tiempoMuerto)).grid(column=0, row=7)

        win = Toplevel()
        win.geometry('600x350')
        win.title('Valores aleatorios generados')
        frm2 = LabelFrame(win,text = 'Datos  del generador aleatorio.',padx=50, pady=30)
        frm2.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)
        ttk.Label(frm2,text="Valores generados aleatoriamente:  ").grid(column=0, row=1)
        ttk.Label(frm2,text= norm).grid(column=0, row=2)
        ttk.Label(frm2,text="Cantidad de valores aleatorios generados:  "+str(len(norm))).grid(column=0, row=3)
        ttk.Label(frm2,text="Valor lambda usado para generar los datos: "+str(statistics.mean(vrRojo))).grid(column=0, row=4)

    else:
        win2 = Toplevel()
        win2.geometry('350x230')
        win2.title('Resultados')
        ttk.Label(win2, text=" ERROR, SELECCIONE UN TIPO DE LONA").grid(row = 0, column=0, 
        columnspan=3, padx=20, pady=20)
#Frame principal


frm = LabelFrame(root,text = 'Inserta datos necesarios.',padx=50, pady=30)
frm.grid(row = 0, column=0, columnspan=3, padx=20, pady=20)

ttk.Label(frm, text="Dias a simular").grid(column=0, row=0)
ttk.Entry(frm,textvariable=datoDias).grid(column=2, row=0)

ttk.Label(frm, text="Tipo de lona").grid(column=0, row=1)
ttk.OptionMenu(frm, datoLona ,*OptionList, ).grid(column=2, row=1)

ttk.Label(frm, text="Stock actual").grid(column=0, row=2)
ttk.Entry(frm, textvariable=datoStock ).grid(column=2, row=2)

#Boton de aceptar
ttk.Label(frm, text=" ").grid(column=0, row=3)
ttk.Button(frm, text="Aceptar", command=ventanaNueva).grid(column=2, row=4,sticky= W + E)


root.mainloop()
