from tkinter import *
import random
import logging
import threading
import time

window = Tk()
# add widgets here

window.title('Reaction Test')
window.geometry("300x200+10+20")
lbl = Label(window, text="Reaction Test", fg='black', font=("Helvetica", 16))
lbl.place(x=60, y=10)

btn = Button(window, text="Start", fg='black', font=("Helvetica", 16))
btn.place(x=100, y=50)

debounce = False

def clicked():
    if lbl.text == "Click!":
        print("a")

def wait():
    time.sleep(random.randint(1, 5))
    window.configure(bg='#00cc00')
    lbl.configure(text="Click!", fg='white', bg='#00cc00')
    debounce = False


def begin(event):
    if not debounce:
        debounce = True
        print(event)
        window.configure(bg='#3366cc')
        lbl.configure(text="Wait for green", fg='white', bg='#3366cc')

        x = threading.Thread(target=wait)
        x.start()


btn.bind("<Button-1>", begin)
window.mainloop()
