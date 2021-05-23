import math


# Συνάρτηση εύρεσης ελάχιστης ευκλείδιας απόστασης από μία κατάσταση προορισμού σε μία κατάσταση στόχου.
def min_distance(start_state, goal_state):
    return math.sqrt((start_state[0] - goal_state[0])**2 + (start_state[1] - goal_state[1])**2)


# Συνάρτηση εύρεσης γειτονικών καταστάσεων μίας οποιασδήποτε κατάστασης.
def neighbor_states(state, start_x, stop_x, start_y, stop_y, size):
    neighbors = []
    for i in range(start_x, stop_x):
        for j in range(start_y, stop_y):
            x = state[0]+i
            y = state[1]+j
            if x >= 0 and x <= (size[0] - 1) and y >= 0 and y <= (size[1] - 1):
                neighbors.append((x, y))
    return neighbors
