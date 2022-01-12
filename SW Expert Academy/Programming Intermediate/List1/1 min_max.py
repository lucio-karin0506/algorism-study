T = int(input())
res_list = []

for test_case in range(1, T + 1):
    input_num = int(input())
    num_list = list(map(int, input().split()))
    res_list.append(max(num_list) - min(num_list))

for index, value in enumerate(res_list):
    print(f'#{index+1} {value}')