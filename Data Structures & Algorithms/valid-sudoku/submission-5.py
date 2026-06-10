class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for num in range(9)]
        cols = [set() for num in range(9)]
        boxes = [set() for num in range(9)]

        for i_row, row in enumerate(board):
            for i_num, num in enumerate(row):
                i_box = (3*(i_row//3)+(i_num//3))

                if num == ".":
                    continue
                else:
                    if num in rows[i_row] or num in cols[i_num] or num in boxes[i_box]:
                        return False
                    #for rows
                    rows[i_row].add(num)
                    #for cols
                    cols[i_num].add(num)
                    #for boxes
                    boxes[i_box].add(num)
        return True

