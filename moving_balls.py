from tkinter import *
import math
import time
from numpy import ones,vstack
from numpy.linalg import lstsq


def MergeSort(data): 
    #Ω(nlogn), O(nlogn)
    if len(data) >1: 
        mid = len(data)//2 # Finding the mid of the array 
        L = data[:mid] # Dividing the array elements  
        R = data[mid:] # into 2 halves 
  
        MergeSort(L) # Sorting the first half 
        MergeSort(R) # Sorting the second half 
  
        i = j = k = 0
        # Merge and sort the two halves 
        while i < len(L) and j < len(R): 
            if L[i][1] < R[j][1]: 
                data[k] = L[i] 
                i+= 1
            else: 
                data[k] = R[j] 
                j+= 1
            k+= 1
        # Checking if any element was left 
        while i < len(L): 
            data[k] = L[i] 
            i+= 1
            k+= 1
        while j < len(R): 
            data[k] = R[j] 
            j+= 1
            k+= 1
    return data


class Shop:
    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.height = height
        self.width = width

        self.rect = self.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill="peru")


class Agent:
    def __init__(self, canvas, x, y, r, delta_x, delta_y, color):
        self.radius = r

        self.x1 = x + r
        self.y1 = y + r
        self.x2 = x - r
        self.y2 = y - r

        self.delta_x = delta_x
        self.delta_y = delta_y
        self.canvas = canvas
        self.color = color
        self.circle = self.canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2, fill=self.color)

    def move_to(self, objects):

        shops = []

        # Make an 2d list with pairs of the shop and the distance
        for obj in objects:

            coords = self.canvas.coords(self.circle)
            coords[0] += self.radius
            coords[1] += self.radius

            distance = math.sqrt(((obj.x + obj.width//2) -  coords[0])**2 + ((obj.y + obj.height//2) - coords[1])**2)

            shops.append([obj, distance])
        
        # Sort distances and shops
        shops = MergeSort(shops)
        target = shops[0][0]

        # Get the circle's and target's coords
        x1, y1, x2, y2 = self.canvas.coords(self.circle)
        x3, y3, x4, y4 = self.canvas.coords(target.rect)

        x3 += target.width//2
        y3 += target.height//2

        # Find the equation of the line
        points = [(coords[0], coords[1]),(target.x + target.width//2, target.y + target.height//2)]
        x_coords, y_coords = zip(*points)
        A = vstack([x_coords,ones(len(x_coords))]).T
        a, b = lstsq(A, y_coords)[0]
        
        # Determine if the circle is left from the object and act accordingly
        isLeft = False
        if x1 < x3:
            isLeft = True

        if isLeft:
            while (coords[0] < x3 or coords[0] < y3):
                time.sleep(0.01)

                self.canvas.move(self.circle, 1, ((x1 + 1) * a + b) - y1)

                x1, y1, x2, y2 = self.canvas.coords(self.circle)
                coords = self.canvas.coords(self.circle)
                coords[0] += self.radius
                coords[1] += self.radius
                
                self.canvas.tag_raise(self.circle)

                window.update()
        else:
            while (coords[0] > x3 or coords[0] < y3):
                time.sleep(0.01)

                self.canvas.move(self.circle, -1, ((x1 + 1) * a + b) - y1)

                x1, y1, x2, y2 = self.canvas.coords(self.circle)
                coords = self.canvas.coords(self.circle)
                coords[0] += self.radius
                coords[1] += self.radius

                self.canvas.tag_raise(self.circle)

                window.update()
            

# main
window = Tk()
window.title("Moving balls")
window.resizable(False, False)

canvas = Canvas(window, width=300, height=300)
canvas.pack()

ball1 = Agent(canvas, 20, 30, 10, 5, 5, "red")
ball2 = Agent(canvas, 200, 100, 10, 4, 4, "green")

shops = [Shop(canvas, 100, 100, 50, 50), Shop(canvas, 100, 10, 50, 50)]

window.update_idletasks()
window.update() 
time.sleep(0.1)
ball1.move_to(shops)
ball2.move_to(shops)

window.mainloop()