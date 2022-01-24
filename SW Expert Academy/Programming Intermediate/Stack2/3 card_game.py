def get_winner_num(num_list, start, end):
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        left = get_winner_num(num_list, start, mid)
        right = get_winner_num(num_list, mid+1, end)

        return find_winner(num_list, left, right)

def find_winner(num_list, left, right):
    l, r = num_list[left-1], num_list[right-1]

    # 비기는 경우, 더 낮은 인덱스 값 리턴
    if l == r:
        return left
    # 가위
    elif l == 1:
        if r == 2:
            return right
        elif r == 3:
            return left
    # 바위
    elif l == 2:
        if r == 1:
            return left
        elif r == 3:
            return right
    # 보
    elif l == 3:
        if r == 1:
            return right
        elif r == 2:
            return left


if __name__ == '__main__':
    T = int(input())
    res = []

    for _ in range(1, T+1):
        N = int(input())
        num_list = list(map(int, input().split()))
        ans = get_winner_num(num_list, 1, N)
        res.append(ans)

    for idx, value in enumerate(res):
        print(f'#{idx+1} {value}')