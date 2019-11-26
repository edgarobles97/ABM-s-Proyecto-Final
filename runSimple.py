from model import miModelo
from mesa.visualization.modules.CanvasGridVisualization import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

def portrayal(agent):
    portrayal = {"Shape":"Circle",
                "Filled":"true",
                "Layer":1,
                "Color":"blue",
                "r":0.75}
    return portrayal
    
grid = CanvasGrid(portrayal,10,10,500,500)
server = ModularServer(miModelo,
                        [grid],
                        "Nuestro segundo modelo",
                        {"N":5})

m1 = miModelo(3)
