def count_word(target_word, test_word):
    word_count = {}

    for i in target_word:
        count = test_word.count(i)
        word_count[i] = count

    max_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[0][1]
    
    return max_count


if __name__ == '__main__':
    T = int(input())
    res = []

    for test_case in range(1, T + 1):
        target_word = list(input())
        test_word = list(input())

        count = count_word(target_word, test_word)
        res.append(count)

    for index, value in enumerate(res):
        print(f'#{index+1} {value}')