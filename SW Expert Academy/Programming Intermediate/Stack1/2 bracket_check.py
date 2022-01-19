def check_bracket(input_str):
    input_list = []
    is_bracket_check = 0

    for letter in input_str:
        # 시작 괄호면 리스트에 추가
        if letter == '{' or letter == '(':
            input_list.append(letter)

        # 끝 괄호면
        elif letter == '}' or letter == ')':
            # 리스트에 원소 존재 시
            if len(input_list) != 0:
                pop_letter = input_list.pop()
            # 리스트에 원소 미 존재 시
            else:
                is_bracket_check = 0
                break

            # 각 괄호 형태가 서로 안맞고 다른 경우
            if (pop_letter == '{' and letter == ')') or (pop_letter == '(' and letter == '}'):
                is_bracket_check = 0
                break

    if len(input_list) != 0:
        is_bracket_check = 0
    else:
        is_bracket_check = 1

    return is_bracket_check

                 

if __name__ == '__main__':
    T = int(input())
    res = []

    for _ in range(1, T + 1):
        input_str = input()
        checked_bracket = check_bracket(input_str)
        res.append(checked_bracket)

    for idx, value in enumerate(res):
        print(f'#{idx+1} {value}')