def solution(n, cloth_type):
    count = 0

    cloth_dic = {}
    for cloth in cloth_type:
        if cloth[1] in cloth_dic:
            cloth_dic[cloth[1]].append(cloth[0])
        else:
            cloth_dic[cloth[1]] = [cloth[0]]

    cloth_num = [str(len(i) + 1) for i in cloth_dic.values()]

    try:
        count = eval('*'.join(cloth_num)) - 1
    except:
        pass

    return count

if __name__ == '__main__':
    res_list = []
    T = int(input())
    for _ in range(T):
        n = int(input())
        cloth_type = [input().split() for _ in range(n)]

        res = solution(n, cloth_type)
        res_list.append(res)

    for i in res_list:
        print(i)