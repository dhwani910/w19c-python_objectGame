class GameBoard:
    def __init__(self):
        self.winningRow = 0
        self.winningColumn = 2
        self.board = [
            [" * ", " * ", "   ", " * ", " * ", " * "],
            [
                " * ",
                " o ",
                "   ",
                "   ",
                " * ",
                " * ",
            ],
            [
                " * ",
                "   ",
                " * ",
                " * ",
                "   ",
                " * ",
            ],
            [
                " * ",
                " o ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            [
                " * ",
                " * ",
                "   ",
                "   ",
                "   ",
                " * ",
            ],
            [
                " * ",
                " * ",
                "   ",
                " * ",
                " * ",
                " * ",
            ],
             [
                " * ",
                "   ",
                " o ",
                "   ",
                "   ",
                " * ",
            ],
            [" * ", " * ", " * ", " * ", " * ", " * "],
        ]

    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print(" P ", end="")
                else:
                    print(self.board[i][j], end="")
            print("")

    # def printCoins(self, coins):
    #     print("coins: " + str(coins))        

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True

    # def checkCoins(self, playerRow, playerColumn):
    #     if self.board[playerRow][playerColumn].find("o") != -1:
    #         self.board[playerRow][playerColumn] = " "
    #         return True
    #     return False

    # def checkTraps(self, playerRow, playerColumn):
    #     if self.board[playerRow][playerColumn].find("DIE") != -1:
    #         return True 
    #     return False               

    # TODO
    # Return True if the player is in the winning column and row
    # Return False otherwise
    def checkWin(self, playerRow, playerColumn):
        if playerRow == 0 and playerColumn == 2:
            return True
        else:
            return False    
