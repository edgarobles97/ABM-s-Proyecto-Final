import random
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector


class miAgente(Agent): # Comenzamos definiendo a cada agente
    def __init__(self, pos, model, gender, beauty, wealth, desired_beauty, desired_wealth, time_to_critical, sojourn, is_critical):
        super().__init__(pos, model) 
        self.pos = pos
        self.gender = gender
        self.beauty = beauty
        self.wealth = wealth
        self.desired_beauty = desired_beauty
        self.desired_wealth = desired_wealth 
        
        self.time_to_critical = time_to_critical
        self.sojourn = -1
        self.is_critical = 0
        
    def step(self): # Modelamos el movimiento
        vecindad = self.model.grid.get_neighborhood(self.pos,moore=True,include_center=False)
        destino = random.choice(vecindad)
        self.model.grid.move_agent(self, destino)

        prospectos = self.model.grid.get_neighbors(self.pos,moore=True, include_center=True,radius=0)
        matches = [x for x in prospectos if type(x) is miAgente and x!=self and x.beauty>=self.desired_beauty and x.gender != self.gender and x.wealth >= self.desired_wealth]

        if len(matches)==1:  # Si encuentra pareja, desaparecen del grid
            self.model.schedule.remove(self)
            self.model.grid.remove_agent(self)
            if self.gender == 1:
                self.model.hombres -= 1
            else:
                self.model.mujeres -= 1
            self.model.parejas += 1 # Contabilizamos una pareja en la lista para futura recolección
            for m in matches: 
                self.model.schedule.remove(m)
                self.model.grid.remove_agent(m) 
                if m.gender == 1:
                    self.model.hombres -= 1
                else:
                    self.model.mujeres -= 1
        
        self.sojourn += 1
        if self.sojourn >= self.time_to_critical:
            self.is_critical = 1
            
        if self.is_critical == 1:
            self.model.schedule.remove(self)
            self.model.grid.remove_agent(self)
            self.model.unhappy += 1
            if self.gender == 1:
                    self.model.hombres -= 1
            else:
                    self.model.mujeres -= 1
                  
class TodosC(Model):
    '''
    Love-match market Model: 
    
    En este modelo, cada individuo recorre de manera aleatoria el lugar, al encontrarse con un match (agente del sexo opuesto con parámetros de belleza y riqueza coincidentes con lo deseado) desaparece del modelo. 
    El objetivo es observar la distribución de perfiles de belleza y riqueza a lo largo del tiempo hasta ver quienes no logran encontrar pareja. 
    '''
    def __init__(self, height=50, width=50, density=0.8, HM_pc=0.2, entry_rate=1, max_agents=750): # Aquí establecemos el tamaño del Grid donde se desarrolla el modelo, además de los parámetros iniciales.
        self.height = height
        self.width = width
        self.density = density
        self.HM_pc = HM_pc
        
        self.entry_rate = 5
            
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(height, width, torus=False)
        self.max_agents = max_agents
        self.parejas = 0
        self.hombres = 0
        self.mujeres = 0
        self.unhappy = 0
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
                    self.hombres += 1
                else:
                    gender = 0
                    self.mujeres += 1
                agent = miAgente((x, y), self, gender, beauty = random.gauss(3,5),
                                                         wealth = random.gauss(2,6),
                                                         desired_beauty = random.gauss(2,5), 
                                                         desired_wealth = random.gauss(3,3),
                                                         time_to_critical = random.gauss(20, 5), 
                                                         sojourn = -1,
                                                         is_critical= 0)   
            self.schedule.add(agent)
            self.grid.place_agent(agent, (x,y))
                

        
        
        self.running = True
        self.datacollector.collect(self)

        

    def step(self): # Este step permite que el modelo siga corriendo hasta que todos los agentes tengan pareja
        self.schedule.step()
        if self.schedule.get_agent_count()<750:
            for i in range(self.entry_rate):
                x = self.random.randrange(self.grid.width)
                y = self.random.randrange(self.grid.height)
                if self.random.random() < self.HM_pc:
                    gender = 1 
                    self.hombres += 1
                else:
                    gender = 0
                    self.mujeres += 1

                agent = miAgente(i, self,gender, 
                                 beauty = random.gauss(4,2),
                                 wealth = random.gauss(4,3), 
                                 desired_beauty = random.gauss(4,3),
                                 desired_wealth = random.gauss(3,2),
                                 time_to_critical = random.gauss(20,5),
                                 sojourn = -1,
                                 is_critical = 0)
            self.schedule.add(agent)
            self.grid.place_agent(agent, (x,y))
        # Por fines gráficos, recolectamos la información sobre la cantidad de parejas
        self.datacollector.collect(self)

        if self.schedule.get_agent_count() == 0: 
            self.running = False

        
