import time
from tkinter import Tk, Label

def digital_clock():
    root = Tk()
    root.title("Relógio Digital")
    
    clock_label = Label(root, font=('Arial', 80), bg='black', fg='white')
    clock_label.pack(anchor='center')
    
    def update_time():
        current_time = time.strftime("%H:%M:%S", time.localtime())
        clock_label.config(text=current_time)
        clock_label.after(1000, update_time)
    
    update_time()
    root.mainloop()

# Executar o relógio digital
digital_clock()
