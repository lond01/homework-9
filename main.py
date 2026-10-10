
import tkinter as tk
import random
from tkinter import messagebox

window = tk.Tk()
window.title("Вгадай число")
window.geometry("350x300")

number = random.randint(1, 10)

label = tk.Label(
    window,
    text="Вгадай число від 1 до 10!"
)
label.pack(pady=15)

entry = tk.Entry(window)
entry.pack()

def check_number():
    global number

    try:
        guess = int(entry.get())

        if guess == number:
            messagebox.showinfo("Перемога", "Ти вгадав!")
        elif guess < number:
            messagebox.showinfo("Підказка", "Моє число більше!")
        else:
            messagebox.showinfo("Підказка", "Моє число менше!")

    except ValueError:
        messagebox.showerror(
            "Помилка",
            "Введи ціле число!"
        )

button = tk.Button(
    window,
    text="Перевірити",
    command=check_number
)
button.pack(pady=15)

window.mainloop()

