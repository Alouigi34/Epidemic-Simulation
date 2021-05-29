from tkinter import *
import random
from typing import Counter
import ReflexAgent as ra
import ui


# Βασικό περιβάλλον προσομοίωσης κοινότητας
class Simulation:
    def __init__(self, canvas_size, population, agent_size, shop_population, sick_population, ui_space=200):
        self.canvas_size = canvas_size
        self.population = population
        self.agent_size = agent_size
        self.shop_population = shop_population
        self.sick_population = sick_population
        self.agent_list = []
        self.shop_list = []
        self.agent_grid = [
            [[] for i in range(canvas_size[1]+1)] for j in range(canvas_size[0]-ui_space+1)]

        self.is_paused = False  # Ελέγχει αν έχει "παγώσει" η προσομοίωση
        self.has_started = False    # Ελέγχει αν έχει ξεκινήσει η προσομοίωση
        self.running = False    # Όσο έχει την τιμή True η προσομοίωση τρέχει

        self.ui_space = ui_space    # Ο χώρος στην οθόνη που δίνεται για το UI
        self.initialize_environment()

    # Η συνάρτηση που αρχικοποιεί το περιβάλλον της προσομοίωσης
    def initialize_environment(self):
        self.window = Tk()
        self.window.title("Epidemic Simulation")
        self.window.resizable(False, False)
        self.canvas = Canvas(
            self.window, width=self.canvas_size[0], height=self.canvas_size[1], bg='gray5')
        self.canvas.pack()

        _ui = ui.Ui(self, self.window)

        while not self.has_started:
            self.window.update_idletasks()
            self.window.update()

    # Η βασική μέθοδος για να τρέξει ολόκληρη η προσομοίωση.
    def run(self):
        if not self.running:
            self.running = True

            # Δημιούργησε τα καταστήματα και τοποθέτησέ τα στη λίστα shop_list.
            for i in range(self.shop_population):
                self.shop_list.append(Shop(self.canvas, (random.randint(0, self.canvas_size[0] - self.ui_space), random.randint(
                    0, self.canvas_size[1])), random.randint(15, 20), random.randint(15, 20)))

            # Δημιούργησε τους πράκτορες και τοποθέτησέ τους στη λίστα agent_list.
            for i in range(self.sick_population):
                ag_x = random.randint(0, self.canvas_size[0] - self.ui_space)
                ag_y = random.randint(0, self.canvas_size[1])
                new_agent = ra.ReflexAgent(self, (ag_x, ag_y), 'red', "sick")
                self.agent_list.append(new_agent)
                self.agent_grid[ag_x][ag_y].append(new_agent)

            for i in range(self.population - self.sick_population):
                ag_x = random.randint(0, self.canvas_size[0] - self.ui_space)
                ag_y = random.randint(0, self.canvas_size[1])
                new_agent = ra.ReflexAgent(self, (ag_x, ag_y), 'turquoise3', "healthy")
                self.agent_list.append(new_agent)
                self.agent_grid[ag_x][ag_y].append(new_agent)

            # Για κάθε έναν πράκτορα βρες το κατάστημα προτίμησής του και αποθήκευσέ την τοποθεσία του στο pref_shop_state.
            for agent in self.agent_list:
                agent.pref_shop_state = agent.preferred_shop(self.shop_list)

            # mainloop
            while self.running:
                # Αν η προσομοίωση δεν έχει "παγώσει"
                # Για κάθε πράκτορα βρες αν έχει φτάσει τον προοσισμό του.
                # Αν ναι, μετακίνησέ τον πίσω στο "σπίτι" του. Αν όχι, συνέχισε να για τον φτάσεις.
                # Επίσης έλεγξε αν ο πράκτορας πρέπει να μολυνθεί ή να μολύνει κάποιον άλλον
                if not self.is_paused:
                    for agent in self.agent_list:
                        if agent.state == agent.pref_shop_state:
                            agent.reached_destination = True
                        elif agent.state == agent.home_state:
                            agent.reached_destination = False

                        if agent.reached_destination:
                            agent.find_next_state(agent.home_state)
                        else:
                            agent.find_next_state(agent.pref_shop_state)

                        agent.update_conditions()

                        agent.update()
                        # time.sleep(0.001)     # Χρειάζεται για μικρό πλήθος πρακτόρων (πχ. 5).

                self.window.update_idletasks()
                self.window.update()

    def destroy(self):
        self.window.destroy()


# Εικονικό κατάστημα για την προσομοίωση της κοινότητας
class Shop:
    def __init__(self, canvas, state, width, height):
        self.canvas = canvas
        self.state = state
        self.x1 = self.state[0] - width
        self.y1 = self.state[1] - height
        self.x2 = self.state[0] + width
        self.y2 = self.state[1] + height
        self.height = height
        self.width = width

        self.rect = self.canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2, fill="peru")
