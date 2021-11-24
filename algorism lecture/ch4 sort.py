'''
    선택정렬
    1. 매번 가장 작은 것을 선택
    2. 뒤에 있는 리스트 원소 중 가장 적은 값의 인덱스를 찾아 현재 인덱스 원소와 비교하여 교환
    3. 시간적 복잡도가 꽤나 큼
'''
def selection_sort(arr):
    for index in range(len(arr)):
        # 가장 작은 원소의 인덱스
        min_index = index
        for next_index in range(index+1, len(arr)):
            if arr[min_index] > arr[next_index]:
                min_index = next_index
        # swap
        arr[index], arr[min_index] = arr[min_index], arr[index]
    return arr

'''
    삽입정렬
    1. 데이터가 거의 정렬되어 있을 때 매우 효율적
    2. 특정 데이터를 적절한 위치에 삽입
    3. 첫 번째 데이터는 그 자체로 정렬되어 있다는 판단 하에 두 번째 데이터부터 시작
'''
def insert_sort(arr):
    for index in range(1, len(arr)):
        # 선택된 인덱스 앞에 있는 인덱스들 하나씩 불러옴
        for prev_index in range(index, 0, -1):
            # 선택된 인덱스가 앞에 있는 인덱스들보다 작다면
            if arr[prev_index] < arr[prev_index-1]:
                # 앞에 있는 인덱스 swap
                arr[prev_index], arr[prev_index-1] = arr[prev_index-1], arr[prev_index]
            # 앞에 있는 인덱스들보다 크다면
            else:
                # 왼쪽으로 이동하는 것 멈추고 반복문 탈출
                break
                
    return arr

'''
    퀵정렬
    1. 대부분의 정렬 라이브러리 근간이 되는 알고리즘
    2. 기준 설정 후 다음 쿤 수와 작은 수 교환한 후 리스트 반으로 나누는 동작 방식
    3. 피벗: 교환하기 위한 기준
'''

if __name__ == '__main__':
    test_arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]