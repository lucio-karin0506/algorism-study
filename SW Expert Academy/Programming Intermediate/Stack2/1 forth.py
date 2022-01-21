def forth(input_list):
    ans_list = []
    ans = 0

    for letter in input_list:
        if type(int(letter)) == int:
            ans_list.append(letter)
        else:
            if letter == '+':
                ans = int(ans_list[0]) + int(ans_list[1])
                ans_list.pop()
                ans_list.pop()
                ans_list.append(ans)
            elif letter == '-':
                ans = int(ans_list[0]) - int(ans_list[1])
                ans_list.pop()
                ans_list.pop()
                ans_list.append(ans)
            elif letter == '*':
                ans = int(ans_list[0]) * int(ans_list[1])
                ans_list.pop()
                ans_list.pop()
                ans_list.append(ans)
            elif letter == '/':
                ans = int(ans_list[0]) / int(ans_list[1])
                ans_list.pop()
                ans_list.pop()
                ans_list.append(ans)
            elif letter == '.':
                if len(ans_list) == 1:
                    ans = ans_list.pop()
                else:                 
                    return 'error'

    return ans

if __name__ == '__main__':
    T = int(input())
    res = []

    for test_case in range(1, T + 1):
        input_list = list(input().split())
        ans = forth(input_list)
        res.append(ans)

    for idx, value in enumerate(res):
        print(f'#{idx+1} {value}')