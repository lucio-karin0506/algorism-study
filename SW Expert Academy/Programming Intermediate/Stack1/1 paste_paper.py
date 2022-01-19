def get_rect_num(size):
    rect_num = ''
    return rect_num

if __name__ == '__main__':
    T = int(input())
    res = []

    for test_case in range(1, T + 1):
        size = int(input())
        rect_num = get_rect_num(size)
        res.append(rect_num)

    for idx, value in enumerate(res):
        print(f'#{idx+1} {value}')