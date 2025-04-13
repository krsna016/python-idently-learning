# Walrus operator: :=
# The walrus operator is a new assignment expression operator introduced in Python 3.8.
# It allows you to assign a value to a variable as part of an expression.
# This can make your code more concise and readable in certain situations.

def descriptive(numbers: list[int]) -> dict:
    # n_length: int = len(numbers)
    # n_sum: int = sum(numbers)
    # n_mean: float = n_sum/n_length
    #
    # details: dict = {
    #     'length' : n_length,
    #     'sum' : n_sum,
    #     'mean' : n_mean
    # }

    # Now using walrus operator we can do like this:
    details: dict = {
        'length': (n_length := len(numbers)),
        'sum': (n_sum := sum(numbers)),
        'mean': (n_mean := (n_sum / n_length))
    }

    return details


def main() -> None:
    print(descriptive(numbers := [1, 10, 5, 200, -4, 7]))


if __name__ == '__main__':
    main()

# Example:
my_dict: dict[int, str] = {
    1: 'Cup',
    2: 'Chair'
}
if item := my_dict.get(3):
    print(f'Got: {item}')
else:
    print('Item not Found!!')
