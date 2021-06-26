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
        self.pause_image = PhotoImage(file=r"images/pause.png")
        self.play_image = PhotoImage(file=r"images/play.png")
        self.stop_image = PhotoImage(file=r"images/stop.png")
        # Μετρητής για τους υγιείς
        self.healthy_counter = Label(
            window, text=f"Healhty: {self.simulation.population} (100%)")
        self.healthy_counter.config(font=("Arial", 13))
        self.healthy_counter.pack()
        self.healthy_counter.place(
            x=self.simulation.canvas_size[0] - self.simulation.ui_space + 30, y=self.simulation.canvas_size[1] // 8 + 40)

        self.date_counter = Label(window, text="Day: 0")
        self.date_counter.config(font=("Arial", 16))
        self.date_counter.pack()
        self.date_counter.place(
            x=self.simulation.canvas_size[0]-self.simulation.ui_space+30, y=self.simulation.canvas_size[1]//8 - 60)

        # Μετρητής για τους αρρώστους
        self.sick_counter = Label(window, text=f"Sick: 0 (0%)")
        self.sick_counter.config(font=("Arial", 13))
        self.sick_counter.pack()
        self.sick_counter.place(
            x=self.simulation.canvas_size[0] - self.simulation.ui_space + 30, y=self.simulation.canvas_size[1] // 8 + 80)

        # Δημιουργία ετικέτας για μάσκες
        self.images = [self.play_image, self.pause_image]
        self.place = 1
        self.mask_label = Label(window, text=f"off")
        self.mask_label.config(font=("Arial", 13))
        self.mask_label.pack()
        self.mask_label.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                              self.simulation.ui_space // 3 + 50, y=self.simulation.canvas_size[1] // 8 + 180)
        # Δημιουργία ετικέτας αποστάσεων
        self.distance_label = Label(window, text=f"off")
        self.distance_label.config(font=("Arial", 13))
        self.distance_label.pack()
        self.distance_label.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                                  self.simulation.ui_space // 3 + 90, y=self.simulation.canvas_size[1] // 8 + 220)
        # Δημιουργία του κουμπιού Pause και Play
        pause_button = Button(self.window, text="Play", image=self.play_image,
                              command=lambda: pause(self.simulation, pause_button, self))
        pause_button.pack()
        pause_button.place(
            x=self.simulation.canvas_size[0] - self.simulation.ui_space + 30, y=self.simulation.canvas_size[1] // 8)

        # Δημιουργία του κουμπιού Start
        stop_button = Button(self.window, text="Stop",
                             image=self.stop_image, command=lambda: stop(self.simulation))
        stop_button.pack()
        stop_button.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                          self.simulation.ui_space // 3, y=self.simulation.canvas_size[1] // 8)
        # Δημιουργία του Κουμπιού masks on/off
        mask_button = Button(self.window, text="Masks On/Off",
                             command=lambda: masks(self.simulation))
        mask_button.pack()
        mask_button.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                          self.simulation.ui_space // 3 - 40, y=self.simulation.canvas_size[1] // 8 + 180)

        # Δημιουργία του Κουμπιού distances on/off
        distance_button = Button(self.window, text="Keep Distances On/Off",
                                 command=lambda: distance(self.simulation))
        distance_button.pack()
        distance_button.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                              self.simulation.ui_space // 3 - 40, y=self.simulation.canvas_size[1] // 8 + 220)

    def update_counters(self):
        self.date_counter["text"] = f"Day: {str(self.simulation.day)}"
        self.sick_counter["text"] = f"Sick: {self.simulation.sick_population} ({round(self.simulation.sick_population / self.simulation.population * 100, 1)}%)"
        self.healthy_counter[
            "text"] = f"Healthy: {self.simulation.population - self.simulation.sick_population} ({round((self.simulation.population - self.simulation.sick_population) / self.simulation.population * 100, 1)}%)"
        if self.simulation.masks == True:
            self.mask_label["text"] = "on"
        else:
            self.mask_label["text"] = "off"

        if self.simulation.distance == True:
            self.distance_label["text"] = "on"
        else:
            self.distance_label["text"] = "off"
