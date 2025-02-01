from tkinter import *
import math

WORK_TIME=0.4
SHORT_BREAK=0.5
LONG_BREAK=3
rep=0
time=None
check_add=''

window=Tk()
window.minsize(500,500)

window.config(padx=100,pady=50,bg='light green')
canvas=Canvas(width=200,height=250,bg='light green',highlightthickness=0)


def count_down(count):
    global time
    if count>=0:
        time=window.after(1000,count_down,count-1)
        min=math.floor(count/60)
        sec=count%60
        if sec==0 :

            canvas.itemconfig(timer_text,text=f'{min}:{sec}0')
        elif sec<10:
            canvas.itemconfig(timer_text, text=f'{min}:0{sec}')
        else:
            canvas.itemconfig(timer_text, text=f'{min}:{sec}')

    else:
        start()




def reset():
    global rep,time,check_add
    rep=0
    window.after_cancel(time)
    check_add=''
    canvas.itemconfig(timer_text,text='00:00')
    timer_label.config(text='Work',fg='green')


def start():
    global rep,check_add
    rep += 1


    if rep%8==0:
        count_down(int(LONG_BREAK*60))
        timer_label.config(text='Long break', fg='red')
    elif rep%2==0:
        check='✔'

        check_add+=check
        count_down(int(SHORT_BREAK*60))
        timer_label.config(text='Short break', fg='yellow')
        check_mark.config(text=check_add)


    elif rep%2!=0:
        count_down(int(WORK_TIME*60))
        timer_label.config(text='Work', fg='green')














canvas.grid(column=1,row=1)

tomato_image=PhotoImage(file='tomato.png')

canvas.create_image(100,112,image=tomato_image)
timer_text=canvas.create_text(100,125,text='00:00',font=('Times New Roman',25,'bold'),fill='white')

timer_label=Label(text='Timer',fg='green',bg='light green',font=('Courier',40,'bold'))
timer_label.grid(column=1,row=0)

start_button=Button(text='Start',font=('Times New Roman',15,'bold'),bg='tomato',fg='white',command=start)
start_button.grid(column=0,row=2)

reset_button=Button(text='Reset',font=('Times New Roman',15,'bold'),bg='tomato',fg='white',command=reset)

reset_button.grid(column=2,row=2)

check_mark=Label(text='',fg='green',bg='light green',font=('Arial',20,'bold'))
check_mark.grid(column=1,row=2)



























window.mainloop()
