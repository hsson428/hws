# def get_secret_word(l):
#     word = ''
#     for i in l:
#         word += chr(i)
#     return word

# print(get_secret_word([83, 115, 65, 102, 89]))

# def get_secret_number(s):
#     n = 0
#     for i in s:
#         n += ord(i)
#     return n

# print(get_secret_number('tom'))

def get_strong_word(a, b):
    n1 = n2 = 0
    for i in a:
        n1 += ord(i)
    for i in b:
        n2 += ord(i)
    return a if n1>n2 else b

print(get_strong_word('z', 'a'))
print(get_strong_word('tom', 'john'))