def target(individual):
    x = individual["x"]
    y = individual["y"]
    z = individual["z"]
    return (2* x**2 - 3* y**2 - 4* x + 5* y + z)

def apply_function(individual):
    x = individual["x"]
    y = individual["y"]
    z = individual["z"]
    return (2* x**2 - 3* y**2 - 4* x + 5* y + z)**9
