class Count:
    def __init__(self, count=0):
        self.count = count


def increment(c1, times2):
    print('into c1:', id(c1))
    print("into times2:", id(times2))
    c1.count += 1
    # print('c:', c.count)
    print('after +1, c1:', id(c1))
    times2 += 1
    # print('t:', times)
    print('after +1, times2:', id(times2))


if __name__ == '__main__':
    c = Count()
    times = 0
    print('original times:', id(times))
    print('original c:', id(c))
    print(" ")

    for i in range(3):
        increment(c, times)


    def foo(lst):
        print("enter foo: {}".format(id(lst)))
        lst.append(1)
        print("after append: {}".format(id(lst)))
        lst = [2]
        print("after [2]: {}".format(id(lst)))

    print("")
    m = []
    print("original {}".format(id(m)))
    foo(m)
    print("after foo {}".format(id(m)))
    print(m)
