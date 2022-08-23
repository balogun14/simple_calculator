import os
from tkinter import *
from functools import partial
from tkinter import font, ttk


def get_input(entry, argument):
    entry.insert(END, argument)


def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)


def clear(entry):
    entry.delete(0, END)


def calc(entry):
    input_info = entry.get()
    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    clear(entry)
    entry.insert(END, output)


def popupmsg():
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("120x120")
    popup.title("Alert")
    label = Label(popup, text="Cannot divide by 0 ! \n Enter valid values")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", bg="#DDDDDD", command=popup.destroy)
    B1.pack()


root = Tk()
root.title("CALC-X")
root.geometry('600x500')
root.resizable(0, 0)

if "nt" == os.name:
    root.wm_iconbitmap(bitmap = '/home/leo/Documents/calc-x/Background.ico')
# else:
#     root.wm_iconbitmap(bitmap = '/home/leo/Documents/calc-x/Background.ico')
# img = PhotoImage('/home/leo/Documents/calc-x/Background.xbm')
# root.tk.call('wm', 'iconphoto', root._w, img)
entry_font = font.Font(size=30)
entry = Entry(root, justify="center", font=entry_font, width=68)
# entry.grid(row=1, column=12, sticky=N + W + S + E, padx=5, pady=5)
entry.pack()
cal_button_bg = '#FF6600'
num_button_bg = '#4B4B4B'
other_button_bg = '#DDDDDD'
text_fg = '#FFFFFF'
button_active_bg = '#C0C0C0'

num_button = partial(Button, root, fg=text_fg, bg=num_button_bg,
                     padx=45, pady=45, activebackground=button_active_bg)
cal_button = partial(Button, root, fg=text_fg, bg=cal_button_bg,
                     padx=10, pady=10, activebackground=button_active_bg)
s_button = partial(Button, root, fg=text_fg, bg=cal_button_bg,
                   padx=10, pady=10, activebackground=button_active_bg)
button9 = num_button(text='9', bg=num_button_bg,
                     command=lambda: get_input(entry, '9'))
button9.place(x=25, y=60)
button8 = num_button(text='8', command=lambda: get_input(entry, '8'))
button8.place(y=60, x=170)
button7 = num_button(text='7', command=lambda: get_input(entry, '7'))
button7.place(y=60, x=315)
button6 = num_button(text='6', command=lambda: get_input(entry, '6'))
button6.place(y=205, x=25)
button5 = num_button(text='5', command=lambda: get_input(entry, '5'))
button5.place(y=205, x=170)
button4 = num_button(text='4', command=lambda: get_input(entry, '4'))
button4.place(y=205, x=315)

button3 = num_button(text='3', command=lambda: get_input(entry, '3'))
button3.place(y=350, x=25)
button2 = num_button(text='2', command=lambda: get_input(entry, '2'))
button2.place(y=350, x=170)
button1 = num_button(text='1', command=lambda: get_input(entry, '2'))
button1.place(y=350, x=315)
button0 = num_button(text='0', command=lambda: get_input(entry, '0'))
button0.place(y=350, x=460)
button13 = s_button(text='.', command=lambda: get_input(entry, '.'))
button13.place(y=60, x=460)

button14 = Button(root, text='/', fg=text_fg, bg=cal_button_bg, padx=10, pady=10,
                  command=lambda: get_input(entry, '/'))
button14.place(y=60, x=500)

button15 = Button(root, text='<-', bg=other_button_bg, padx=10, pady=3,
                  command=lambda: backspace(entry), activebackground=button_active_bg)
button15.place(x=170, y=470)

button16 = Button(root, text='C', bg=other_button_bg, padx=10, pady=3,
                  command=lambda: clear(entry), activebackground=button_active_bg)
button16.place(x=219, y=470)

button17 = Button(root, text='=', fg=text_fg, bg=cal_button_bg, padx=10, pady=10,
                  command=lambda: calc(entry), activebackground=button_active_bg)
button17.place(x=500, y=140)

button18 = Button(root, text='^', fg=text_fg, bg=cal_button_bg, padx=10, pady=10,
                  command=lambda: get_input(entry, '**'))
button18.place(y=140, x=460)

button19 = cal_button(text='*', command=lambda: get_input(entry, '*'))
button19.place(y=140, x=540)
button11 = cal_button(text='-', command=lambda: get_input(entry, '-'))
button11.place(y=60, x=540)
call_button = partial(Button, root, fg=text_fg, bg=cal_button_bg,
                      height=7, width=2, activebackground=button_active_bg)
button198 = call_button(text='+', command=lambda: get_input(entry, '+'))
button198.place(x=550, y=205)


def quit():
    exit['command'] = root.quit()


exit = Button(root, text='Quit', fg='white', bg='black', command=quit, height=7, width=7)
exit.place(x=460, y=205)
root.mainloop()
