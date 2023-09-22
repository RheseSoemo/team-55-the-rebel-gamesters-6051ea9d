#from levelup.controller import Direction
from levelup.position import Position
from random import randrange
import array

class GameMap:
    BoardWidth = 2
    MapTiles = [[0]*1]*1

    def __init__(self, number):
        self.BoardWidth = number
        rows, cols = (self.BoardWidth, self.BoardWidth)
        #self.MapTiles = [[0]*cols]*rows
        self.MapTiles = [[0 for j in range(cols)] for i in range(rows)]
        #print("Successfully created Map")
        

        for x in range (0, self.BoardWidth):
            for y in range (0, self.BoardWidth):
                #print(x, " ", y)
                DescriptionNumber: int = randrange(6)
                #print(DescriptionNumber)
                NewPosition: Position = Position(1)
                if (DescriptionNumber == 0):
                    NewPosition.Description = "You are standing in a grassy field"
                elif (DescriptionNumber == 1):
                    NewPosition.Description = "You are standing in a dark forest"
                elif (DescriptionNumber == 2):
                    NewPosition.Description = "You are standing in front of a river"
                elif (DescriptionNumber == 3):
                    NewPosition.Description = "You are knee deep in a lake"
                elif (DescriptionNumber == 4):
                    NewPosition.Description = "You are standing on a cold mountain"
                elif (DescriptionNumber == 5):
                    NewPosition.Description = "You are running in a corn field being chased by bees"
                #print(NewPosition.Description)
                self.MapTiles[x][y] = NewPosition

    def getDescription(self, x: int, y: int):
        a: Position = self.MapTiles[x][y]
        return a.getDescription()

    def getPosition(self, x: int, y: int):
        return self.MapTiles[x][y]

    def checkPosition(self, x: int, y: int):
        ReturnState: bool = True
        #print(self.BoardWidth)
        #print(x, "|", y)
        if self.BoardWidth-1 < x or 0 > x:
            ReturnState = False
            #print("board x out of bounds")

        if self.BoardWidth-1 < y or 0 > y:
            ReturnState = False
            #print("board y out of bounds")

        #print (ReturnState)
        return ReturnState


    #def calculatePosition(direction: Direction):
        # to implement method
       # pass

    # def IsPositionValid(Position: positionCoordinates):

    def get_total_positions(self):
        return self.NumberOfPosition