from tkinter import *
from charl import treinando
from charl import conversar
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
import tkinter.scrolledtext as ScrolledText

#from charl import testando

window = Tk()
window.title("Chat")
window.geometry('850x600')
lbl = Label(window, text="HIII")
lbl.grid(column=0, row=0)
txt = Entry(window,width=40)
txt.grid(column=1, row=0)
	#chatter.trainer()

#lb2 = Label(window, text="conversa anterior")
#lb2.grid(column=0,row=1)

#txt2 = Entry(window, width = 50)
#txt2.grid(column=1,row=1)
 
editArea = Text(window, width=75, height=75)
editArea.grid(column = 1 ,row = 1)

treinando()

def clicked():
	s = txt.get()
	resp = conversar(s)
	editArea.insert('end',resp)
	editArea.insert('end','\n')

	#lbl.configure(s)
    #res = "Oi" + txt.get()
    #lbl.configure(text= res)
 
btn = Button(window, text="Enviar msg", command=clicked)
 
btn.grid(column=2, row=0)
 
window.mainloop()
