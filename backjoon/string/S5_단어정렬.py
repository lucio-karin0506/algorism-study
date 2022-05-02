T = int(input())
words = [input() for _ in range(T)]
words_len = {word : len(word) for word in words}

# 길이 순으로 단어 정렬
words_len = dict(sorted(words_len.items(), key=lambda x: x[1]))

# 고유 단어 길이 리스트
word_len_num = list(set(words_len.values()))

res = []
for word_len in word_len_num:
    # 해당 길이를 가진 단어가 한 개일 경우,
    if list(words_len.values()).count(word_len) == 1:
        res.append(words_len.keys())

    # 해당 길이를 가진 단어가 두 개 이상일 경우,
    else:
        pass