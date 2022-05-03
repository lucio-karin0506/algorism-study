from collections import deque

def solution(graph, start, visit):
    queue = deque()
    queue.append(start)
    visit[0][0] = 1

    dx, dy = [1, 0], [0, 1]

    while queue:
        x, y = queue[0][0], queue[0][1]
        del queue[0]

        # 맨 오른쪽 아래 도달 시
        if graph[x][y] == -1:
            return 'HaruHaru'

        jump = graph[x][y]

        for i in range(2):
            nx = x + dx[i] * jump
            ny = y + dy[i] * jump
            
            # 범위 안에 있고, 미방문 시 방문 체크 후 queue에 삽입
            if 0 <= nx < len(graph) and 0 <= ny < len(graph) and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                queue.append((nx, ny))

    return 'Hing'


if __name__ == '__main__':
    T = int(input())
    graph = [list(map(int, input().split())) for _ in range(T)]
    # 방문체크
    visit = [[0]*T for _ in range(T)]

    res = solution(graph=graph, start=(0, 0), visit=visit)
    print(res)