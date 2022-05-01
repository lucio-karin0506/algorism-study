def solution(id_list, reports, k):
    stop = []
    answer = [0] * len(id_list)

    report_dic = {id : [] for id in id_list}

    for i in set(reports):
        report = i.split(' ')
        stop.append(report[1])
        report_dic[report[0]].append(report[1])

    print(stop)

    print(report_dic)
    for value in report_dic.values():
        if len(value) >= k:
            for v in value:
                pass

    return answer

if __name__ == '__main__':
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    answer = solution(id_list, report, k)
    print(answer)