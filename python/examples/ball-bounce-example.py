from tkinter import *
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
        self.shape = canvas.create_oval(0, 0, SIZE, SIZE, fill=color)
        self.speedx = 9 # changed from 3 to 9
        self.speedy = 9 # changed from 3 to 9
        self.active = True
        self.move_active()

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

ball = Ball()


class FpsIndicator:
    def __init__(self, master):
        self.textBox = Text(master, height=1, width=8)
        self.fpsStart = time.time()
        self.current_fps = 0
        self.last_tick_num = 0

    def pack(self):
        self.textBox.pack(side=RIGHT)
        self.textBox.insert(END, "...")

    def update_fps(self, tick_num):
        now = time.time()
        if now > self.fpsStart + 1:
            if self.last_tick_num == 0:
                self.last_tick_num = tick_num
                self.fpsStart = now
            else:
                self.current_fps = (tick_num - self.last_tick_num) / (now - self.fpsStart)
                self.textBox.delete('1.0', END)
                self.textBox.insert(END, f"{self.current_fps:.2f}fps")

                self.last_tick_num = tick_num
                self.fpsStart = now

# Use
global tickNum
tickNum = 0

def cycle():
    global tickNum
    tickNum += 1
    fpsIndicator.update_fps(tickNum)
    tk.after(5, cycle)


fpsIndicator = FpsIndicator(tk)
fpsIndicator.pack()
tk.after(0, cycle)




tk.mainloop()