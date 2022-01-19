def check_bracket(size):
    rect_num = ''
    return rect_num

if __name__ == '__main__':
    T = int(input())
    res = []

    for test_case in range(1, T + 1):
        input_str = input()
        checked_bracket = check_bracket(input_str)
        res.append(checked_bracket)

    for idx, value in enumerate(res):
        print(f'#{idx+1} {value}')