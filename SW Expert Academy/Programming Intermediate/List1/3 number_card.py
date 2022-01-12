T = int(input())
answer_list = []
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num_size = int(input())
    input_num = input()

    input_num_list = list(map(int, input_num))
    count_dict = {}

    for value in input_num_list:
        count_dict[value] = input_num_list.count(value)

    sorted_val = sorted(count_dict.items(), key=lambda x: x[1])
    sorted_val_item = [i[1] for i in sorted_val]

    if len(sorted_val_item) != len(set(sorted_val_item)):
        sorted_val = [i for i in sorted_val if i[1] == max(sorted_val_item)]
        max_num = max([i[0] for i in sorted_val])
        sorted_val = [i for i in sorted_val if i[0] == max_num]
        answer_list.append(sorted_val[0])
    else:
        answer_list.append(sorted_val[-1])

for index, value in enumerate(answer_list):
    print(f'#{index+1} {value[0]} {value[1]}')