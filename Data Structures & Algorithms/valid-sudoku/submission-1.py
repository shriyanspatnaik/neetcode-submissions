class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                if num in row[i]:
                    return False
                row[i].add(num)

                if num in column[j]:
                    return False
                column[j].add(num)

                idx = (i//3) * 3 + j//3
                if num in box[idx]:
                    return False
                box[idx].add(num)



        return True