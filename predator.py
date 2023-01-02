""" Agent modeling Predator """
from mesa import Agent
import config


class PredatorAgent(Agent):

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.dir_x, self.dir_y = 3, 3

    def move_alternative(self):
        x_pos, y_pos = self.pos
        move_to = (x_pos + self.dir_x, y_pos + self.dir_y)
        self.model.grid.move_agent(self, move_to)

    def move(self):
        """Moves the agent once along its heading vector if a cell is free"""
        neighbors = self.model.grid.get_neighborhood(self.pos, True, False, 3)
        free_cells = []
        for neighbor in neighbors:
            x_pos, y_pos = neighbor
            if self.model.grid[x_pos, y_pos] is None:
                free_cells.append(neighbor)
        x_pos, y_pos = self.pos
        move_to = (x_pos + self.dir_x, y_pos + self.dir_y)
        if move_to in free_cells:
            self.model.grid.move_agent(self, move_to)

    def calculate_trajectory(self):
        pass

    def step(self):
        #self.move_alternative()
        self.move()
