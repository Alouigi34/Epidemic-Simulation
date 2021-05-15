import SimulationEnvironment as se
from tkinter import *
from tkinter.ttk import *
from uiFunctions import *

class Ui:
    # H συνάρτηση που αρχικοποιεί το UI
    def __init__(self, simulation, window):
        # Δημιουργία του κουμπιού Pause και Play

        self.pause_image = PhotoImage(file = r"images/pause.png")
        self.play_image = PhotoImage(file = r"images/play.png")
        self.stop_image = PhotoImage(file = r"images/stop.png")

        self.images = [self.play_image, self.pause_image]
        self.place = 1

        pause_button = Button(window, text="Play", image=self.play_image, command=lambda: pause(simulation, pause_button, self))
        pause_button.pack()
        pause_button.place(x=simulation.canvas_size[0] - simulation.ui_space + 30, y=simulation.canvas_size[1] // 8)
        
        # Δημιουργία του κουμπιού Start
        stop_button = Button(window, text="Stop", image=self.stop_image, command=lambda: stop(simulation))
        stop_button.pack()
        stop_button.place(x=simulation.canvas_size[0] - simulation.ui_space + simulation.ui_space // 3, y=simulation.canvas_size[1] // 8)