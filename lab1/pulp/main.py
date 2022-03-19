import pulp as p
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()

win.title('Максимизация прибыли предприятия')
win.geometry('300x300')

tk.Label(win, text='Цена A').grid(row=0)
tk.Label(win, text='Цена B').grid(row=1)
tk.Label(win, text='Максимальное кол-во A').grid(row=2)
tk.Label(win, text='Максимальное кол-во B').grid(row=3)
tk.Label(win, text='Пропускная способность').grid(row=4)

a_price = tk.Entry(win)
b_price = tk.Entry(win)
a_max_count = tk.Entry(win)
b_max_count = tk.Entry(win)
bandwidth = tk.Entry(win)

a_price.grid(row=0, column=1)
b_price.grid(row=1, column=1)
a_max_count.grid(row=2, column=1)
b_max_count.grid(row=3, column=1)
bandwidth.grid(row=4, column=1)


def solve():
    a_price_val = float(a_price.get())
    b_price_val = float(b_price.get())
    a_max_count_val = int(a_max_count.get())
    b_max_count_val = int(b_max_count.get())
    bandwidth_val = int(bandwidth.get())
    model = p.LpProblem('Максимальная прибыль', p.LpMaximize)
    
    A = p.LpVariable('1', lowBound=0, cat='integer')
    B = p.LpVariable('2', lowBound=0, cat='integer')
    
    model += a_price_val * A + b_price_val * B
    model += A >= 0
    model += A <= a_max_count_val
    model += B >= 0
    model += B <= b_max_count_val
    model += A + B <= bandwidth_val

    model.solve()
    
    messagebox.showinfo(
            'Ответ', 
            f'A = {A.varValue}\nB = {B.varValue}\nMax = {a_price_val * A.varValue + b_price_val * B.varValue}')


btn = tk.Button(win, text="Решить", width=10, height=5, command=solve)

btn.grid(row=5)

win.mainloop()
