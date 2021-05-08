import SimulationEnvironment as se

canvas_width = 800
canvas_height = 600
simulation = se.Simulation(
    [canvas_width, canvas_height], population=100, agent_size=3, shop_population=2)
simulation.run()
