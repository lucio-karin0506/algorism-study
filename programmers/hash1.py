# def solution(participant, completion):
#     answer = {}
#     for i in participant:
#         answer[i] = answer.get(i, 0) + 1
#         # print(answer)
#     for j in completion:
#         answer[j] -= 1
#         # print(answer)
#     for k in answer:
#         if answer.get(k) == 1:
#             return k

import collections

# def solution(participant, completion):
#     print(collections.Counter(participant))
#     print(collections.Counter(completion))
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     print(answer)
#     return list(answer.keys())

# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}

#     for part in participant:
#         dic[hash(part)] = part
#         temp += hash(part)
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]

#     return answer

def solution(participant, completion):
    print(participant.sort())
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant) - 1]

if __name__ == '__main__':
    participant = ['a', 'b', 'c', 'c', 'd']
    completion = ['a', 'b', 'c']

    a = solution(participant, completion)
    print(a)