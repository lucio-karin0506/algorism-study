dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(x, y):
    global ans
    visited[x][y] = True
    if ans: return

    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 미로 크기를 벗어나지 않은 경우에,
        if 0 <= nx < N and 0 <= ny < N:
            # 중심 좌표의 상하좌우에 해당하는 좌표가 아직 방문 노드로 등록되지 않았거나
            # 1 즉 벽이 아니면
            if not visited[nx][ny] and graph[nx][ny] != 1:
                # 해당 좌표를 방문했다고 등록하고
                visited[nx][ny] = True
                # 해당 좌표가 3 즉 도착지점이면
                if graph[nx][ny] == 3:
                    # 도착했다고 알림
                    ans = 1
                dfs(nx, ny)

T = int(input())
res = []
for _ in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    # 방문 노드 리스트 선언
    visited = [[False]*N for _ in range(N)]
    ans = 0
    # 출발 좌표는 1, 1
    dfs(1, 1)
    res.append(ans)

for idx, value in enumerate(res):
    print(f'#{idx+1} {value}')