def solution(research, n, k):
    answer = ''
    word_issue_dict = {}
    word_count_list = []

    for num in range(1, len(research) + 1):
        word_letter = research[num - 1]
        word_issue_dict[word_letter] = word_count_list.append({num : word_letter})
    return answer

if __name__ == '__main__':
    research = ["abaaaa","aaa","abaaaaaa","fzfffffffa"]
    n = 2
    k = 2

    res = solution(research, n, k)
    print(res)