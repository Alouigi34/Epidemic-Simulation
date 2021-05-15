import HelperFunctions as hf


# Ανακλαστικός πράκτορας τεχνητής νοημοσύνης
class ReflexAgent:
    def __init__(self, canvas, state, radius, color):
        self.canvas = canvas
        self.radius = radius
        self.state = state
        self.x1 = self.state[0] - self.radius
        self.y1 = self.state[1] - self.radius
        self.x2 = self.state[0] + self.radius
        self.y2 = self.state[1] + self.radius
        self.color = color
        self.circle = self.canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2, fill=self.color)

        self.home_state = state     # Η κατάσταση όπου 'γεννιέται' ο πράκτορας.
        self.next_state = self.state

        self.reached_destination = False # Η μεταβλητή στην οποία αποθηκεύεται αν έφτασε ο πράκτορας στον προορισμό του

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
        successor_states = hf.neighbor_states(self.state)
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

        # Εκτέλεσε τη μετακίνηση.
        self.canvas.move(self.circle, dx, dy)
        self.canvas.tag_raise(self.circle)
        # Πλέον, η τωρινή κατάσταση του πράκτορα είναι αυτή που μέχρι προηγουμένως ήταν η επόμενη.
        self.state = self.next_state
