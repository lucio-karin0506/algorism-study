def solution(connect_info, visited, start):
    global cnt

    # 시작 노드에 방문 표시
    visited[start] = True

    for computer_num in connect_info[start]:
        if not visited[computer_num]:
            cnt += 1
            solution(connect_info, visited, computer_num)

    return cnt

if __name__ == '__main__':
    import sys
    computer_num = int(sys.stdin.readline())
    connect_num = int(sys.stdin.readline())

    connect_info = [list(map(int, sys.stdin.readline().split())) for _ in range(connect_num)]

    # 노드 및 간선 정보에 따른 그래프 구조에 맞게 자료구조 변형
    network_info = {node : [] for node in range(computer_num+1)}
    for info in connect_info:
        node = info[0] # 가리키는 노드
        target = info[1] # 가리킴 받는 노드
        network_info[node].append(target) # 정보 하나씩 삽입
        network_info[target].append(node) # 정보 하나씩 삽입

    visited = [False] * (computer_num+1)
    start = 1

    # 1번 컴퓨터와 연결된 컴퓨터 노드의 수
    cnt = 0

    res = solution(network_info, visited, start)
    print(res)