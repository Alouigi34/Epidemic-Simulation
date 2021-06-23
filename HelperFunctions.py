import math
from os import register_at_fork


# Συνάρτηση εύρεσης ελάχιστης ευκλείδιας απόστασης από μία κατάσταση προορισμού σε μία κατάσταση στόχου.
def min_distance(start_state, goal_state):
    return math.sqrt((start_state[0] - goal_state[0])**2 + (start_state[1] - goal_state[1])**2)


# Συνάρτηση εύρεσης γειτονικών καταστάσεων μίας οποιασδήποτε κατάστασης.
def neighbor_states(state, _range, grid_size):
    neighbors = []

    for i in range(-_range, _range+1):
        for j in range(-_range, _range+1):
            x = state[0]+i
            y = state[1]+j
            if x >= 0 and x <= (grid_size[0] - 1) and y >= 0 and y <= (grid_size[1] - 1):
                neighbors.append((x, y))
    return neighbors

# Συνάρτηση που διαβάζει το αρχείο txt με τα δεδομένα του ιού
def read_virus_file(file):
    data = {}

    file = open(file, "r")
    file = file.read().split("\n")

    for i in file:
        if i == "":
            file.remove(i)
    file.remove(file[2])

    data["name"] = file[0][6:]
    data["symptoms"] = file[1][16:].split(", ")

    data["general_transmission"] = float(file[2][9 : len(file[2]) - 1])  / 100
    data["mask_transmission"] = float(file[3][11 : len(file[3]) - 1])  / 100
    data["distance_transmission"] = float(file[4][18: len(file[4]) - 1])  / 100

    data["recovery_rate"] = int(file[5][15 : len(file[5]) - 4])
    data["mortality_rate"] = float(file[6][16 : len(file[6]) - 1])  / 100
    
    return data