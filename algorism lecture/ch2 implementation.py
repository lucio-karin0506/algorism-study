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

# problem2
# 완전 탐색
def func2(n):
    count = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count += 1

    return count

# problem3
def func3(place_num):
    knight_place_num = 0
    row = int(place_num[1])
    col = int(ord(place_num[0])) - int(ord('a')) + 1

    steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), 
            (-1, -2), (-1, 2), (1, -2), (1, 2)]

    for step in steps:
        next_row = row + step[0]
        next_col = col + step[1]

        if next_row >= 1 and next_row <= 8 and next_col >=1 and next_col <= 8:
            knight_place_num += 1

    return knight_place_num

# problem4
def func4(input_text):
    input_list = list(input_text)

    alpha_list = []
    num_list = []
    
    for i in input_list:
        if i.isalpha() == True:
            alpha_list.append(i)
        elif i.isdigit() == True:
            num_list.append(int(i))

    result = ''.join(sorted(alpha_list)) + str(sum(num_list))

    return result

if __name__ == '__main__':
    # n = int(input('input n: '))
    # d_list = input('input d_list: ').split()
    # a = func1(n, d_list)

    n = input('input: ')
    a = func4(n)
    print(a)