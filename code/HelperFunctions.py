import math
import os

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
    here = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(here, file)
    with open(filename, "r") as virus:
        virus = virus.read().split("\n")
        for i in virus:
            if i == "":
                virus.remove(i)
        virus.remove(virus[2])
        data["name"] = virus[0][5:].translate({ord(' '): None})
        symptoms = virus[1][15:].split(",")
        for i in range(len(symptoms)):
            symptoms[i] = symptoms[i].translate({ord(' '): None})
            symptoms[i] = symptoms[i].translate({ord('-'): ord(' ')})
        data["symptoms"] = symptoms
        data["general_transmission"] = float(
            virus[2][8: len(virus[2]) - 1]) / 100
        print("General transmission: ", data["general_transmission"])
        data["mask_transmission"] = float(
            virus[3][10: len(virus[3]) - 1]) / 100
        print("With mask: ", data["mask_transmission"])
        data["distance_transmission"] = float(
            virus[4][17: len(virus[4]) - 1]) / 100
        print("With distancing: ", data["distance_transmission"])
        data["recovery_rate"] = int(virus[5][14: len(virus[5]) - 4]) + 1
        print("Recovery rate: ", data["recovery_rate"]-1, "days")
        data["mortality_rate"] = float(virus[6][15: len(virus[6]) - 1]) / 100
        print("Mortality rate: ", data["mortality_rate"])
        return data
