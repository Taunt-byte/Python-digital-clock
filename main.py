from tkinter import *
from tkinter import ttk
from datetime import datetime

###### Cores usadas #######

cor1 = "#3d3d3d"  # preta
cor2 = "#fafcff"  # branca
cor3 = "#21c25c"  # verde
cor4 = "#eb463b"  # vermelha
cor5 = "#dedcdc"  # cinza
cor6 = "#3080f0"  # azul

fundo = cor1
cor = cor2

janela = Tk()
janela.title("")
janela.geometry("450*200")
janela.resizable(width=False, height=False)
janela.configure(bg = cor1)

tempo=detetime.now()

hora = tempo.strftime("%H: %M: %S")
dia_semana = tempo.strftime("%A")
dia = tempo.day
mes = tempo.strftime("%b")
ano = empo.strftime("%Y")



print(mes)

janela.mainloop()