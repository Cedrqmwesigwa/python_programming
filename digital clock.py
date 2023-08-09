from tkinter import *
from time import strftime
mywindow=Tk()
mywindow.title('my clock')
def time():
    mytime=strftime('%H:%M %p')
    clock.configure(text=mytime)
    clock.after(1000, time)
clock= label(mywindow, font=('arial', 40, 'bold'), background= 'white', foreground='black' )
clock.pack(anchor='center')
time ()
mainloop()