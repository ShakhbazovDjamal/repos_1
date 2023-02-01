################################################################################################# знакомство с tkinter

# from tkinter import *
# root = Tk()
# root.title('Window')
# root.geometry('600x400')
# def function1():
#    b=int(e.get())*2
#    print(b)
# e = Entry(root, width = 30, bg = 'green', font = 'consolas', fg = 'red')
# e.pack()
# a = Button(root, text='нажми меня', width = 30, height = 10, command = function1, bg = 'orange', activebackground = 'orange')
# a.pack()
# root.mainloop()

################################################################################################# изменение цвета на кнопку

#from tkinter import *
#def change():
#    canvas.itemconfig(square, fill='green')
#side = 200
#canvas_width, canvas_height = 300, 300
#x, y=20, 20
#root = Tk()
#root.title('Window')
#root.geometry('800x400')
#canvas = Canvas(root, width =400, height = 300, bg = 'purple')
#canvas.pack()
##canvas.create_line(150,10,10,150,width = 10, fill='green')
##canvas.create_polygon(140,140,220,220, 190,300, activewidth = 5, fill='cyan', activefill = 'yellow', activeoutline = 'brown', activedash='5')
#square = canvas.create_rectangle(x, y, x+side, y+side, fill='yellow')
#Button(text='нажми', command=change).pack()
#root.mainloop()

################################################################################################# messagebox

#from tkinter import *
#from tkinter import messagebox
#def button_1():
#	messagebox.showinfo('Результат', int(a.get())*15)
#root=Tk()
#root.title('Приложение')
#root.geometry('500x300')
#a=Entry(root, width=10, bg='gray', fg='white', font='consolas')
#a.pack()
#Button(root, text='Посчитать', width=10, height=2, bg='cyan', command=button_1).pack()
#root.mainloop()

################################################################################################# игра с кнопкой

#from tkinter import *
#import random
#score, max_score = 0, 20
#size_x, size_y = 1280, 700
#def put():
#    global button
#    button = Button(root, text='Нажми меня', bg = 'gray', activebackground = 'red', command = click)
#    button.place(x=random.randint(10, size_x-10), y=random.randint(5, size_y-5))
#def click():
#    global score
#    button.destroy()
#    score+=1
#    if score < max_score:
#        put()
#    else:
#        Label(root, text='Вы выиграли, \n поздравляем').place(relx=0.5,rely=0.5)
#root = Tk()
#root.title('Моя первая игра')
#root.geometry(f'{size_x}x{size_y}')
#root.resizable(False, False)
#put()
#root.mainloop()

################################################################################################# сложный калькулятор

#from tkinter import *
#def set_value(formula):
#    if formula == '':
#        label['text'] = '0'
#    else:
#        label['text']=str(eval(formula))
#def logic(operation):
#    if operation == 'C':
#        set_value('')
#    elif operation == 'DEL':
#        set_value(label['text'][0:-1])
#    elif operation == 'X^2':
#        set_value(str((eval(label['text']))**2))
#    elif operation == '=':
#        set_value(label['text'])
#    else:
#        if label['text']=='0':
#            label['text']=''
#        label['text'] = label['text']+operation
#list = ['C','DEL','*','=','1','2','3','/','4','5','6','+','7','8','9','-','(','0',')','X^2']
#root = Tk()
#root['bg'] = 'black'
#root.title('Cложный калькулятор')
#root.geometry('485x550')
#root.resizable(False, False)
#label = Label(text='0',font=('Consolas',21,'bold'),bg='black',foreground='white')
#label.place(x=10,y=50)
#x=10
#y=140
#for lis in list:
#    com = lambda x=lis: logic(x)
#    Button(text=lis, bg='white',font=('Consolas',15), command = com).place(x=x, y=y, width=115, height = 79)
#    x+=117
#    if x>400:
#        x=10
#        y+=81
#root.mainloop()

################################################################################################# 
# from tkinter import *
# def set_value(formula):
#     if formula == '':
#         label['text'] = '0'
#     else:
#         label['text']=str(eval(formula))
# def logic(operation):
#     if operation == 'C':
#         set_value('')
#     elif operation == 'DEL':
#         set_value(label['text'][0:-1])
#     elif operation == 'X^2':
#         set_value(str((eval(label['text']))**2))
#     elif operation == '=':
#         set_value(label['text'])
#     else:
#         if label['text']=='0':
#             label['text']=''
#         label['text'] = label['text']+operation
# list = ['C','DEL','*','=','1','2','3','/','4','5','6','+','7','8','9','-','(','0',')','X^2']
# root = Tk()
# root['bg'] = 'black'
# root.title('Cложный калькулятор')
# root.geometry('485x550')
# root.resizable(False, False)
# label = Label(text='0',font=('Consolas',21,'bold'),bg='black',foreground='white')
# label.place(x=10,y=50)
# x=10
# y=140
# for lis in list:
#     com = lambda x=lis: logic(x)
#     Button(text=lis, bg='white',font=('Consolas',15), command = com).place(x=x, y=y, width=115, height = 79)
#     x+=117
#     if x>400:
#         x=10
#         y+=81
# root.mainloop()