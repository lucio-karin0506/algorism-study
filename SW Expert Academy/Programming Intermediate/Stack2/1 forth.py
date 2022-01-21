def forth(input_list):
    ans_list = []

    for letter in input_list:
        if type(eval(letter)) != int:
            pass

    return ans_list[0]

if __name__ == '__main__':
    T = int(input())
    res = []

    for test_case in range(1, T + 1):
        input_list = list(input().split())
        ans = forth(input_list)
        res.append(ans)

    for idx, value in enumerate(res):
        print(f'#{idx+1} {value}')