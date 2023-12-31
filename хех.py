from tkinter import *
from random import randint

win = Tk()
win.geometry('210x150')
win.title('Угадай число')

a = randint(1, 101)

def start():
    global a
    a = randint(1, 101)
    answer = Label(win, text='',
                   fg='white', bg='black').grid(row=5, column=1, columnspan=10, sticky='nsew')

def lucky():
    b = int(digit.get())
    if a == b:
        answer = Label(win, text='Вы выйграли!', fg='white', bg='black').grid(row=5, column=1,
                                                                              columnspan=10, sticky='nsew')
    else:
        if a > b:
            answer = Label(win, text='Попробуйте число побольше!',
                           fg='white', bg='black').grid(row=5, column=1,columnspan=10, sticky='nsew')
        else:
            answer = Label(win, text='Попробуйте число поменьше!',
                           fg='white', bg='black').grid(row=5, column=1, columnspan=10, sticky='nsew')


text_1 = Label(win, text='Угадайте число', fg='white', bg='black').grid(row=1, column=1, columnspan=10, sticky='nsew')
text_2 = Label(win, text='Введите число', fg='white', bg='black').grid(row=2, column=1, columnspan=10, sticky='nsew')

digit=Entry(win)
digit.focus()
digit.grid(row=4,column=1,columnspan=10,sticky=NSEW)


but_1 = Button(win, text="Испытать удачу", command=lucky, fg='white', bg='red').grid(row=10, column=1, columnspan=10,sticky="nsew")
but_1 = Button(win, text="Начать заново", command=start, fg='white', bg='red').grid(row=11, column=1, columnspan=10,sticky="nsew")


win.mainloop()