from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

class miAgente(Agent): # Comenzamos definiendo a cada agente
    def __init__(self, pos, model, gender, beauty, wealth, desired_beauty, desired_wealth):
        super().__init__(pos, model) 
        self.pos = pos
        self.gender = gender
        self.beauty = beauty
        self.wealth = wealth
        self.desired_beauty = desired_beauty
        self.desired_wealth = desired_wealth
        
        def step(self):
            
# Modelamos el movimiento
            encuentros = self.model.grid.get_neighbors(self.pos,moore=True, include_center=True,radius=0)
            encuentros = [x for x in encuentros if type(x) is miAgente and x!=self] 
            if len(encuentros)==2 and encuentros.wealth >= self.desired_wealth:  # Si encuentra pareja
                self.model.schedule.remove(self)
                self.model.grid.remove_agent(self)
                self.model.parejas += 1 # Contabilizamos una pareja en la lista para futura recolección
                for n in encuentros: 
                    self.model.schedule.remove(n)
                    self.model.grid.remove_agent(n) 
            else:                                       # Si no encuentra pareja
                self.model.grid.move_to_empty(self)

class TodosCogemos(Model):
    '''
    Love-match market Model
    '''
    def __init__(self, height=50, width=50, density=0.8, HM_pc=0.2, entry_rate=30): # Aquí establecemos el tamaño del Grid donde se desarrolla el modelo, además de los parámetros iniciales.
        self.height = height
        self.width = width
        self.density = density
        self.HM_pc = HM_pc
        self.entry_rate = entry_rate
            
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(height, width, torus=False)
            
        self.parejas = 0 
        self.datacollector = DataCollector(
        {"parejas": "parejas"},  # Cantidad de parejas 
 
        {"x": lambda a: a.pos[0], "y": lambda a: a.pos[1]})
            
# En esta sección, etiquetamos a cada agente según su tipo 
        for cell in self.grid.coord_iter():
            x = cell[1]
            y = cell[2]
            if self.random.random() < self.density:
                if self.random.random() < self.HM_pc:
                    gender = 1
                else:
                    gender = 0
                
                agent = miAgente((x, y), self, gender, beauty=0.5, wealth = 0.8, desired_beauty=0.2, desired_wealth=0.5)
                self.grid.place_agent(agent, (x, y))
                self.schedule.add(agent)

        self.running = True
        self.datacollector.collect(self)

    def step(self): # Este step permite que el modelo siga corriendo hasta que todos los agentes tengan pareja
        self.parejas = 0
        self.schedule.step()
        # Por fines gráficos, recolectamos la información sobre la cantidad de parejas
        self.datacollector.collect(self)

        if self.schedule.get_agent_count() == 0:
            self.running = False
