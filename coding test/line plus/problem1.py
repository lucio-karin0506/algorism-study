def solution(student, k):
    answer = 0
    
    for stu in student:
        if stu == 1:
            answer += 1
    return answer

if __name__ == '__main__':
    student = [0, 1, 0, 0]
    k = 1
    res = solution(student, k)
    print(res)