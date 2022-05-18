import tkinter as tk
from tkinter import messagebox

import simplex

win = tk.Tk()

win.title("Задача максимизации (№9)")
win.geometry("400x200")

x1 = tk.Entry(win, width=5, justify="center")
x1.insert(0, "2")
x2 = tk.Entry(win, width=5, justify="center")
x2.insert(0, "11")
b = tk.Entry(win, width=5, justify="center")
b.insert(0, "38")

x1_1 = tk.Entry(win, width=5, justify="center")
x1_1.insert(0, "1")
x2_1 = tk.Entry(win, width=5, justify="center")
x2_1.insert(0, "1")
b_1 = tk.Entry(win, width=5, justify="center")
b_1.insert(0, "7")

x1_2 = tk.Entry(win, width=5, justify="center")
x1_2.insert(0, "4")
x2_2 = tk.Entry(win, width=5, justify="center")
x2_2.insert(0, "-5")
b_2 = tk.Entry(win, width=5, justify="center")
b_2.insert(0, "5")

o1 = tk.Entry(win, width=5, justify="center")
o1.insert(0, "-1")
o2 = tk.Entry(win, width=5, justify="center")
o2.insert(0, "-1")

tk.Label(win, text="x1").grid(row=0, column=0)
tk.Label(win, text="x2").grid(row=0, column=1)
tk.Label(win, text="b").grid(row=0, column=5)


def run():
    arr = [
        [
            float(x1.get()),
            float(x2.get()),
            1,
            0,
            0,
            float(b.get()),
        ],
        [
            float(x1_1.get()),
            float(x2_1.get()),
            0,
            1,
            0,
            float(b_1.get()),
        ],
        [
            float(x1_2.get()),
            float(x2_2.get()),
            0,
            0,
            1,
            float(b_2.get()),
        ],
    ]
    arr_q = [
        float(o1.get()),
        float(o2.get()),
        0,
        0,
        0,
    ]
    obj, rel = simplex.solve(arr, arr_q)
    x1_var = next(x for x in rel if x[0] == 1)
    x2_var = next(x for x in rel if x[0] == 2)
    messagebox.showinfo(
        "Ответ",
        f"F = {obj}\nx1 = {x1_var[1]}\nx2 = {x2_var[1]}",
    )


btn = tk.Button(win, text="Решить", command=run)

x1.grid(row=1, column=0)
x2.grid(row=1, column=1)
b.grid(row=1, column=5)

x1_1.grid(row=2, column=0)
x2_1.grid(row=2, column=1)
b_1.grid(row=2, column=5)

x1_2.grid(row=3, column=0)
x2_2.grid(row=3, column=1)
b_2.grid(row=3, column=5)

o1.grid(row=4, column=0)
o2.grid(row=4, column=1)

btn.grid(row=5, column=0)

win.mainloop()
