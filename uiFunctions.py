from tkinter import *

# Η εντολή που θα εκτελεί το κουμπί Stop


def stop(simulation):
    simulation.destroy()

# Η εντολή που θα εκτελεί το κουμπί Pause και Play


def pause(simulation, btn, ui):

    if not simulation.has_started:
        btn["image"] = ui.images[ui.place]
        simulation.run()
        simulation.has_started = True

    simulation.is_paused = not simulation.is_paused

    if ui.place == 0:
        ui.place = 1
    elif ui.place == 1:
        ui.place = 0

    btn["image"] = ui.images[ui.place]


def masks(simulation):
    if simulation.masks == False:
        simulation.masks = True
        simulation.masks_helper_var = 15
    else:
        simulation.masks = False
        simulation.masks_helper_var = 900


def distance(simulation):
    if simulation.distance:
        simulation.distance = False
    else:
        simulation.distance = True
