def check_bracket(input_str):
    input_list = []
    is_bracket_check = 0

    for letter in input_str:
        # 시작 괄호면 리스트에 추가
        if letter == '{' or letter == '(':
            input_list.append(letter)

        # 끝 괄호면
        elif letter == '}' or letter == ')':
            # 리스트에 원소 미 존재 시
            # 차피 끝 괄호가 먼저 들어갔기 때문에
            # 짝 안맞음
            if len(input_list) == 0:
                input_list.append(letter)
                is_bracket_check = 0
                break

            # 각 괄호 형태가 서로 안맞고 다른 경우
            elif (input_list[-1] == '{' and letter == ')') or (input_list[-1] == '(' and letter == '}'):
                input_list.append(letter)
                is_bracket_check = 0
                break

            # 리스트에 원소 존재 시
            # 짝 맞는 경우
            else:
                input_list.pop()

    # 리스트에 괄호 있으면
    if len(input_list) != 0:
        is_bracket_check = 0
    # 리스트에 괄호 없으면
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