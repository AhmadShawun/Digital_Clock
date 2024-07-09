from tkinter import *

clock = Tk()
clock.title('Digital Clock') # Title
# Graphics work
clock.geometry('800x600') #for window size by pixels
clock.config(bg='#064534') # Background color

lab_hr = Label(clock,text='00',font=('DM Led',60,'bold'), bg='#b50b41',fg='white') # for hour (class,)
lab_hr.place(x=35,y=35,height=120,width=120)

lab_min = Label(clock,text='00',font=('DM Led',60,'bold'), bg='#b50b41',fg='white') # for min (class,)
lab_min.place(x=250,y=35,height=120,width=120)

lab_sac = Label(clock,text='00',font=('DM Led',60,'bold'), bg='#b50b41',fg='white') # for min (class,)
lab_sac.place(x=450,y=35,height=120,width=120)

lab_am = Label(clock,text='00',font=('DM Led',60,'bold'), bg='#b50b41',fg='white') # for min (class,)
lab_am.place(x=650,y=35,height=120,width=120)


clock.mainloop()