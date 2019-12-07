from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter
from LoveMatch import LoveMatch

class CoupleElement(TextElement): # Comenzamos con la parte visual del modelo

    def __init__(self):
        pass

    def render(self, model):
        return "parejas: " + str(model.parejas) # Debajo del grid observamos la cuenta total de agentes felices

def LoveMatch_draw(agent): # En esta sección, establecemos cómo se representará a cada agente en el grid

    if agent.gender == 0: # Asignamos un color a hombres y otro a mujeres
        portrayal = {"Shape": "circle",
         "Color": "blue",
         "Filled": "true",
        "Layer": 0,
        "r": 0.5}
    if agent.gender == 1:
       portrayal = {"Shape": "circle",
                 "Color": "red",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5}
    if agent is None:
        portrayal = {"Shape": "rect", "w": 1, "h":1, "Filled": "false", "Layer": 0}
    return portrayal

couple_element = CoupleElement()
canvas_element = CanvasGrid(LoveMatch_draw, 50, 50, 500, 500)
couples_chart = ChartModule([{"Label": "parejas", "Color": "Black"}])
unhappy_chart = ChartModule([{"Label": "unhappy", "Color":"Red"}])


model_params = {
    "height": 50,
    "width": 50,
    "density": UserSettableParameter("slider", "Densidad poblacional", 0.5, 0.1, 1.0, 0.1),
    "HM_pc": UserSettableParameter("slider", "Fracción de hombres vs mujeres", 0.5, 0.00, 1.0, 0.1),
    "entry_rate": UserSettableParameter("slider", "Ticks de entrada de nuevo grupo", 4, 0, 50, 1),
}

server = ModularServer(LoveMatch,
                       [canvas_element, couple_element, couples_chart, unhappy_chart],
                       "Proyecto Final", model_params)
