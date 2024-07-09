from tkinter import *

clock = Tk()
clock.title('Digital Clock') # Title
# Graphics work
clock.geometry('800x400') #for window size by pixels
clock.config(bg='#064534') # Background color

lab_hr = Label(clock,text='00',font=('DM Led',60,'bold'), bg='#b50b41',fg='white') # for hour (class,)
lab_hr.place(x=40,y=40,height=110,width=100)




clock.mainloop()