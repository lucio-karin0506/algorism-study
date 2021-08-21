def solution(clothes):
    answer = 1
    clothes_cate = []
    temp = []

    for item in clothes:
        clothes_cate.append(item[1])

    for i in set(clothes_cate):
        a = clothes_cate.count(i)
        temp.append(a + 1)

    for i in temp:
        if i == 0:
            return 0
        else:
            answer *= i

    return answer - 1

def solution2(clothes):
    from collections import Counter
    from functools import reduce

    cnt = Counter([kind for _, kind in clothes])
    answer = reduce(lambda x, y: x * (y + 1), cnt.values(), 1) - 1
    return answer

if __name__ == '__main__':
    import time
    start = time.time()
    item = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], 
        ["green_turban", "headgear"]]
    item1 = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
    # a = solution(item)
    # print(a)
    # print(time.time() - start)
    # 0.0009591579437255859

    b = solution2(item)
    # print(time.time() - start)
    # 0.011008262634277344