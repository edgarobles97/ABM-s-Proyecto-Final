from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
   
class miAgente(Agent):
    def __init__(self, unique_id, model, value):
        super().__init__(unique_id, model)
        self.value = value

    def step(self):
        neighborhood = self.model.grid.get_neighborhood(self.pos,moore=True,include_center=False)
        target = self.model.random.choice(neighborhood)
        self.model.grid.move_agent(self,target)
        print("Ahora estoy en ",self.pos)

class miModelo(Model):
    def __init__(self, N): 
#Definimos el schedule para hacer la ejecución en orden aleatorio
        self.schedule = RandomActivation(self)
        self.current_id = 1
        self.running = True

#Definimos el grid de tamaño
        self.grid = MultiGrid(10, 10, False)
        
        self.num_agents = N
        for i in range(N):
            a = miAgente(self.next_id(), self, 5)
            self.schedule.add(a)
            
            pos_x = self.random.randint(1,9)
            pos_y = self.random.randint(1,9)
            self.grid.place_agent(a, [pos_x, pos_y])

    def step(self):
        self.schedule.step()
    