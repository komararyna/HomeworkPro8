def memo():
    sl = {}

    def fibonachi(num):
        if sl.get(num):
            return sl.get(num)

        sl1 = []
        first_num = 0
        second_num = 1
        for item in range(20):
            first_num, second_num = second_num, first_num + second_num
            sl1.append(second_num)
        sl[num] = sl1
        return sl1[num]
    return fibonachi


x = memo()
print(x(2))
print(x(8))
