from collections import defaultdict

def isValidSudoku(board:list[list[str]]) -> bool:
    verticalSet = defaultdict(set)
    horizontalSet = defaultdict(set)
    boxSet = defaultdict(set)
    
    for i in range(len(board)):
        for j in range(len(board)):
            value = board[i][j]
            if value != '.':
                if(value in verticalSet[j] or
                   value in horizontalSet[i] or 
                   value in boxSet(i//3,j//3)):
                    return False
            verticalSet[j].add(value)
            horizontalSet[i].add(value)
            boxSet[(i//3,j//3)].add(value)
    
    return True