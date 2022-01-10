def solution(s):
    answer = s
    num_eng_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4',
                    'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

    for eng, num in num_eng_dict.items():
        answer = answer.replace(eng, num)

    return int(answer)
        

if __name__ == '__main__':
    s = "one4seveneight"
    s1 = '123'
    res = solution(s)
    print(res)