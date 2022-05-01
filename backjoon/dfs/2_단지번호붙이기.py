def solution(i, j):
    global cnt

    # i, j의 값이 리스트 인덱스 벗어나면 종료
    if i >= N or i < 0 or j >= N or j < 0:
        return False

    # element가 0이면 종료
    if graph[i][j] == 0:
        return False

    # element가 1이면 0으로 바꾸고 cnt+1
    graph[i][j] = 0
    cnt += 1

    # 4방향 재귀호출
    solution(i+1, j)
    solution(i, j+1)
    solution(i-1, j)
    solution(i, j-1)

    # 단지 있음 알림
    return True


if __name__ == '__main__':
    import sys
    N = int(sys.stdin.readline())
    graph = [list(map(int, sys.stdin.readline().strip('\n'))) for _ in range(N)]
    print(graph)

    # answer: 0번 인덱스는 총 단지수를 나타낼 용도
    # cnt: 집의 수 체크할 용도
    answer, cnt = [0], 0

    # 2차원 리스트 돌기
    for i in range(N):
        for j in range(N):
            # 단지가 있다면 search는 True
            search = solution(i, j)
            if search:
                answer[0] += 1
                answer.append(cnt) # 해당 단지의 집 수 저장
                cnt = 0 # cnt 초기화

    # 0번 인덱스 제외한 나머지 오름차순 정렬
    answer = answer[:1] + sorted(answer[1:])
    print(*answer, sep='\n')