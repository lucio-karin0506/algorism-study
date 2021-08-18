def solution(phone_book):
    answer = True
    phone_book.sort()
    # print(phone_book)
    for i in range(len(phone_book) - 1):
        if len(phone_book[i]) < len(phone_book[i + 1]):
            if phone_book[i + 1].startswith(phone_book[i]) == True:
                answer = False

    return answer

if __name__ == '__main__':
    book = ["12","123","1235","567","88"]
    a = solution(book)
    print(a)