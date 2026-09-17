class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking lines
        for i in range(0, 9):
            lineIsHealty = {}
            for j in range(0, 9):
                number = ord(board[i][j])
                if number != 46:
                    if lineIsHealty.get(number) == None:
                        lineIsHealty[ord(board[i][j])] = 1
                    else:
                        return False
        # checking columns
        for i in range(0, 9):
            lineIsHealty = {}
            for j in range(0, 9):
                number = ord(board[j][i])
                if number != 46:
                    if lineIsHealty.get(number) == None:
                        lineIsHealty[ord(board[j][i])] = 1
                    else:
                        return False
        # checking boards
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                boardIsHealthy = {}
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        number = ord(board[k][l])
                        if number != 46:
                            if boardIsHealthy.get(number) == None:
                                boardIsHealthy[ord(board[k][l])] = 1
                            else:
                                return False
        return True
