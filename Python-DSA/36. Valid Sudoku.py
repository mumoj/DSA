class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_boxes = collections.defaultdict(set)     
        columns = collections.defaultdict(set)

        for l in range(len(board)):
            _row = set()
            for i in range(len(board[l])):
                cl_set = set()
                if board[l][i] == ".":
                    continue

                if board[l][i] in _row:
                    return False
                elif  board[l][i] not in _row:
                    _row.add(board[l][i])

                if board[l][i] in columns[i]: 
                    return False
                elif board[l][i] not in columns[i]:
                    columns[i].add(board[l][i])

                if board[l][i] in sub_boxes[(l//3, i//3)]:
                    return False

                elif board[l][i] not in sub_boxes[(l//3, i//3)]:
                    sub_boxes[(l//3, i//3)].add(board[l][i])

        
        return True                        
