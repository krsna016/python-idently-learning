"""
This is a docstring
"""


class User:
    """
    This is the base class for creating users
    """

    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def show_id(self) -> None:
        """
        Prints the user id
        :return: None
        """
        print(self.user_id)


def user_exist(user: User, database: set[User]) -> bool:
    """
    Checks if a user is inside the database
    :param user: The user to check for
    :param database: The database to check inside
    :return: bool
    """
    return user in database


def main() -> None:
    user: User = User(1)
    user.show_id()

    bob: User = User(22)
    anna: User = User(23)

    database: set[User] = {bob, anna}
    if user_exist(bob, database):
        print("User Exists.")
    else:
        print("No User Founded !!")

    print(User.__doc__)
    print(user_exist.__doc__)


if __name__ == '__main__':
    main()
