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


# Η εντολή που θα εκτελεί το κουμπί Masks On/Off
def masks(simulation):
    if simulation.masks:
        if simulation.distance == False:    
            simulation.masks = False
            simulation.masks_helper_var = (simulation.general_transmission)*1000
        else:
            simulation.masks = False
            simulation.masks_helper_var = (simulation.distance_transmission)*1000
    else:
        if simulation.distance == False:
            simulation.masks = True
            simulation.masks_helper_var = (simulation.mask_transmission)*1000
        else:
            simulation.masks = True
            simulation.masks_helper_var = ((simulation.distance_transmission)*(simulation.mask_transmission))*1000



# Η εντολή που θα εκτελεί το κουμπί Keep distances On/Off
def distance(simulation):
    if simulation.distance:
        if simulation.masks == False:    
            simulation.distance = False
            simulation.masks_helper_var = (simulation.general_transmission)*1000
        else:
            simulation.distance = False
            simulation.masks_helper_var = (simulation.mask_transmission)*1000
    else:
        if simulation.masks == False:
            simulation.distance = True
            simulation.masks_helper_var = (simulation.distance_transmission)*1000
        else:
            simulation.distance = True
            simulation.masks_helper_var = ((simulation.distance_transmission)*(simulation.mask_transmission))*1000



# Η εντολή που θα εκτελεί το κουμπί Lockdown On/Off
def lockdown(simulation):
    if simulation.lockdown:
        simulation.lockdown = False
        for i in simulation.agent_list:
            i.in_lockdown = False
    else:
        simulation.lockdown = True
        for i in simulation.agent_list:
            i.in_lockdown = True
