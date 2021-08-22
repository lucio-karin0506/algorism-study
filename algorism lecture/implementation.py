# problem 1
def func1(n, d_list):
    x = 1
    y = 1
    move_types = ['L', 'R', 'U', 'D']

    # U, D 방향
    dx = [0, 0, -1, 1]
    # L, R 방향
    dy = [-1, 1, 0, 0]

    # 이동 계획 확인
    for i in d_list:
        # 이동 후 좌표 구하기
        for index in range(len(move_types)):
            if i == move_types[index]:
                nx = x + dx[index]
                ny = y + dy[index]

        # 공간 벗어날 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue

        # 이동 수행
        x, y = nx, ny

    return x, y

if __name__ == '__main__':
    n = int(input('input n: '))
    d_list = input('input d_list: ').split()
    a = func1(n, d_list)
    print(a)