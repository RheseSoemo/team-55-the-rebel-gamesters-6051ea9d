from levelup.controller import Direction
from levelup.position import Position
import array

class GameMap:
    BoardWidth = 10
    ArrayX = []
    ArrayY = []
    # define position []

    def __init__(self, number):
        self.NumberOfPosition = number
        for x in range(0, number):
            position: Position = Position(1)
            self.ArrayX.append(position)
        for y in range(0,number):
            position: Position = Position(1)
            self.ArrayY.append(position)



    # def getPosition()
    def calculatePosition(direction: Direction):
        # to implement method
        pass

    # def IsPositionValid(Position: positionCoordinates):

    def get_total_positions(self):
        return self.NumberOfPosition