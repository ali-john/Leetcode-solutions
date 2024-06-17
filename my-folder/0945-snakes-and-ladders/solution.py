class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        def intToPos(square):
            r = (square-1)//n
            c = (square-1) %n
            if r%2: # odd
                c = n-1-c
            return [r,c]
        moves_collected = []
        def bfs():
            visited = set()
            q = []
            q.append([1,0])

            while q:
                square,moves = q.pop(0)
                for i in range(1,7):
                    nextMove = square+i
                    if nextMove<=n*n:
                        if nextMove == n*n:
                            moves_collected.append(moves+1)
                        r,c = intToPos(nextMove)
                        if board[r][c]==n*n:
                            moves_collected.append(moves+1)
                        if board[r][c]!=-1:
                            nextMove = board[r][c]
                        if nextMove not in visited:
                            q.append([nextMove,moves+1])
                            visited.add(nextMove)
            if len(moves_collected):
                print(moves_collected)
                return min(moves_collected)
            return -1
           
        return bfs()


        
        
