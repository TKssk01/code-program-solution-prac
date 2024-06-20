class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isValidUnit(row):
                return False
        
        for col in zip(*board):
            if not self.isValidUnit(col):
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.isValidSubBox(board, i, j):
                    return False
                
        return True
    
    def isValidUnit(self, unit: List[str]) -> bool:
        # Remove empty cells represented by ’.’
        unit = [x for x in unit if x != '.']
        
        return len(unit) == len(set(unit))
    
    def isValidSudoku(self, board: List[List[str]], start_row: int, start_col: int) -> bool:
        sub_box = []
        for i in range(3):
            for j in range(3):
                cell = board[start_row + i][start_col + j]
                if cell != '.':
                    sub_box.append(cell)
        return self.isValidUnit(sub_box)