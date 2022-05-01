def solution(n, computers):
    answer = 0
    

    for i in range(n):
        for j in range(len(computers[i])):
            if i != j and computers[i][j] == 1:
                print(i, j)
                print(computers[i][j])

    return answer

if __name__ == '__main__':
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    res = solution(n, computers)
    print(res)