def get_rect_num(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    # dynamic programmin, 점화식 형태
    return get_rect_num(n-1) + 2*get_rect_num(n-2)

if __name__ == '__main__':
    T = int(input())
    res = []

    for test_case in range(1, T + 1):
        N = int(input())
        rect_num = get_rect_num(N // 10)
        res.append(rect_num)
        
    for idx, value in enumerate(res):
        print(f'#{idx+1} {value}')