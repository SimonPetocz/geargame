import sys
from tkinter import *
from tkinter import ttk
import time

WIDTH = 800
HEIGHT = 500
SIZE = 50
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="grey")
canvas.pack()
color = 'black'


class Ball:
    def __init__(self):
        self.shape = canvas.create_oval(WIDTH/2, HEIGHT/2, SIZE, SIZE, fill=color)
        self.speedx = 1 # changed from 3 to 9
        self.speedy = 1.1 # changed from 3 to 9
        self.active = True

    def ball_update(self):
        canvas.move(self.shape, self.speedx, self.speedy)
        pos = canvas.coords(self.shape)
        if pos[2] >= WIDTH or pos[0] <= 0:
            self.speedx *= -1
        if pos[3] >= HEIGHT or pos[1] <= 0:
            self.speedy *= -1

    def move_active(self):
        if self.active:
            self.ball_update()
            tk.after(10, self.move_active) # changed from 10ms to 30ms

    def move(self, key):
        if(key.keysym=="Up"):
            canvas.move(self.shape, 0, -5)
        if(key.keysym=="Right"):
            canvas.move(self.shape, 5, 0)
        if(key.keysym=="Down"):
            canvas.move(self.shape, 0, 5)
        if(key.keysym=="Left"):
            canvas.move(self.shape, -5, 0)
        

ball = Ball()


def close_win(e):
   tk.destroy()


tk.bind('<Up>', lambda e: ball.move(e))

tk.bind('<Escape>', lambda e: close_win(e))

tk.mainloop()