T = int(input())
res = []

for test_case in range(1, T + 1):
    input_num = int(input())
    num_list = list(map(int, input().split()))
    temp = []

    for num in num_list:

        temp.append(str(max(num_list)))
        temp.append(str(min(num_list)))

        num_list.remove(max(num_list))
        num_list.remove(min(num_list))

        if len(num_list) == 2:
            temp.append(str(max(num_list)))
            temp.append(str(min(num_list)))

    res.append(temp)

for index, value in enumerate(res):
    value_text = ' '.join(value[:10])
    print(f'#{index+1} {value_text}')