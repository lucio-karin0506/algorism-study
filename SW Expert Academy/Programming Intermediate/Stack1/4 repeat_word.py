def check_repeat(word_list):
    word_len = len(word_list)

    # 글자 수 하나일 경우 리턴 ㄱ
    if word_len == 1:
        return word_len

    # 전체 글자에서
    for idx in range(1, word_len):

        # 인접한 두 글자끼리 동일한지 비교
        if word_list[idx-1] == word_list[idx]:
            left = word_list[idx-1]
            right = word_list[idx]

            word_list.remove(left)
            word_list.remove(right)

            # 재귀 호출 수행
            return check_repeat(word_list)

        # 동일하지 않으면
        else:
            # 전체 글자 수 만큼 반복문 안 돌았으면 패스
            if idx != word_len-1:
                pass
            # 돌았으면 해당 글자 수 리턴 ㄱ
            else:
                return word_len
            


if __name__ == '__main__':
    T = int(input())
    res = []

    for _ in range(1, T + 1):
        word_list = list(input())
        checked_word_num = check_repeat(word_list)
        res.append(checked_word_num)

    for idx, value in enumerate(res):
        print(f'#{idx+1} {value}')