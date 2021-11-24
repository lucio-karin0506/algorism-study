def solution(id_list, report, k):
    answer = []
    problem_user = []
    vote_dict = {}
    
    for info in report:
        for user in id_list:
            if user == info.split(' ')[0]:
                problem_user.append(info.split(' ')[1])
                vote_dict[user] = problem_user
            else:
                vote_dict[user] = 0
    
    return answer

if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    res = solution(id_list, report, k)
    print(res)