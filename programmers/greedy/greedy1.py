def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)

    for i in new_lost:
        if i + 1 in new_reserve:
            new_reserve.remove(i + 1)
        elif i - 1 in new_reserve:
            new_reserve.remove(i - 1)
        else:
            n -= 1
        
    return n

if __name__ == '__main__':
    n = 5
    lost = [2, 4]
    reserve = [1, 3, 5]
    a = solution(n, lost, reserve)
    print(a)