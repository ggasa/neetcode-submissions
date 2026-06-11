class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]
        
        for i_row,row in enumerate(board):
            for i_col,col in enumerate(row):
                i_box = 3*(i_row//3)+(i_col//3)
                if col == ".":
                    continue
                
                if col in boxes[i_box] or col in rows[i_row] or col in cols[i_col]:
                    return False
                else:
                    # rows
                    rows[i_row].add(col)
                    # cols
                    cols[i_col].add(col)
                    # boxes
                    boxes[i_box].add(col)


        return True

