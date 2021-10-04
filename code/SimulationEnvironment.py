from tkinter import *
import random
from typing import Counter
import ReflexAgent as ra
import ui
import time
import Virus as vi

# Βασικό περιβάλλον προσομοίωσης κοινότητας


class Simulation:
    def __init__(self, canvas_size, population, agent_size, sick_population, ui_space=200,):
        self.canvas_size = canvas_size
        self.population = population
        self.agent_size = agent_size
        self.sick_population = sick_population
        self.recovered_population = 0
        self.deceased_population = 0
        self.healthy_population = self.population - self.sick_population
        self.agent_list = []
        self.shop_list = []
        self.agent_grid = [
            [[] for i in range(canvas_size[1]+1)] for j in range(canvas_size[0]-ui_space+1)]
        self.is_paused = False  # Ελέγχει αν έχει "παγώσει" η προσομοίωση
        self.has_started = False    # Ελέγχει αν έχει ξεκινήσει η προσομοίωση
        self.running = False    # Όσο έχει την τιμή True η προσομοίωση τρέχει
        self.masks = False
        self.distance = False
        self.lockdown = False
        # Transmission Probability
        c = vi.Virus("virus_info.txt")
        self.general_transmission = c.general_transmission
        self.masks_helper_var = self.general_transmission * 1000
        self.mask_transmission = c.mask_transmission
        self.distance_transmission = c.distance_transmission
        self.recovery_rate = c.recovery_rate
        self.mortality_rate = c.mortality_rate / c.recovery_rate
        self.ui_space = ui_space    # Ο χώρος στην οθόνη που δίνεται για το UI
        self.initialize_environment()
    # Η συνάρτηση που αρχικοποιεί το περιβάλλον της προσομοίωσης

    def initialize_environment(self):
        self.window = Tk()
        self.window.title("Epidemic Simulation")
        self.window.resizable(False, False)
        try:
            self.window.iconbitmap('images/citylab_icon.ico')
        except:
            print("Could not find icon...")
        self.canvas = Canvas(
            self.window, width=self.canvas_size[0], height=self.canvas_size[1], bg='gray5')
        self.canvas.pack()
        self._ui = ui.Ui(self, self.window)
        while not self.has_started:
            self.window.update_idletasks()
            self.window.update()
    # Η βασική μέθοδος για να τρέξει ολόκληρη η προσομοίωση.

    def run(self):
        if not self.running:
            self.running = True
            # Δημιούργησε τα καταστήματα και τοποθέτησέ τα στη λίστα shop_list.
            self.shop_list.append(
                Shop(self.canvas, (20, self.canvas_size[1]//2), random.randint(15, 20), random.randint(15, 20)))
            self.shop_list.append(
                Shop(self.canvas, (self.canvas_size[0]-self.ui_space-20, self.canvas_size[1]//2), random.randint(15, 20), random.randint(15, 20)))
            self.shop_list.append(
                Shop(self.canvas, ((self.canvas_size[0]-self.ui_space)//2, 20), random.randint(15, 20), random.randint(15, 20)))
            self.shop_list.append(
                Shop(self.canvas, ((self.canvas_size[0]-self.ui_space)//2, self.canvas_size[1]-20), random.randint(15, 20), random.randint(15, 20)))
            # Δημιουργία κέντρου κοινότητας.
            self.center = Center(
                self.canvas, self.canvas_size, self.ui_space, 40, 40)
            # Δημιούργησε τους πράκτορες και τοποθέτησέ τους στη λίστα agent_list.
            for i in range(self.sick_population):
                ag_x = random.randint(0, self.canvas_size[0] - self.ui_space)
                ag_y = random.randint(0, self.canvas_size[1])
                m_d_s_x = 75
                m_d_s_y = 50
                for shop in self.shop_list:
                    while ag_x >= (shop.x1 - m_d_s_x) and ag_x <= (shop.x2 + m_d_s_x) and ag_y >= (shop.y1 - m_d_s_y) and ag_y <= (shop.y2 + m_d_s_y):
                        ag_x = random.randint(
                            0, self.canvas_size[0] - self.ui_space)
                        ag_y = random.randint(0, self.canvas_size[1])
                new_agent = ra.ReflexAgent(
                    self, (ag_x, ag_y), 'firebrick1', "sick")
                new_agent.sick_days += 1
                self.agent_list.append(new_agent)
                self.agent_grid[ag_x][ag_y].append(new_agent)
            for i in range(self.population - self.sick_population):
                ag_x = random.randint(0, self.canvas_size[0] - self.ui_space)
                ag_y = random.randint(0, self.canvas_size[1])
                m_d_s_x = 75
                m_d_s_y = 50
                for shop in self.shop_list:
                    while ag_x >= (shop.x1 - m_d_s_x) and ag_x <= (shop.x2 + m_d_s_x) and ag_y >= (shop.y1 - m_d_s_y) and ag_y <= (shop.y2 + m_d_s_y):
                        ag_x = random.randint(
                            0, self.canvas_size[0] - self.ui_space)
                        ag_y = random.randint(0, self.canvas_size[1])
                while ag_x >= (self.center.x1 - m_d_s_x) and ag_x <= (self.center.x2 + m_d_s_x) and ag_y >= (self.center.y1 - m_d_s_y) and ag_y <= (self.center.y2 + m_d_s_y):
                    ag_x = random.randint(
                        0, self.canvas_size[0] - self.ui_space)
                    ag_y = random.randint(0, self.canvas_size[1])
                new_agent = ra.ReflexAgent(
                    self, (ag_x, ag_y), 'turquoise3', "healthy")
                self.agent_list.append(new_agent)
                self.agent_grid[ag_x][ag_y].append(new_agent)
            # Για κάθε έναν πράκτορα βρες το κατάστημα προτίμησής του και αποθήκευσέ την τοποθεσία του στο pref_shop_state.
            for agent in self.agent_list:
                agent.pref_shop_state = agent.preferred_shop(self.shop_list)
            # Μετρητές των loop και των ημερών
            self.counter = 0
            self.day = 1
            # mainloop
            while self.running:
                # Αν η προσομοίωση δεν έχει "παγώσει"
                if not self.is_paused:
                    # Για κάθε πράκτορα
                    for agent in self.agent_list:
                        if agent.condition != "deceased":
                            # Αν έχει φτάσει στο κατάστημα ή στο κέντρο, έχει φτάσει στον προορισμό του
                            if agent.state == agent.pref_shop_state or agent.state == self.center.state:
                                agent.reached_destination = True
                            elif agent.state == agent.home_state:
                                agent.reached_destination = False
                            # Αν επικρατεί lockdown, δες αν έχει έρθει η στιγμή να βγει ο πράκτορας έξω
                            if self.lockdown:
                                if (self.day % agent.shop_in_lockdown) == 0:
                                    agent.in_lockdown = False
                                else:
                                    agent.in_lockdown = True
                            # Αν ο πράκτορας έχει φτάσει τον προορισμό του ή επικρατεί lockdown, να επιστρέψει στο σπίτι του
                            if agent.reached_destination or agent.in_lockdown:
                                agent.find_next_state(agent.home_state)
                            else:
                                # Αλλιώς, μετακίνησε τον πράκτορα στο κατάστημα ή στο κέντρο
                                if (self.day % agent.center_days) == 0:
                                    agent.find_next_state(self.center.state)
                                else:
                                    agent.find_next_state(
                                        agent.pref_shop_state)
                            # Δες αν ο πράκτορας πρέπει να μολυνθεί ή να μολύνει κάποιον άλλον και ενημέρωσε το UI
                            agent.update_conditions()
                            # Ενημέρωσε τη θέση του πράκτορα
                            agent.update()
                    # Αν χρειαστεί, άλλαξε τη μέρα και έλεγξε αν πρέπει να πεθάνει κάποιος ή να αναρρώσει
                    self.counter += 1
                    if self.counter >= (self.canvas_size[0] - self.ui_space) // 2:
                        self.day += 1
                        self.counter = 0
                        for agent in self.agent_list:
                            if agent.sick_days > 0 and agent.sick_days <= self.recovery_rate:
                                agent.sick_days += 1
                            agent.check_death()
                if self.population < 30:
                    # Χρειάζεται για μικρό πλήθος πρακτόρων (πχ. 5).
                    time.sleep(0.001/self.population)
                self.window.update_idletasks()
                self.window.update()
                self._ui.update_counters()

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

# Το κέντρο της κοινότητας απ' όπου περνάει κάθε πράκτορας κάποια στιγμή


class Center:
    def __init__(self, canvas, canvas_size, ui_space, width, height):
        self.canvas = canvas
        self.canvas_size = canvas_size
        self.width = width
        self.height = height
        self.state = (
            (self.canvas_size[0]-ui_space)//2, self.canvas_size[1]//2)
        self.x1 = self.state[0] - width
        self.y1 = self.state[1] - height
        self.x2 = self.state[0] + width
        self.y2 = self.state[1] + height
        self.rect = self.canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2, fill="green4")
