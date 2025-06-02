import tkinter as tk
from tkinter import ttk
import serial
port="COM1"
baudrate = 9600
ser=serial.Serial(port, baudrate=baudrate)
# Функция для обновления значений переменных
def update_value(val, var):
    var.set(float(val))

# Создание основного окна
root = tk.Tk()
root.title("Слайдеры")

# Создание переменных для хранения значений слайдеров
slider_vars = [tk.DoubleVar() for _ in range(6)]

# Создание и размещение слайдеров
sliders = []
for i in range(6):
    label = ttk.Label(root, text=f"Слайдер {i+1}:")
    label.grid(row=i, column=0, padx=10, pady=10)

    slider = ttk.Scale(root, from_=0, to=100, orient="horizontal",
                       command=lambda val, var=slider_vars[i]: update_value(val, var))
    slider.grid(row=i, column=1, padx=10, pady=10)
    sliders.append(slider)

# Функция для вывода текущих значений переменных
def print_values():
    for i, var in enumerate(slider_vars):
        ser.write(var.get())

# Кнопка для вывода значений
print_button = ttk.Button(root, text="Вывести значения", command=print_values)
print_button.grid(row=6, column=0, columnspan=2, pady=10)

# Запуск основного цикла
root.mainloop()