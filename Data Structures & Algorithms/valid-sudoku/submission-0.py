class Solution:
    from collections import defaultdict

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowsDict = defaultdict(set)
        colsDict = defaultdict(set)
        boxDict = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue
                boxNum = (i//3) * 3 + (j//3)
                if board[i][j] in rowsDict[i] or board[i][j] in colsDict[j] or board[i][j] in boxDict[boxNum]:
                    return False
                else:
                    rowsDict[i].add(board[i][j])
                    colsDict[j].add(board[i][j])
                    boxDict[boxNum].add(board[i][j])
        
        return True