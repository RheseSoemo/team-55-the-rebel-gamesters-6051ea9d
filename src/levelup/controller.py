import logging
from dataclasses import dataclass
from enum import Enum
from levelup.GameMap import GameMap
from random import randrange


DEFAULT_CHARACTER_NAME = "Character"

#TODO: ADD THINGS YOU NEED FOR STATUS
@dataclass
class GameStatus:
    running: bool = False
    character_name: str = DEFAULT_CHARACTER_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (-100,-100)
    move_count: int = 0

class Direction(Enum):
    NORTH = "n"
    SOUTH = "s"
    EAST = "e"
    WEST = "w"

class CharacterNotFoundException(Exception):
    pass

class InvalidMoveException(Exception):
    pass

class GameController:


    status: GameStatus
    CurrentMap: GameMap
    PositionX: int = randrange(10)
    PositionY: int = randrange(10)
    MoveCount: int = 0

    def __init__(self):
        self.status = GameStatus()

    def start_game(self):
        self.CurrentMap = GameMap(10)
        #print(CurrentMap.MapTiles)

    # Pre-implemented to demonstrate ATDD
    # TODO: Update this if it does not match your design (hint - it doesnt)
    def create_character(self, character_name: str) -> None:
        if character_name is not None and character_name != "":
            self.status.character_name = character_name
        else:
            self.status.character_name = DEFAULT_CHARACTER_NAME

    def move(self, direction: Direction) -> None:
        CanMove: bool
        NewX: int = self.PositionX
        NewY: int = self.PositionY
        FriendlyDirection: str
        self.MoveCount += 1
        #print(direction)

        if direction == Direction.NORTH:
            NewY += 1
            FriendlyDirection = "North"
            if self.CurrentMap.checkPosition(NewX, NewY) == True:
                #print("can move north")
                CanMove = True
            else:
                CanMove = False
                #print("can't move north")
        elif direction == Direction.SOUTH:
            NewY += -1
            FriendlyDirection = "South"
            if self.CurrentMap.checkPosition(NewX, NewY) == True:
                CanMove = True
            else:
                CanMove = False
        elif direction==Direction.EAST:
            NewX += 1
            FriendlyDirection = "East"
            if self.CurrentMap.checkPosition(NewX, NewY) == True:
                CanMove = True
            else:
                CanMove= False
        elif direction==Direction.WEST:
            NewX += -1
            FriendlyDirection = "West"
            if self.CurrentMap.checkPosition(NewX, NewY)==True:
                CanMove = True
            else:
                CanMove = False
        
        if CanMove == True:
            self.PositionX = NewX
            self.PositionY = NewY
            print("You move", FriendlyDirection, "to map tile X:", self.PositionX+1, "Y:", self.PositionY+1)
            print(self.CurrentMap.getDescription(self.PositionX, self.PositionY))
        else:
            print("You cannot move", FriendlyDirection, "to map tile X:", NewX+1, "Y:", NewY+1, ", so you stay on tile X:", self.PositionX+1, "Y:", self.PositionY+1)
            print(self.CurrentMap.getPosition(self.PositionX, self.PositionY).Description)
        print("You have moved", self.MoveCount, "times")

    def set_character_position(self, xycoordinates: tuple) -> None:
        # TODO: IMPLEMENT THIS TO SET CHARACTERS CURRENT POSITION -- exists to be testable
        pass

    def set_current_move_count(self, move_count: int) -> None:
        # TODO: IMPLEMENT THIS TO SET CURRENT MOVE COUNT -- exists to be testable
        pass

    def get_total_positions(self) -> int:
        
        # TODO: IMPLEMENT THIS TO GET THE TOTAL POSITIONS FROM THE MAP - - exists to be
        # testable
        return -10

    
