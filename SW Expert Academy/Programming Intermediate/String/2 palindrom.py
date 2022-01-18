def get_palin(word_canvas, word_len):
    palin_word = []
    row_num = len(word_canvas)

    count = 0
    # 행 탐색
    for i in range(row_num):
        # 전체 글자 수에서 찾고자 하는 회문 글자 수를 뺀 값만큼 탐색
        for j in range(0, row_num-word_len+1):
            # 각 단어를 처음~중간, 끝~중간으로 나누어 한글자씩 탐색
            for k in range(word_len//2):
                # 각 단어의 처음과 끝 글자, 두 번째와 두 번째 끝 글자 이런식으로 같은지 비교하고~
                if word_canvas[i][j+k] == word_canvas[i][j + word_len-1-k]:
                    count += 1
            # 각 단어를 처음~중간, 끝~중간으로 나누어 한글자씩 탐색하고
            # 탐색하고자 하는 회문길이의 절반값에 count가 일치하면
            if count == word_len//2:
                for l in range(j, j + word_len):
                    palin_letter = word_canvas[i][l]
                    palin_word.append(palin_letter)
            # 못찾고 다음 단어 탐색 시 count 초기화
            count = 0

    # 열 탐색
    count = 0
    for j in range(row_num):
        for i in range(0, row_num-word_len+1):
            for k in range(word_len // 2):
                if word_canvas[i+k][j] == word_canvas[i + word_len-1-k][j]:
                    count += 1
            if count == word_len//2:
                for l in range(i, i + word_len):
                    palin_letter = word_canvas[l][j]
                    palin_word.append(palin_letter)
            count = 0

    return ''.join(palin_word)

if __name__ == '__main__':
    T = int(input())
    res = []

    for _ in range(1, T + 1):
        size, word_len = map(int, input().split())
        word_canvas = []

        for _ in range(size):
            word = list(input())
            word_canvas.append(word)

        palin_word = get_palin(word_canvas, word_len)
        res.append(palin_word)

    for index, value in enumerate(res):
        print(f'#{index+1} {value}')