def solution1(lottos, win_nums):
    cnt = len(set(lottos) & set(win_nums))
    zero = lottos.count(0)

    return [7-max(cnt+zero, 1), 7-max(cnt, 1)]

def solution2(lottos, win_nums):
    # 일치하는 번호 개수 인덱스에 대응되는 순위가 위치한 순위 리스트
    rank_list = [6, 6, 5, 4, 3, 2, 1]
    # 일치하는 번호 개수
    cnt = 0

    for i in lottos:
        if i in win_nums:
            cnt += 1

    high_rank = rank_list[cnt+lottos.count(0)]
    low_rank = rank_list[cnt]

    return [high_rank, low_rank]

if __name__ == '__main__':
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]

    res = solution2(lottos, win_nums)
    print(res)