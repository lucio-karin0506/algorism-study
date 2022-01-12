T = int(input())
res_list = []

for test_case in range(1, T + 1):
    input_num = int(input())

    # 모든 색칠 영역 리스트 담는 전체 리스트
    all_num_list = []

    # 입력한 숫자 크기만큼 숫자 위치 리스트 받음
    for i in range(input_num):
        num_list = list(map(int, input().split()))
        all_num_list.append(num_list)

    for num_list in all_num_list:
        # red
        if num_list[-1] == 1:
            pass
        # blue
        elif num_list[-1] == 2:
            pass