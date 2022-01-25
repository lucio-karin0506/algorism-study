def maze(graph, N):
    # 출발점 좌표 탐색
    start_point = (0, 0)
    for i in range(len(graph)):
        for j in range(i):
            if graph[i][j] == 2:
                start_point = (i, j)

    # queue 생성
    from collections import deque
    queue = deque()

    # 시작점 삽입
    queue.append(start_point)

    # x, y축 이동방향 선언(중심 좌표 x, y기준 상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # queue가 빌 때까지,
    while queue:
        # 탐색하고자 하는 중심좌표 뽑아냄
        x, y = queue.popleft()

        # 이동방향 상하좌우로 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로의 크기 범위를 벗어난 경우,
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            # 미로가 벽에 막힌 경우,
            if graph[nx][ny] == 1:
                continue
            # 미로가 통로를 마주친 경우, 한 번만 탐색하게 함.
            if graph[nx][ny] == 0:
                graph[nx][ny] = 'pass'
                queue.append((nx, ny))
            # 도착점 3에 도달한 경우,
            if graph[nx][ny] == 3:
                return 1

    return 0


if __name__ == '__main__':
    T = int(input())
    res = []

    for _ in range(1, T + 1):
        N = int(input())
        graph = [list(map(int, input())) for _ in range(N)]
        ans = maze(graph, N)
        res.append(ans)

    for idx, value in enumerate(res):
        print(f'#{idx+1} {value}')