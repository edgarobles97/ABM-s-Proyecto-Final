from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule, TextElement
from mesa.visualization.UserParam import UserSettableParameter
from TodosC import TodosC

class CoupleElement(TextElement): # Comenzamos con la parte visual del modelo

    def __init__(self):
        pass

    def render(self, model):
        return "matches -- left: " + str(model.parejas) + ' -- ' +str(model.unhappy) # Debajo del grid observamos la cuenta total de agentes felices

def todoscogemos_draw(agent): # En esta sección, establecemos cómo se representará a cada agente en el grid
    if agent is None:
        return
    portrayal = {"Shape": "rect", "w" : 0.8, "h" : 0.8, "Filled": "true", "Layer": 1}
    
    if agent.gender == 0:
        portrayal["Color"] = ["#FF0000", "#FF9999"]
        portrayal["stroke_color"] = "#00FF00"
    else:
        portrayal["Color"] = ["#0000FF", "#9999FF"]
        portrayal["stroke_color"] = "#000000"
    return portrayal

couple_element = CoupleElement()
canvas_element = CanvasGrid(todoscogemos_draw, 25, 30, 500, 500)

couples_chart = ChartModule([{"Label": "parejas", "Color": "Black"}])
unhappy_chart = ChartModule([{"Label": "unhappy", "Color":"Red"}], data_collector_name='datacollector')

model_params = {
    "height": 25,
    "width": 30,
    "density": UserSettableParameter("slider", "Densidad poblacional", 0.5, 0.1, 1.0, 0.1),
    "HM_pc": UserSettableParameter("slider", "Fracción de hombres vs mujeres", 0.5, 0.00, 1.0, 0.1),
    }

server = ModularServer(TodosC,
                       [canvas_element, couple_element, couples_chart, unhappy_chart],
                       "Proyecto Final", model_params)
