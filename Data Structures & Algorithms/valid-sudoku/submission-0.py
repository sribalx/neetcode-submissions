from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        x_hash = defaultdict(set)
        y_hash = defaultdict(set)
        z_hash = defaultdict(set)

        for x in range(0, 9):
            for y in range(0, 9):
                if board[x][y] != ".":
                    digit = int(board[x][y])
                    if digit in x_hash[x]:
                        return False
                    else:
                        x_hash[x].add(digit)

                    if digit in y_hash[y]:
                        return False
                    else:
                        y_hash[y].add(digit)
                    
                    if digit in z_hash[str(int(x/3)) + str(int(y/3))]:
                        return False
                    else:
                        z_hash[str(int(x/3)) + str(int(y/3))].add(digit)
                        print(z_hash)
        
        print 
        return True
                        
                    
                    

