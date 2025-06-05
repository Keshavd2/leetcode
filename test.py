board = [1,2]
cc = set()
[cc.add(b) for b in board]
cc = board[:]
cc[0] = 2
board.pop()
print(board[:])
print(cc[:])
