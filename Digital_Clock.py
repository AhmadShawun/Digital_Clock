from tkinter import *
import datetime
#print(datetime.datetime.now())

def dateTime():
    time = datetime.datetime.now()
    hour = time.strftime('%I')
    minutes = time.strftime('%M')
    second = time.strftime("%S")
    am = time.strftime("%p")
    lab_hr.config(text=hour)
    lab_min.config(text=minutes)
    lab_sec.config(text=second)
    lab_am.config(text=am)
    lab_hr.after(200,dateTime) # change provided graphics

clock = Tk()
clock.title('Digital Clock') # Title
# Graphics work
clock.geometry('800x600') #for window size by pixels
clock.config(bg='#064534') # Background color

# ******************Time Started***********************

lab_hr = Label(clock,text='00',font=('Ga Maamli',60,'bold'), bg='#b50b41',fg='white') # for hour (class,)
lab_hr.place(x=35,y=35,height=120,width=120)

lab_hr_text = Label(clock,text='Hour',font=('Ga Maamli',24,'bold'), bg='#b50b41',fg='white') # for hour (class,)
lab_hr_text.place(x=35,y=175,height=30,width=120)

lab_min = Label(clock,text='00',font=('Ga Maamli',60,'bold'), bg='#b50b41',fg='white') # for min (class,)
lab_min.place(x=250,y=35,height=120,width=120)

lab_min_text = Label(clock,text='Minutes',font=('Ga Maamli',24,'bold'), bg='#b50b41',fg='white') # for hour (class,)
lab_min_text.place(x=250,y=175,height=30,width=120)

lab_sec = Label(clock,text='00',font=('Ga Maamli',60,'bold'), bg='#b50b41',fg='white') # for min (class,)
lab_sec.place(x=450,y=35,height=120,width=120)

lab_sec_text = Label(clock,text='Sec',font=('Ga Maamli',24,'bold'), bg='#b50b41',fg='white') # for hour (class,)
lab_sec_text.place(x=450,y=175,height=30,width=120)

lab_am = Label(clock,text='00',font=('Ga Maamli',60,'bold'), bg='#b50b41',fg='white') # for min (class,)
lab_am.place(x=650,y=35,height=120,width=120)

lab_am_text = Label(clock,text='Am/Pm',font=('Ga Maamli',24,'bold'), bg='#b50b41',fg='white',) # for hour (class,)
lab_am_text.place(x=650,y=175,height=30,width=120)

# ******************Date Started***********************

lab_date = Label(clock,text='00',font=('Ga Maamli',60,'bold'), bg='#b50b41',fg='white') # for Date (class,)
lab_date.place(x=35,y=350,height=120,width=120)

lab_date_text = Label(clock,text='Date',font=('Ga Maamli',24,'bold'), bg='#b50b41',fg='white') # for Date (class,)
lab_date_text.place(x=35,y=275,height=30,width=120)

lab_mo = Label(clock,text='00',font=('Ga Maamli',60,'bold'), bg='#b50b41',fg='white') # for Month (class,)
lab_mo.place(x=250,y=350,height=120,width=120)

lab_mo_text = Label(clock,text='Month',font=('Ga Maamli',24,'bold'), bg='#b50b41',fg='white') # for Month (class,)
lab_mo_text.place(x=250,y=275,height=30,width=120)

lab_year = Label(clock,text='00',font=('Ga Maamli',60,'bold'), bg='#b50b41',fg='white') # for year (class,)
lab_year.place(x=450,y=350,height=120,width=120)

lab_year_text = Label(clock,text='Year',font=('Ga Maamli',24,'bold'), bg='#b50b41',fg='white') # for year (class,)
lab_year_text.place(x=450,y=275,height=30,width=120)

lab_day = Label(clock,text='00',font=('Ga Maamli',60,'bold'), bg='#b50b41',fg='white') # for Day (class,)
lab_day.place(x=650,y=350,height=120,width=120)

lab_day_text = Label(clock,text='Day',font=('Ga Maamli',24,'bold'), bg='#b50b41',fg='white') # for Day (class,)
lab_day_text.place(x=650,y=275,height=30,width=120)











dateTime()

clock.mainloop()