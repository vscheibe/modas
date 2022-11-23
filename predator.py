""" Agent modeling Predator """
from mesa import Agent
from enum import Enum, auto
import config

class PredatorAgent(Agent):
    class Compass(Enum):
        """ Compass enum used for directional logic """
        NORTH = auto()
        WEST = auto()
        SOUTH = auto()
        EAST = auto()
        # TODO

    def __init__(self, unique_id, model):
        """ Once max_age is reached, agent automatically dies """
        super().__init__(unique_id, model)
        self.direction = model.random.choice(list(self.Compass))
        # TODO

    def get_direction_unit_vector(self):
        """ Movement helper method
            Calculates the movement vector of an agent
        """
        # TODO Add 4 more vectors

        x_pos_add = 0
        y_pos_add = 0
        match self.direction:
            case self.Compass.NORTH:
                x_pos_add = -1
            case self.Compass.SOUTH:
                x_pos_add = 1
            case self.Compass.WEST:
                y_pos_add = -1
            case self.Compass.EAST:
                y_pos_add = 1
        return x_pos_add, y_pos_add