import SimulationEnvironment as se
from tkinter import *

class Ui:
    ui_elements = []

    def __init__(self, window, simulation):
        self.window = window
        self.simulation = simulation

        Ui.ui_elements.append(Button(self.window, text="Start", ))

    def s(self):
        self.simulation.