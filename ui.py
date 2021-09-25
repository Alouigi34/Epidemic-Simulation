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
        self.images = [self.play_image, self.pause_image]
        self.place = 1

        # Μετρητής για τους υγιείς
        self.healthy_counter = Label(
            window, bg="gray5", fg="turquoise3", text=f"Healhty: {self.simulation.healthy_population} (100%)")
        self.healthy_counter.config(font=("Arial", 13))
        self.healthy_counter.pack()
        self.healthy_counter.place(
            x=self.simulation.canvas_size[0] - self.simulation.ui_space + 30, y=self.simulation.canvas_size[1] // 8 + 40)

        # Μετρητής για τους αρρώστους
        self.sick_counter = Label(
            window, bg="gray5", fg="firebrick1", text=f"Sick: 0 (0%)")
        self.sick_counter.config(font=("Arial", 13))
        self.sick_counter.pack()
        self.sick_counter.place(
            x=self.simulation.canvas_size[0] - self.simulation.ui_space + 30, y=self.simulation.canvas_size[1] // 8 + 80)

        # Μετρητής για τους recovered
        self.recovered_counter = Label(
            window, bg="gray5", fg="chartreuse3", text=f"Recovered: {self.simulation.recovered_population} ({round(self.simulation.recovered_population / self.simulation.population * 100, 1)}%)")
        self.recovered_counter.config(font=("Arial", 13))
        self.recovered_counter.pack()
        self.recovered_counter.place(
            x=self.simulation.canvas_size[0] - self.simulation.ui_space + 30, y=self.simulation.canvas_size[1] // 8 + 120)

        # Μετρητής για τους deceased
        self.deceased_counter = Label(
            window, bg="gray5", fg="white", text=f"Deceased: {self.simulation.deceased_population} ({round(self.simulation.deceased_population / self.simulation.population * 100, 1)}%)")
        self.deceased_counter.config(font=("Arial", 13))
        self.deceased_counter.pack()
        self.deceased_counter.place(
            x=self.simulation.canvas_size[0] - self.simulation.ui_space + 30, y=self.simulation.canvas_size[1] // 8 + 160)

        self.date_counter = Label(
            window, bg="gray5", fg="white", text="Day: 0")
        self.date_counter.config(font=("Arial", 16))
        self.date_counter.pack()
        self.date_counter.place(
            x=self.simulation.canvas_size[0]-self.simulation.ui_space+30, y=self.simulation.canvas_size[1]//8 - 60)

        # Μετρητής των ημερών
        self.date_counter = Label(
            window, bg="gray5", fg="white", text="Day: 0")
        self.date_counter.config(font=("Arial", 16))
        self.date_counter.pack()
        self.date_counter.place(
            x=self.simulation.canvas_size[0]-self.simulation.ui_space+30, y=self.simulation.canvas_size[1]//8 - 60)

        # Δημιουργία ετικέτας για μάσκες
        self.mask_label = Label(window, bg="gray5", fg="white", text=f"Off")
        self.mask_label.config(font=("Arial", 13))
        self.mask_label.pack()
        self.mask_label.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                              self.simulation.ui_space // 3 + 50, y=self.simulation.canvas_size[1] // 8 + 220)

        # Δημιουργία ετικέτας lockdown
        self.lockdown_label = Label(
            window, bg="gray5", fg="white", text=f"Off")
        self.lockdown_label.config(font=("Arial", 13))
        self.lockdown_label.pack()
        self.lockdown_label.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                                  self.simulation.ui_space // 3 + 75, y=self.simulation.canvas_size[1] // 8 + 260)

        # Δημιουργία ετικέτας αποστάσεων
        self.distance_label = Label(
            window, bg="gray5", fg="white", text=f"Off")
        self.distance_label.config(font=("Arial", 13))
        self.distance_label.pack()
        self.distance_label.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                                  self.simulation.ui_space // 3 + 100, y=self.simulation.canvas_size[1] // 8 + 300)

        # Δημιουργία του κουμπιού Pause και Play
        pause_button = Button(self.window, bg="gray5", text="Play", image=self.play_image,
                              command=lambda: pause(self.simulation, pause_button, self))
        pause_button.pack()
        pause_button.place(
            x=self.simulation.canvas_size[0] - self.simulation.ui_space + 33, y=self.simulation.canvas_size[1] // 10)

        # Δημιουργία του κουμπιού Stop
        stop_button = Button(self.window, bg="gray5", text="Stop",
                             image=self.stop_image, command=lambda: stop(self.simulation))
        stop_button.pack()
        stop_button.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                          self.simulation.ui_space // 3 + 3, y=self.simulation.canvas_size[1] // 10)
        # Δημιουργία του Κουμπιού masks on/off
        mask_button = Button(self.window, bg="gray5", fg="white", text="Masks On/Off",
                             command=lambda: masks(self.simulation))
        mask_button.pack()
        mask_button.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                          self.simulation.ui_space // 3 - 40, y=self.simulation.canvas_size[1] // 8 + 220)

        # Δημιουργία κουμπιού lockdown
        lockdown_button = Button(self.window, bg="gray5", fg="white", text="Lockdown On/Off",
                                 command=lambda: lockdown(self.simulation))
        lockdown_button.pack()
        lockdown_button.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                              self.simulation.ui_space // 3 - 40, y=self.simulation.canvas_size[1] // 8 + 260)

        # Δημιουργία του Κουμπιού distances on/off
        distance_button = Button(self.window, bg="gray5", fg="white", text="Keep Distances On/Off",
                                 command=lambda: distance(self.simulation))
        distance_button.pack()
        distance_button.place(x=self.simulation.canvas_size[0] - self.simulation.ui_space +
                              self.simulation.ui_space // 3 - 40, y=self.simulation.canvas_size[1] // 8 + 300)

    def update_counters(self):
        self.deceased_counter[
            "text"] = f"Deceased: {self.simulation.deceased_population} ({round(self.simulation.deceased_population / self.simulation.population * 100, 1)}%)"
        self.recovered_counter[
            "text"] = f"Recovered: {self.simulation.recovered_population} ({round(self.simulation.recovered_population / self.simulation.population * 100, 1)}%)"
        self.date_counter["text"] = f"Day: {str(self.simulation.day)}"
        self.sick_counter["text"] = f"Sick: {self.simulation.sick_population} ({round(self.simulation.sick_population / self.simulation.population * 100, 1)}%)"
        self.healthy_counter[
            "text"] = f"Healthy: {self.simulation.healthy_population} ({round(self.simulation.healthy_population/ self.simulation.population * 100, 1)}%)"

        if self.simulation.masks == True:
            self.mask_label["text"] = "On"
        else:
            self.mask_label["text"] = "Off"

        if self.simulation.distance == True:
            self.distance_label["text"] = "On"
        else:
            self.distance_label["text"] = "Off"

        if self.simulation.lockdown == True:
            self.lockdown_label["text"] = "On"
        else:
            self.lockdown_label["text"] = "Off"
