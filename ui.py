import SimulationEnvironment as se
from tkinter import *
from tkinter.ttk import *
from uiFunctions import *
import time

class Ui:
    # H συνάρτηση που αρχικοποιεί το UI
    def __init__(self, simulation, window):
        self.simulation = simulation
        self.window = window

        # Εικόνες που θα χρησιμοποιήσουμε
        self.pause_image = PhotoImage(file = r"images/pause.png")
        self.play_image = PhotoImage(file = r"images/play.png")
        self.stop_image = PhotoImage(file = r"images/stop.png")

        # Μετρητής των ημερών
        self.date_counter = Label(window, text="Day: 0")
        self.date_counter.config(font = ("Arial", 13))
        self.date_counter.pack()
        self.date_counter.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space + 30, y=self.simulation.canvas_size[1] // 8)

        # Μετρητής για τους υγιείς
        self.healthy_counter = Label(window, text=f"Healhty: {self.simulation.population} (100%)")
        self.healthy_counter.config(font = ("Arial", 13))
        self.healthy_counter.pack()
        self.healthy_counter.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space + 30, y=self.simulation.canvas_size[1] // 8 + 80)
        
        # Μετρητής για τους αρρώστους
        self.sick_counter = Label(window, text = f"Sick: 0 (0%)")
        self.sick_counter.config(font = ("Arial", 13))
        self.sick_counter.pack()
        self.sick_counter.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space + 30, y=self.simulation.canvas_size[1] // 8 + 120)
        
        # Δημιουργία του κουμπιού Pause και Play
        self.images = [self.play_image, self.pause_image]
        self.place = 1

        pause_button = Button(self.window, text="Play", image=self.play_image, command=lambda: pause(self.simulation, pause_button, self))
        pause_button.pack()
        pause_button.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space + 30, y=self.simulation.canvas_size[1] // 8 + 40)
        
        # Δημιουργία του κουμπιού Start
        stop_button = Button(self.window, text="Stop", image=self.stop_image, command=lambda: stop(self.simulation))
        stop_button.pack()
        stop_button.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space + self.simulation.ui_space // 3, y=self.simulation.canvas_size[1] // 8 + 40)

    def update_counters(self):
        # Ενημέρωσε τους μετρητές
        self.sick_counter["text"] = f"Sick: {self.simulation.sick_population} ({round(self.simulation.sick_population / self.simulation.population * 100, 1)}%)"
        self.healthy_counter["text"] = f"Healthy: {self.simulation.population - self.simulation.sick_population} ({round((self.simulation.population - self.simulation.sick_population) / self.simulation.population * 100, 1)}%)"
        self.date_counter["text"] = f"Day: {str(self.simulation.day)}"