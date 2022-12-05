""" Agent module for the Flocking simulation """
import random
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
        """ Executes one step of an agent """
        self.calculate_isolation()
        self.avoid_dispersion_movement()
        self.move()

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

    def avoid_dispersion_movement(self):
        """birds avoid dispersion and collisions"""
        bird_array = self.model.schedule.agents
        picked_bird = random.choice(bird_array)

        if picked_bird.is_isolated:
            picked_bird = self

        picked_bird_x, picked_bird_y = picked_bird.pos
        own_pos_x, own_pos_y = self.pos
        future_pos_x = picked_bird_x + config.FUTURE_POSITION_VAR * picked_bird.dir_x
        future_pos_y = picked_bird_y + config.FUTURE_POSITION_VAR * picked_bird.dir_y

        if own_pos_x == future_pos_x:
            sgn_x = 0
        elif own_pos_x > future_pos_x:
            sgn_x = -1
        else:
            sgn_x = 1

        if own_pos_y == future_pos_y:
            sgn_y = 0
        elif own_pos_y > future_pos_y:
            sgn_y = -1
        else:
            sgn_y = 1

        dx = abs(own_pos_x - future_pos_x)
        dy = abs(own_pos_y - future_pos_y)

        if dy > dx:
            new_dir_x = sgn_x * 1
        else:
            new_dir_x = sgn_x * 2
        if dy < dx:
            new_dir_y = sgn_y * 1
        else:
            new_dir_y = sgn_y * 2

        self.dir_x = int((self.dir_x + new_dir_x) / 2)
        self.dir_y = int((self.dir_y + new_dir_y) / 2)

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
                distance = abs(my_pos_x - bird_x) + abs(my_pos_y - bird_y)
                if distance < config.ISOLATION_DISTANCE:
                    arr.append(distance)
        if len(arr) == 0:
            self.is_isolated = True
        else:
            self.is_isolated = False
