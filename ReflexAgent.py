import HelperFunctions as hf
from tkinter import *
import random

# Ανακλαστικός πράκτορας τεχνητής νοημοσύνης
class ReflexAgent:
    def __init__(self, simENV, state, color, condition):
        self.simENV = simENV
        self.canvas = simENV.canvas
        self.radius = simENV.agent_size
        self.state = state
        self.x1 = self.state[0] - self.radius
        self.y1 = self.state[1] - self.radius
        self.x2 = self.state[0] + self.radius
        self.y2 = self.state[1] + self.radius
        self.color = color
        self.condition = condition
        self.circle = self.canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2, fill=self.color)

        self.home_state = state     # Η κατάσταση όπου 'γεννιέται' ο πράκτορας.
        self.next_state = self.state

        # Η μεταβλητή στην οποία αποθηκεύεται αν έφτασε ο πράκτορας στον προορισμό του
        self.reached_destination = False

        # Η κατάσταση όπου βρίσκεται το κατάστημα που προτιμάει.
        self.pref_shop_state = (None, None)

    # Μέθοδος εύρεσης του καταστήματος προτίμησης βάσει τοποθεσίας.
    def preferred_shop(self, shop_list):
        min_d = float('inf')
        pref_shop_state = self.state
        # Για κάθε κατάστημα στην προσομοίωση υπολόγισε την απόσταση του πράκτορα από αυτό και κράτα αυτό με την μικρότερη.
        for shop in shop_list:
            d = hf.min_distance(self.state, shop.state)
            if d < min_d:
                min_d = d
                pref_shop_state = shop.state
        return pref_shop_state

    # Μέθοδος εύρεσης της επόμενης κατάστασης στην οποία σκοπεύει να μετακινηθεί ο πράκτορας
    def find_next_state(self, goal_state):
        successor_states = hf.neighbor_states(self.state, 1, (len(self.simENV.agent_grid), len(self.simENV.agent_grid[0])))
        min_cost = float('inf')
        next_state = self.state
        # Για κάθε γειτονική κατάσταση από την τωρινή του πράκτορα υπολόγισε το κόστος μετακίνησης σε αυτήν
        # βάσει μίας συνάρτησης αξιολόγησης. Ο πράκτορας επιλέγει την μετακίνηση με το μικρότερο κόστος.
        for succesor in successor_states:
            cost = self.evaluation_function(succesor, goal_state)
            if cost < min_cost:
                min_cost = cost
                next_state = succesor
        self.next_state = next_state

    # Η συνάρτηση αξιολόγησης (προς το παρόν ο πράκτορας αξιολογεί βάσει ελάχιστης απόστασης από τον στόχο).
    def evaluation_function(self, start_state, goal_state):
        return hf.min_distance(start_state, goal_state)

    # Η μέθοδος που ελέγχει αν ο πράκτορας έχει μολυνθεί από την ασθένεια
    def update_conditions(self):
        size = (len(self.simENV.agent_grid), len(self.simENV.agent_grid[0]))

        # Για κάθε κοντινή κατάστηση από την τωρινή του πράκτορα δες αν υπάρχουν άλλοι πράκτορες σε αυτές.
        # Αν ναι και κάποιος από αυτούς είναι μολυσμένος, μολύνσου και εσύ. Αν όχι αλλά εσύ είσαι ήδη μολυσμένος, μόλυνέ τους. Αλλιώς, συνέχισε κανονικά.
        neighbors = hf.neighbor_states(self.state, 5, size)
        possibility_range = [0, 100]

        for i in neighbors:
            for j in self.simENV.agent_grid[i[0]] [i[1]]:
                if random.randint(possibility_range[0], possibility_range[1]) == 2:
                    if j.condition == "sick" and self.condition == "healthy":
                        self.canvas.itemconfig(self.circle, fill = "red")
                        self.condition = "sick"
                        self.simENV.sick_population += 1

                    elif self.condition == "sick" and j.condition == "healthy":
                        self.canvas.itemconfig(j.circle, fill = "red")
                        j.condition = "sick"
                        self.simENV.sick_population += 1
                        
                    return True
        return False

    # Η μέθοδος αυτή καλείται για να ανανεώσει την κατάσταση του πράκτορα.
    def update(self):
        dx = 0  # Μετατόπιση στον άξονα x
        dy = 0  # Μετατόπιση στον άξονα y

        # Αν η τετμημένη του πράκτορα είναι μεγαλύτερη από αυτήν της επόμενης κατάστασής του τότε
        # μετατόπισέ τον προς τα αριστερά κατά 1 pixel.
        if self.state[0] > self.next_state[0]:
            dx = -1
        # Αλλιώς αν η τετμημένη του πράκτορα είναι μικρότερη από αυτήν της επόμενης κατάστασής του τότε
        # μετατόπισέ τον προς τα δεξιά κατά 1 pixel.
        elif self.state[0] < self.next_state[0]:
            dx = 1

        # Αν η τεταγμένη του πράκτορα είναι μεγαλύτερη από αυτήν της επόμενης κατάστασής του τότε
        # μετατόπισέ τον προς τα πάνω κατά 1 pixel.
        if self.state[1] > self.next_state[1]:
            dy = -1
        # Αν η τεταγμένη του πράκτορα είναι μικρότερη από αυτήν της επόμενης κατάστασής του τότε
        # μετατόπισέ τον προς τα κάτω κατά 1 pixel.
        elif self.state[1] < self.next_state[1]:
            dy = 1

        # (Προφανώς, αν τα παραπάνω δεν ισχύουν τότε ο πράκτορας θα παραμείνει σταθερός.)

        # Εκτέλεσε τη μετακίνηση και ανανέωσε το grid.
        self.canvas.move(self.circle, dx, dy)
        self.canvas.tag_raise(self.circle)

        self.simENV.agent_grid[self.state[0]][self.state[1]].remove(self)
        self.simENV.agent_grid[self.next_state[0]
                               ][self.next_state[1]].append(self)

        # Πλέον, η τωρινή κατάσταση του πράκτορα είναι αυτή που μέχρι προηγουμένως ήταν η επόμενη.
        self.state = self.next_state
