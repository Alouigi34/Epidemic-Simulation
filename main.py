import SimulationEnvironment as se

canvas_width = 1100
canvas_height = 600
simulation = se.Simulation(
    [canvas_width, canvas_height], population=70, agent_size=3, sick_population=3)
