class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {}
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # loop for checking the sudoku rulesets
        for i_row,row in enumerate(board): #i_row = 0,1,2,...9
            for i,num in enumerate(row):
                box_key = (i_row//3, i//3)
                box_index = (i_row//3)*3+(i//3)

                if num ==".":
                    continue

                if num in rows[i_row] or num in cols[i] or num in boxes[box_index]:
                    return False
                else:
                    rows[i_row].add(num)
                    cols[i].add(num)
                    boxes[box_index].add(num)
            print(rows)
            print(f"Cols: {cols}")
            print(f"boxes: {boxes}")

        return True
        ###

        # cols
        return output