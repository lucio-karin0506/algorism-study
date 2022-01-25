# 1. 특정 거리의 도시 찾기
N, M, K, X = map(int, input().split())
# index가 0부터 시작하므로 시작 노드 숫자 1을 적용하기 위하여 N+1 수행
graph = [[] for _ in range(N+1)]

# 인접 리스트 생성
for i in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (N+1)
# 출발 도시까지의 거리는 0으로 설정
distance[X] = 0

# bfs 수행
from collections import deque

queue = deque([X])
while queue:
    now = queue.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            queue.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for idx, value in enumerate(distance):
    if value == K:
        print(idx)
        check = True

# 만약 최단 거리가 K인 도시 없다면 -1 출력
if check == False:
    print(-1)