from collections import defaultdict

def solution(row, col, words):
    count = 0
    start, end = 0, row-1

    while start <= end:
        mid = (start + end) // 2

        # 문자열 중복 확인
        is_duplicated = True
        dict = defaultdict(int)

        for j in range(col):
            temp = ''
            for i in range(mid, row):
                temp += str(words[i][j])
            
            if not dict[temp]:
                dict[temp] += 1

            else:
                is_duplicated = False
                break

        if is_duplicated:
            count = mid
            start = mid + 1
        
        else:
            end = mid - 1

    return count


if __name__ == '__main__':
    row, col = map(int, input().split())
    words = [list(input()) for _ in range(row)]

    res = solution(row, col, words)
    print(res)