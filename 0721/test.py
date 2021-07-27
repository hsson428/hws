def get_strong_name(a, b):
    score0 = 0
    score1 = 0
    zipped = list(zip([a, b], [score0, score1]))
    for string, score in zipped:
        for i in string:
            score += ord(i)
    print(zipped)

print(get_strong_name('z', 'a'))