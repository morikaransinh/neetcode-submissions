class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board)
        rows = {}
        columns = {}
        squares = {}

        for i in range(m):
            rows.clear()
            columns.clear()

            for j in range(m):

                # Row
                num = board[i][j]
                if num != ".":
                    if num in rows:
                        return False
                    else:
                        rows[num] = 1

                # Column
                num1 = board[j][i]
                if num1 != ".":
                    if num1 in columns:
                        return False
                    else:
                        columns[num1] = 1

                # Square
                num2 = board[i][j]
                if num2 != ".":
                    square = (i // 3, j // 3)

                    if square not in squares:
                        squares[square] = set()

                    if num2 in squares[square]:
                        return False
                    else:
                        squares[square].add(num2)

        return True