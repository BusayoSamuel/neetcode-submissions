class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for i in range(len(board[0]))]
        rows = [set() for i in range(len(board))]
        grid = [ [set() for i in range(3)] for j in range(3)]

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in cols[c]:
                        print("Here1")
                        return False
                    else:
                        cols[c].add(board[r][c])
                    
                    if board[r][c] in rows[r]:
                        print("Here2")
                        return False
                    else:
                        rows[r].add(board[r][c])

                    if board[r][c] in grid[r // 3][c // 3]:
                        print(grid)
                        print("Here3", board[r][c])
                        return False
                    else:
                        grid[r // 3][c // 3].add(board[r][c])

        return True
        