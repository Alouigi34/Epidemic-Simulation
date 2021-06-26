import math


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
