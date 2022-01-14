T = int(input())
res = []

for test_case in range(1, T + 1):
    target = input()
    input_str = input()

    a = input_str.find(target)
    ans = 0

    if a != -1:
        ans = 1
    else:
        ans = 0

    res.append(ans)

for index, value in enumerate(res):
    print(f'#{index+1} {value}')