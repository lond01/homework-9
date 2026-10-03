import tkinter as tk

bomb = 100
score = 0
press_return = True

root = tk.Tk()
root.title("Bomb Clicker")
root.geometry("600x650+700+150")
root.resizable(False, False)

label_1 = tk.Label(
    root,
    text="Press [ENTER] to start the game",
    font=("Comic Sans MS", 14)
)
label_1.pack(pady=10)

fuse_label = tk.Label(
    root,
    text=f"Fuse: {bomb}",
    font=("Comic Sans MS", 16)
)
fuse_label.pack()

score_label = tk.Label(
    root,
    text=f"Score: {score}",
    font=("Comic Sans MS", 16)
)
score_label.pack()

img_1 = tk.PhotoImage(file="bomb_1.png").subsample(3, 3)
img_2 = tk.PhotoImage(file="bomb_2.png").subsample(3, 3)
img_3 = tk.PhotoImage(file="bomb_3.png").subsample(3, 3)
img_4 = tk.PhotoImage(file="bomb_4.png").subsample(3, 3)

bomb_label = tk.Label(root, image=img_1)
bomb_label.pack(pady=20)


def update_display():
    if bomb >= 80:
        bomb_label.config(image=img_1)
    elif bomb >= 50:
        bomb_label.config(image=img_2)
    elif bomb > 0:
        bomb_label.config(image=img_3)
    else:
        bomb_label.config(image=img_4)

    fuse_label.config(text=f"Fuse: {bomb}")
    score_label.config(text=f"Score: {score}")

    root.after(100, update_display)


def decrease_bomb():
    global bomb
    global press_return

    if press_return:
        return

    bomb -= 1

    if bomb <= 0:
        bomb = 0
        press_return = True

        label_1.config(text="BANG! GAME OVER!")
        click_button.config(text="PLAY AGAIN")

        return

    root.after(100, decrease_bomb)


def increase_score():
    global score

    if press_return:
        return

    score += 1
    root.after(1000, increase_score)


def click_bomb():
    global bomb
    global score

    if press_return:
        return

    bomb += 5

    if bomb > 100:
        bomb = 100

    score += 1

    label_1.config(text="Good click!")


def start(event=None):
    global bomb
    global score
    global press_return

    if not press_return:
        return

    bomb = 100
    score = 0
    press_return = False

    label_1.config(text="Клікай по бомбі!")

    click_button.config(text="CLICK THE BOMB!")

    decrease_bomb()
    increase_score()


click_button = tk.Button(
    root,
    text="CLICK THE BOMB!",
    width=20,
    height=2,
    font=("Comic Sans MS", 16, "bold"),
    command=click_bomb
)
click_button.pack(pady=15)

restart_button = tk.Button(
    root,
    text="RESTART",
    width=12,
    font=("Comic Sans MS", 12),
    command=start
)
restart_button.pack()

root.bind("<Return>", start)

update_display()

root.mainloop()
