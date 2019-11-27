from model import miModelo
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer 

def portrayal(agent):
    portrayal = {"Shape":"circle",
                "Filled":"true",
                "Layer":0,
                "Color":"red",
                "r":0.5}
    return portrayal
    
grid = CanvasGrid(portrayal, 10, 10, 500, 500)
server = ModularServer(miModelo,
                        [grid],
                        "Nuestro segundo modelo",
                        {"N":2})