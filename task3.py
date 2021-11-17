def my_func(seq, predicate):
    for item in seq:
        if predicate(item):
            yield item


seq = [1, 23, 121, 324, 45, 17, 24, 28]
print(*list(my_func(seq, lambda x: x > 100)))
y = [item for item in my_func(seq, lambda x: x % 2 == 0)]
print(y)
