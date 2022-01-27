def solution(numbers, target):
    answer = 0
    visited = []
    visited.append(0)

    for num in numbers:
        temp = []
        for i in visited:
            temp.append(i + num)
            temp.append(i - num)
        visited = temp

    for i in visited:
        if i == target:
            answer += 1

    return answer

if __name__ == '__main__':
    numbers = [1, 1, 1, 1, 1]
    target = 3
    s = solution(numbers, target)
    print(s)