def binary_search(num_list, start, end, target):
    # 쪽 탐색 횟수
    count = 1

    # 이진탐색 수행
    while start <= end:

        # 중앙값 갱신
        mid = (start + end) // 2

        # 찾고자 하는 값이 갱신된 중앙값이랑 일치할 때
        if target == num_list[mid]:
            return count

        # 중앙값보다 작을 때
        elif target < num_list[mid]:
            end = mid - 1
            count += 1

        # 중앙값보다 클 때
        else:
            start = mid + 1
            count += 1

    return None


T = int(input())
res = []
for test_case in range(1, T + 1):
    page, a_key, b_key = map(int, input().split())

    # 전체 페이지 리스트
    num_list = [i for i in range(1, page+1)]

    # 시작, 끝 값 인덱스 선언
    start = 0
    end = len(num_list) - 1

    # 승부 판별
    a_count = binary_search(num_list, start, end, a_key)
    b_count = binary_search(num_list, start, end, b_key)

    if a_count < b_count:
        res.append('A')
    elif a_count > b_count:
        res.append('B')
    else:
        res.append(0)

for index, value in enumerate(res):
    print(f'#{index+1} {value}')