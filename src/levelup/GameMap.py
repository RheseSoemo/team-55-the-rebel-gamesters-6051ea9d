#from levelup.controller import Direction
from levelup.position import Position
import array

class GameMap:
    BoardWidth = 10
    MapTiles = [[0]*1]*1

    ArrayX = []
    ArrayY = []
    # define position []

    def __init__(self, number):
        self.NumberOfPosition = number
        rows, cols = (self.NumberOfPosition, self.NumberOfPosition)
        #self.MapTiles = [[0]*cols]*rows
        self.MapTiles = [[0 for j in range(cols)] for i in range(rows)]
        #print("Successfully created Map")
        

        for x in range (0, self.NumberOfPosition):
            for y in range (0, self.NumberOfPosition):
                #print(x, " ", y)
                NewPosition: Position = Position(1)
                self.MapTiles[x][y] = NewPosition



    # def getPosition()
    #def calculatePosition(direction: Direction):
        # to implement method
       # pass

    # def IsPositionValid(Position: positionCoordinates):

    def get_total_positions(self):
        return self.NumberOfPosition