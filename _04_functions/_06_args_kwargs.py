def add_nums_get_sums(*args: int) -> int:
    sums = 0
    for i in args:
        sums += i
    print(args)
    return sums


print(add_nums_get_sums(1, 2, 3, 4, 5))


def pin_position(**kwargs: int) -> None:
    print(kwargs)


pin_position(x=10, y=20)
