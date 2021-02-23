from tkinter import *
import random
import threading
import time
import datetime

window = Tk()
window.title('Reaction Test')
window.geometry("300x200+10+20")
lbl = Label(window, text="Reaction Test", fg='black', font=("Helvetica", 16))
lbl.place(x=60, y=10)

btn = Button(window, text="Start", fg='black', font=("Helvetica", 16))
btn.place(x=100, y=50)

timelbl = Label(window, text="", fg='black', font=("Helvetica", 16))
timelbl.place(x=60, y=100)

global status
status = 0
# 0 idle
# 1 waiting
# 2 measuring
# 3 failed


def wait():
    global status
    status = 1
    time.sleep(random.randint(1, 5))
    if not status == 0:
        status = 2
        global begin
        begin = datetime.datetime.now()
        window.configure(bg='#00cc00')
        lbl.configure(text="Click!", fg='white', bg='#00cc00')
        btn.configure(text="Click!")


def begin(event):
    global status
    if status == 0:
        print(event)
        window.configure(bg='#3366cc')
        lbl.configure(text="Wait for green", fg='white', bg='#3366cc')
        timelbl.configure(text="", fg='white', bg='#3366cc')
        btn.configure(text="Wait...")

        x = threading.Thread(target=wait)
        x.start()
        status = 1

    elif status == 2:
        end = datetime.datetime.now()
        timed = end - begin
        timelbl.configure(text=(int(timed.total_seconds() * 1000), "ms"), fg='white', bg='#00cc00')
        lbl.configure(text="Test finished")
        btn.configure(text="Restart")
        status = 0
    else:
        window.configure(bg='#DD2700')
        lbl.configure(text="You clicked too early!", fg='white', bg='#DD2700')
        timelbl.configure(text="", fg='white', bg='#DD2700')
        btn.configure(text="Restart")
        status = 0


btn.bind("<Button-1>", begin)
window.mainloop()
