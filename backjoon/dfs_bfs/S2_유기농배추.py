import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline()

def search(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return

    if farm_info[x][y] == 0:
        return

    # 이미 탐색한 배추는 0으로 갱신
    farm_info[x][y] = 0

    # 동서남북 탐색
    search(x-1, y)
    search(x+1, y)
    search(x, y-1)
    search(x, y+1)


if __name__ == '__main__':
    T = int(input())
    res = []
    for _ in range(T):
        M, N, K = map(int, input().split())
        # 농장 정보 0으로 초기화
        farm_info = [[0]*N for _ in range(M)]
        
        # 지렁이 위치 정보 입력받음
        warm_location = [list(map(int, input().split())) for _ in range(K)]
        # 농장에 지렁이 위치 있는 곳에 1표시
        for warm in warm_location:
            x = warm[0]
            y = warm[1]
            farm_info[x][y] = 1

        # 배추 있는 공간 개수 count
        cnt = 0
        for a in range(M):
            for b in range(N):
                if farm_info[a][b] == 1:
                    search(a, b)
                    cnt += 1

        res.append(cnt)

    for value in res:
        print(value)