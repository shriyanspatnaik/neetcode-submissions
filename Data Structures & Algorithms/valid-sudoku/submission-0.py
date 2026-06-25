class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):

            row = [0] * 9
            column = [0] * 9

            for j in range(9):

                row_num = board[i][j]
                column_num = board[j][i]

                if row_num.isdigit():
                    row_idx = ord(row_num) - 49
                    row[row_idx] += 1
                    if row[row_idx] > 1:
                        return False
                if column_num.isdigit():
                    column_idx = ord(column_num) - 49
                    column[column_idx] += 1
                    if column[column_idx] > 1:
                        return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):

                freq = [0] * 9

                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        num = board[k][l]

                        if num.isdigit():
                            idx = ord(num) - 49
                            freq[idx] += 1
                            if freq[idx] > 1:
                                return False
        return True