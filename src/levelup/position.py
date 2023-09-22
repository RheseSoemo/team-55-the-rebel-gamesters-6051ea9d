class Position:
    Description: str = ""
    

    def __init__(self, incomeDesc):
        #print(incomeDesc)
        self.Description = incomeDesc
        #print(self.Description)

    def getDescription(self):
        return self.Description
