""" Agent module for the Flocking simulation """
from copy import copy
from enum import Enum, auto
import math

from mesa import Agent

import predator
import config


def init_position(model):
    dir_x = model.random.randint(-config.MAX_VELOCITY_BIRD, config.MAX_VELOCITY_BIRD)
    dir_y = model.random.randint(-config.MAX_VELOCITY_BIRD, config.MAX_VELOCITY_BIRD)
    return dir_x, dir_y


class BirdAgent(Agent):
    """ Class modeling agent with flocking capabilities """

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.dir_x, self.dir_y = init_position(model)
        self.direction = (self.dir_x, self.dir_y)
        while self.direction == (0, 0):
            print("reinitializing direction")
            self.dir_x, self.dir_y = init_position(model)
            self.direction = (self.dir_x, self.dir_y)
        self.is_isolated = False


    def get_direction(self):
        return self.direction

    def step(self):
        self.move()
        self.calculate_isolation()
        """ Executes one step of an agent """
        # TODO

    def move(self):
        """Moves the agent once along its heading vector if a cell is free"""
        neighbors = self.model.grid.get_neighborhood(self.pos, True, False, 2)
        free_cells = []
        for neighbor in neighbors:
            x_pos, y_pos = neighbor
            if self.model.grid[x_pos, y_pos] is None:
                free_cells.append(neighbor)
        x_pos, y_pos = self.pos
        move_to = (x_pos + self.dir_x, y_pos + self.dir_y)
        if move_to in free_cells:
            self.model.grid.move_agent(self, move_to)

    def alig_coh_movement(self):
        """birds align"""

    def avoid_dispersion_movement(self):
        """birds avoid dispersion and collision*"""
    def fleeing_from_predator(self):
        """Final movement type"""

    def get_id(self):
        """ Get unique ID of the agent """
        return self.unique_id

    def calculate_isolation(self):
        arr = []
        for bird in self.model.schedule.agents:
            if bird != self:
                my_pos_x, my_pos_y = self.pos
                bird_x, bird_y = bird.pos
                distance = abs(my_pos_x-bird_x)+abs(my_pos_y-bird_y)
                if distance < config.ISOLATION_DISTANCE:
                    arr.append(distance)
        if len(arr) == 0:
            self.is_isolated = True
        else:
            self.is_isolated = False
