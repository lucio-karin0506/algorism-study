'''
    - 순차 탐색
    - 앞에서부터 데이터 하나씩 차례대로 확인하는 방법
    - 배열 내부 정렬 안해도 됨
'''

def sequential_search(target, array):
    for index, arr in enumerate(array):
        if arr == target:
            return index + 1

'''
    - 이진 탐색
    - 찾으려는 데이터와 중간점 위치에 있는 데이터 반복적으로 비교
    - 데이터 무작위 x, 정렬되어 있을 때 빨리 탐색 가능
'''
# 재귀함수 이용
def binary_search1(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search1(array, target, start, mid - 1)

    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search1(array, target, mid + 1, end)


# 반복문 사용
def binary_search2(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# 실전문제 1
def search_part(N, N_arr, M, M_arr):
    searched_result = []

    N_arr = sorted(N_arr)
    result_flag = 'no'

    for target in M_arr:
        start = 0
        end = N - 1

        while start <= end:
            mid = (start + end) // 2

            if N_arr[mid] == target:
                result_flag =  'yes'
                break
            elif N_arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        searched_result.append(result_flag)
    
    return searched_result

# 실전문제2
def get_dduck_length(N, M, dduck_length):
    # 이진 탐색 위한 시작, 끝 설정
    start = 0
    end = max(dduck_length)

    # 이진 탐색 수행
    result = 0
    while start <= end:
        total = 0
        mid = (start + end) // 2

        for x in dduck_length:
            # 잘랐을 때 떡의 양 계산
            if x > mid:
                total += (x - mid)
        
        # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
        if total < M:
            end = mid - 1
        # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로 여기에 result 기록
            start = mid + 1

    return result


if __name__ == '__main__':
    # print(sequential_search(7, [1, 2, 3, 4, 7, 9, 8]))
    # print(binary_search1([1, 3, 5, 7, 9, 11], 7, 0, 5))
    # result = binary_search2([1, 2, 7, 9, 10], 9, 0, 4)
    # print('no target' if result == None else result + 1)

    # 빠른 입력받기
    # import sys
    # input_data = sys.stdin.readline().rstrip()
    # print(input_data)

    # 실전문제 1 input
    # N = int(input())
    # N_arr = list(map(int, input().split()))
    # M = int(input())
    # M_arr = list(map(int, input().split()))
    # print(search_part(N, N_arr, M, M_arr))

    # 실전문제 2 input
    N, M = map(int, input().split())
    dduck_length = list(map(int, input().split()))
    print(get_dduck_length(N, M, dduck_length))