# redo
def solution(graph, N, M):
    count = 0

    # check -
    for i in range(N):
        pre = '/'
        for j in range(M):
            # - 일 경우 count 증가
            if graph[i][j] == '-':
                # 같은 모양일 경우, count 제외 ==> 이전 타일 모양과 다를 때만 확인 위함
                if graph[i][j] != pre:
                    count += 1

            # 이전 타일 모양 정보 저장 => 다음 타일 모양과의 일치 여부 비교 위함
            pre = graph[i][j]

    # check |
    for j in range(M):
        pre = '/'
        for i in range(N):
            # | 일 경우 count 증가
            if graph[i][j] == '|':
                if graph[i][j] != pre:
                    count += 1

            pre = graph[i][j]

    return count


if __name__ == '__main__':
    N, M = map(int, input().split())
    floor_info = [list(input()) for _ in range(N)]

    res = solution(graph=floor_info, N=N, M=M)
    print(res)