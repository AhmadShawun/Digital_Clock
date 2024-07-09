from tkinter import *

clock = Tk()
clock.title('Digital Clock') # Title
# Graphics work
clock.geometry('800x600') #for window size by pixels
clock.config(bg='#064534') # Background color

lab_hr = Label(clock,text='00',font=('DM Led',60,'bold'), bg='#b50b41',fg='white') # for hour (class,)
lab_hr.place(x=35,y=35,height=120,width=120)

lab_hr_text = Label(clock,text='Hour',font=('DM Led',24,'bold'), bg='#b50b41',fg='white') # for hour (class,)
lab_hr_text.place(x=35,y=175,height=30,width=120)

lab_min = Label(clock,text='00',font=('DM Led',60,'bold'), bg='#b50b41',fg='white') # for min (class,)
lab_min.place(x=250,y=35,height=120,width=120)

lab_min_text = Label(clock,text='Minutes',font=('DM Led',24,'bold'), bg='#b50b41',fg='white') # for hour (class,)
lab_min_text.place(x=250,y=175,height=30,width=120)

lab_sac = Label(clock,text='00',font=('DM Led',60,'bold'), bg='#b50b41',fg='white') # for min (class,)
lab_sac.place(x=450,y=35,height=120,width=120)

lab_sac_text = Label(clock,text='Sec',font=('DM Led',24,'bold'), bg='#b50b41',fg='white') # for hour (class,)
lab_sac_text.place(x=450,y=175,height=30,width=120)

lab_am = Label(clock,text='00',font=('DM Led',60,'bold'), bg='#b50b41',fg='white') # for min (class,)
lab_am.place(x=650,y=35,height=120,width=120)

lab_am_text = Label(clock,text='Am/Pm',font=('DM Led',24,'bold'), bg='#b50b41',fg='white') # for hour (class,)
lab_am_text.place(x=650,y=175,height=30,width=120)


clock.mainloop()