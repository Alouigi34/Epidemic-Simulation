import math


# Συνάρτηση εύρεσης ελάχιστης ευκλείδιας απόστασης από μία κατάσταση προορισμού σε μία κατάσταση στόχου.
def min_distance(start_state, goal_state):
    return math.sqrt((start_state[0] - goal_state[0])**2 + (start_state[1] - goal_state[1])**2)


# Συνάρτηση εύρεσης γειτονικών καταστάσεων μίας οποιασδήποτε κατάστασης.
def neighbor_states(state):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            x = state[0]+i
            y = state[1]+j
            if x >= 0 and y >= 0:
                neighbors.append((x, y))
    return neighbors
