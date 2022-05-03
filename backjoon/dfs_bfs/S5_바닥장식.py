def solution(graph, N, M):
    count = 0

    # 같은 행 나무 판자 판별
    for a in range(N):
        pos = '/'
        for b in range(M):
            if graph[a][b] == '-':
                if graph[a][b] != pos:
                    count += 1

            pos = graph[a][b]

    # 같은 열 나무 판자 판별
    for b in range(M):
        pos = '/'
        for a in range(N):
            # 카운트 세고 거쳤던 바닥문양 pos로 초기화
            if graph[a][b] == '|':
                if graph[a][b] != pos:
                    count += 1

            pos = graph[a][b]

    return count


if __name__ == '__main__':
    N, M = map(int, input().split())
    floor_info = [list(input()) for _ in range(N)]

    res = solution(graph=floor_info, N=N, M=M)
    print(res)