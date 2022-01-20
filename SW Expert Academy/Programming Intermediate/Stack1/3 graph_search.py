def find_graph_way(graph_info, start_target, end_target):
    ans = 0

    # 탐색 완료된 노드 리스트
    visited = []
    # 아직 탐색 안한 노드 리스트
    not_visited = []

    # 시작 노드 추가
    not_visited.append(start_target)

    # 탐색이 완료될 때까지
    while not_visited:
        # 탐색 아직 안한 리스트에서 마지막 값 뽑아냄
        node = not_visited.pop()
        # 해당 노드가 탐색 완료된 리스트에 없으면
        if node not in visited:
            # 탐색 완료된 리스트에 추가
            visited.append(node)
            # 해당 노드에 연결되어 있는 노드들을
            # 탐색 안한 노드 리스트에 추가
            not_visited.extend(graph_info[node])

    for node in visited:
        # 경로 존재 시
        if node == end_target:
            ans = 1

    return ans

if __name__ == '__main__':
    T = int(input())
    res = []

    for _ in range(1, T + 1):
        V, E = map(int, input().split())
        graph_info = {}

        for node in range(1, V+1):
            graph_info[node] = []

        # 간선 수 만큼 간선 정보 입력
        for _ in range(E):
            start_node, end_node = map(int, input().split())
            # 간선 정보에 해당 노드와 연결된 노드 있으면
            # graph_info 업데이트 ㄱㄱ
            for node, line_info in graph_info.items():
                if node == start_node:
                    line_info.append(end_node)

        start_target, end_target = map(int, input().split())

        ans = find_graph_way(graph_info, start_target, end_target)
        res.append(ans)

    for idx, value in enumerate(res):
        print(f'#{idx+1} {value}')