def get_palin(word_canvas, word_len):
    palin_word = ''

    # 행 단위 회문 탐색
    for word in word_canvas:
        if word == word[::-1]:
            palin_word = word

    return palin_word

if __name__ == '__main__':
    T = int(input())
    res = []

    for _ in range(1, T + 1):
        size, word_len = map(int, input().split())
        word_canvas = []

        for _ in range(size):
            word = input()
            word_canvas.append(word)

    palin_word = get_palin(word_canvas, word_len)
    res.append(palin_word)

    for index, value in enumerate(res):
        print(f'#{index+1} {value}')