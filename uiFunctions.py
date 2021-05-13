from tkinter import *

# Η εντολή που θα εκτελεί το κουμπί Start
def start(simulation):
    simulation.run()
    simulation.has_started = True

# Η εντολή που θα εκτελεί το κουμπί Pause
def pause(simulation, btn):
    simulation.is_paused = not simulation.is_paused

    if btn["text"] == "Pause":
        btn["text"] = "Unpause"
    elif btn["text"] == "Unpause":
        btn["text"] = "Pause"
