import SimulationEnvironment as se
from tkinter import *
from uiFunctions import *

# H συνάρτηση που αρχικοποιεί το UI
def initUI(simulation, window):
    # Δημιουργία του κουμπιού Start
    start_button = Button(window, text="Start", command=lambda: start(simulation))
    start_button.pack()
    start_button.place(x=simulation.canvas_size[0] - simulation.ui_space + 30, y=simulation.canvas_size[1] // 8)

    # Δημιουργία του κουμπιού Pause
    pause_button = Button(window, text="Pause", command=lambda: pause(simulation, pause_button))
    pause_button.pack()
    pause_button.place(x=simulation.canvas_size[0] - simulation.ui_space + simulation.ui_space // 3, y=simulation.canvas_size[1] // 8)