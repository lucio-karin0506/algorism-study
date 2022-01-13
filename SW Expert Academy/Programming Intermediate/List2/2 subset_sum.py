def get_subset(num_list):
    # subset list
    subset_list = []

    # 집합 A에대한 부분집합 이중리스트
    for i in range(1 << len(num_list)):
        # 개별 부분집합
        subset = []

        # 비트부호가 1인부분만 추려 원래 값으로 대입
        for j in range(len(num_list)):
            if i & (1 << j):
                subset.append(num_list[j])
        
        # 부분집합 리스트 최종 리스트에 추가
        subset_list.append(subset)

    return subset_list

'''
    main
'''
# 집합 A
num_list = [i for i in range(1, 13)]
# 집합 A의 부분집합
subset_list = get_subset(num_list)

T = int(input())
res = []

for test_case in range(1, T + 1):
    # 부분집합 원소 개수 및 합
    N, K = map(int, input().split())

    # 부분집합 개수
    count = 0

    for subset in subset_list:
        if len(subset) == N and sum(subset) == K:
            count += 1

    res.append(count)
'''
    print
'''
for index, value in enumerate(res):
    print(f'#{index+1} {value}')