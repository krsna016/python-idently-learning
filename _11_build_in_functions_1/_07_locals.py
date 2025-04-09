print(locals())

NAME: str = 'Bob'


def add(a: int, b: int) -> None:
    result: int = a + b
    print(f"{a} + {b} = {result}")
    print(f'add() has this locals : {locals()}')
    print(f"add() can see this globals : {globals()}")
    print(NAME)


add(1, 2)
