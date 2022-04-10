import sys
from string import ascii_lowercase

letter_list = list(sys.stdin.readline().strip())
alphabet_list = list(ascii_lowercase)
existed_list = list(set(alphabet_list) & set(letter_list))

res = [str(letter_list.index(alphabet)) if alphabet in existed_list else str(-1) for alphabet in alphabet_list]
print(' '.join(res))