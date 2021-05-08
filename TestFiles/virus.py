file = open("virus.txt", "r")
file = file.read().split("\n")

file[0] = file[0][6:]
file[1] = file[1][27:]
file[2] = file[2][9:]
file[3] = file[3][12:]

file[2] = file[2].split(", ")

class Virus:
    def __init__(self, name, contagion, symptoms, deathRate):
        self.name = name
        self.contagion = contagion
        self.symptoms = symptoms
        self.deathRate = deathRate
    
corona = Virus(file[0], file[1], file[2], file[3])

print(f"Hello, i am {corona.name}")
print(f"I have a contagion rate of {corona.contagion}")
print("My symptoms include ", end="")
print(*corona.symptoms, sep=", ")
print(f"And I have a death rate of {corona.deathRate}%.")