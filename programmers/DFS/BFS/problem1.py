def solution(numbers, target):
    answer = 0
    visited = []

    visited.append(0)

    for num in numbers:
        tmp = []
        for i in visited:
            tmp.append(i + num)
            tmp.append(i - num)
        visited = tmp

    for i in visited:
        if i == target:
            answer += 1

    return answer

if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    s = solution(numbers, target)
    print(s)