'''
1. DFS 깊이 우선 탐색
   - 깊은 부분을 우선적 탐색
   - 스택 자료구조 또는 재귀 함수 사용
'''

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

'''
2. BFS 너비 우선 탐색
   - 가까운 노드부터 우선적 탐색
   - 큐 자료구조 사용
'''
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    
    # 현재 노드 방문 처리
    visited[start] = True

    # 큐 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접 원소 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# problem 1 - dfs
def make_ice_dfs(x, y, row, col, graph):
    if x <= -1 or x >= row or y <= -1 or y >= col:
        return False
    # 현재 노드 미방문 시
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        make_ice_dfs(x - 1, y, row, col, graph)
        make_ice_dfs(x, y - 1, row, col, graph)
        make_ice_dfs(x + 1, y, row, col, graph)
        make_ice_dfs(x, y + 1, row, col, graph)
        return True
    return False

# problem 2 - bfs
def out_of_miro(x, y, row, col, dx, dy, graph):
    # 큐 구현 위한 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때 까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    return graph[row - 1][col - 1]            

if __name__ == '__main__':
    # 각 노드가 연결된 정보를 표현 (2차원 리스트)
    # graph = [
    #     # 0번째 노드는 존재하지 않으므로 빈 배열 처리
    #     [],
    #     # 1번째 인접노드 리스트
    #     [2, 3, 8],
    #     [1, 7],
    #     [1, 4, 5],
    #     [3, 5],
    #     [3, 4],
    #     [7],
    #     [2, 6, 8],
    #     [1, 7]
    # ]

    # 각 노드가 방문된 정보를 표현 (1차원 리스트)
    # false 초기화 이용하여 빈 리스트 선언
    # visited = [False] * 9

    # 정의된 DFS 함수 호출
    # dfs(graph, 1, visited)

    # 정의된 BFS 함수 호출
    # bfs(graph, 1, visited)

    # problem 1 input data
    # 행, 열 정보 입력 받기
    row, col = map(int, input().split())

    # 2차원 리스트의 맵 정보 입력 받기
    graph = []
    for _ in range(row):
        graph.append(list(map(int, input())))
    
    # 모든 노드에 대하여 음료수 채우기
    result = 0
    for i in range(row):
        for j in range(col):
            # 현재 위치에서 dfs 수행
            if make_ice_dfs(i, j, row, col, graph) == True:
                result += 1
    
    # print(result)

    # problem 2 result
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    print(out_of_miro(0, 0, row, col, dx, dy, graph))