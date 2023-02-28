d = {'a': 2, 'b': 4, 'c': 10}

# def add(*args) -> int:
#     print(args)
#     return sum([int(i) for i in args])
#     # return


# # test = add(3, 5, 43)
# test = add(**d)


# print(f"{**d}")
# print( test)


def calc(n, **kwargs):
    # print(kwargs)
    n += kwargs['add']
    n *= kwargs['multiply']


calc(5, add=3, multiply=5)


def multi(**kwargs):
    test = kwargs.get('test')
    return test
    pass


print(multi(test=5))


class Car():
    """docstring for Car."""

    def __init__(self, **kw):
        super(Car, self).__init__()
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('color')
        self.seats = kw.get('seats')


my_car = Car(make='nissan', seats='2')
# with open('./test.txt', 'w') as f:
#     f.write(str(my_car))

print(my_car)
