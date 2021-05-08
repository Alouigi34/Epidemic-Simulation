from tkinter import *
import random
import ReflexAgent as ra
import time


# Βασικό περιβάλλον προσομοίωσης κοινότητας
class Simulation:
    def __init__(self, canvas_size, population, agent_size, shop_population):
        self.canvas_size = canvas_size
        self.population = population
        self.agent_size = agent_size
        self.shop_population = shop_population
        self.agent_list = []
        self.shop_list = []
        self.running = False    # Όσο έχει την τιμή True η προσομοίωση τρέχει

    # Η βασική μέθοδος για να τρέξει ολόκληρη η προσομοίωση.
    def run(self):
        self.running = True
        window = Tk()
        window.title("Epidemic Simulation")
        window.resizable(False, False)
        canvas = Canvas(
            window, width=self.canvas_size[0], height=self.canvas_size[1], bg='gray5')
        canvas.pack()

        # Δημιούργησε τα καταστήματα και τοποθέτησέ τα στη λίστα shop_list.
        for i in range(self.shop_population):
            self.shop_list.append(Shop(canvas, (random.randint(0, self.canvas_size[0]), random.randint(
                0, self.canvas_size[1])), random.randint(15, 20), random.randint(15, 20)))

        # Δημιούργησε τους πράκτορες και τοποθέτησέ τους στη λίστα agent_list.
        for i in range(self.population):
            self.agent_list.append(ra.ReflexAgent(canvas, (random.randint(
                0, self.canvas_size[0]), random.randint(0, self.canvas_size[1])), self.agent_size, 'turquoise3'))

        # Για κάθε έναν πράκτορα βρες το κατάστημα προτίμησής του και αποθήκευσέ την τοποθεσία του στο pref_shop_state.
        for agent in self.agent_list:
            agent.pref_shop_state = agent.preferred_shop(self.shop_list)

        # mainloop
        while self.running:
            # Για κάθε πράκτορα βρες αν έχει φτάσει τον προοσισμό του. 
            # Αν ναι, μετακίνησέ τον πίσω στο "σπίτι" του. Αν όχι, συνέχισε να για τον φτάσεις.
            for agent in self.agent_list:
                if agent.state == agent.pref_shop_state:
                    agent.reached_destination = True
                elif agent.state == agent.home_state:
                    agent.reached_destination = False
                
                if agent.reached_destination:
                    agent.find_next_state(agent.home_state)
                else:
                    agent.find_next_state(agent.pref_shop_state)
                    
                agent.update()
                # time.sleep(0.001) #Χρειάζεται για μικρό πλήθος πρακτόρων (πχ. 5).

            window.update_idletasks()
            window.update()


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
