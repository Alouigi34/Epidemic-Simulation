from tkinter import *

# this is a test change


class Ball:
    def __init__(self, canvas, x1, y1, x2, y2, delta_x, delta_y, color):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.canvas = canvas
        self.color = color
        self.circle = canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2, fill=self.color)

    def move_ball(self):
        if self.canvas.coords(self.circle)[0] <= 250 and self.canvas.coords(self.circle)[1] <= 250:
            self.canvas.move(self.circle, self.delta_x, self.delta_y)
            self.canvas.after(50, self.move_ball)


# main
window = Tk()
window.title("Moving balls")
window.resizable(False, False)

canvas = Canvas(window, width=300, height=300)
canvas.pack()

ball1 = Ball(canvas, 10, 10, 30, 30, 5, 5, "red")
ball2 = Ball(canvas, 60, 60, 80, 80, 4, 4, "green")

ball1.move_ball()
ball2.move_ball()

window.mainloop()
