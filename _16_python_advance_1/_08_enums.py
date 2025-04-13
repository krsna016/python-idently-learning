from enum import Enum


# class State(Enum):
#     OFF = 0
#     ON = 1
#
# # state: State = State.OFF
# state: State = State.ON
#
# if state == State.ON:
#     print("The device is turned on.")
# elif state == state.OFF:
#     print("The device is turned off.")
# else:
#     print("Unknown input!!")


class Color(Enum):
    RED = 'R'
    GREEN = 'G'
    BLUE = 'B'


# red: Color = Color.RED
# print(red)
# print(red.value)
# print(red.name)
# print(Color('R'))

def buy_car(brand: str, color: Color) -> None:
    if color == Color.RED:
        print(f"You bought a smoking hot red {brand}.")
    elif color == Color.GREEN:
        print(f"You bought a chill green {brand}!.")
    elif color == Color.BLUE:
        print(f"You bought a smoking blue {brand}!")
    else:
        print("Unknown Color!!!")


def main() -> None:
    buy_car("Tesla", Color.BLUE)
    buy_car('BMW', Color.RED)


if __name__ == '__main__':
    main()
