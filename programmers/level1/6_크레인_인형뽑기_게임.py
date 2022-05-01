import numpy as np

def solution(board, moves):
    answer = 0

    new_board = np.array(board).T
    
    temp = []
    for move_num in moves:
        for idx, col in enumerate(new_board):
            if move_num == idx+1:
                for num in col:
                    if num == 0:
                        pass
                    else:
                        temp.append(num)
                        break

       

    return answer

if __name__ == '__main__':
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]

    res = solution(board, moves)
    print(res)