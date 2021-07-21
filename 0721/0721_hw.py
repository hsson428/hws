def my_avg(*args):
    length = len(args)
    mean = sum(args)/length
    return round(mean, 1)

print(my_avg(77, 83, 95, 80, 70))