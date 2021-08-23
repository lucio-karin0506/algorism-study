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

if __name__ == '__main__':
    # 각 노드가 연결된 정보를 표현 (2차원 리스트)
    graph = [
        # 0번째 노드는 존재하지 않으므로 빈 배열 처리
        [],
        # 1번째 인접노드 리스트
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]

    # 각 노드가 방문된 정보를 표현 (1차원 리스트)
    # false 초기화 이용하여 빈 리스트 선언
    visited = [False] * 9

    # 정의된 DFS 함수 호출
    # dfs(graph, 1, visited)

    # 정의된 BFS 함수 호출
    bfs(graph, 1, visited)