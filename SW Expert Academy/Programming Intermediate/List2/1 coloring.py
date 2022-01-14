T = int(input())
res_list = []

for test_case in range(1, T + 1):
    input_num = int(input())

    # 10 * 10 도화지
    canvas = [[0 for _ in range(10)] for _ in range(10)]

    # 입력한 숫자 크기만큼 숫자 위치 리스트 받음
    for _ in range(input_num):
        start_x, start_y, end_x, end_y, color = map(int, input().split())

        # 색칠 ㄱㄱ
        for i in range(start_x, end_x+1):
            for j in range(start_y, end_y+1):
                canvas[i][j] += 1

        # 겹치는 부분 탐색
        count = 0
        for row in range(len(canvas)):
            # 행 리스트
            canvas_row = canvas[row]
            for col in range(len(canvas_row)):
                if canvas[row][col] == 2:
                    count += 1

    res_list.append(count)

for index, value in enumerate(res_list):
    print(f'#{index+1} {value}')