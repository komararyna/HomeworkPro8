def func(end):
    first_num = 2
    second_num = 2
    count = 0
    while count <= end:
        def get_next():
            nonlocal first_num
            nonlocal second_num
            nonlocal count
            next_num = first_num * second_num
            first_num, second_num = second_num, next_num
            return next_num
        return get_next()


f = func(10)

for i in range(10):
    print(f)
