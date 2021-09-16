import SimulationEnvironment as se

canvas_width = 1000
canvas_height = 600
simulation = se.Simulation(
    [canvas_width, canvas_height], population=50, agent_size=3, sick_population=1)
