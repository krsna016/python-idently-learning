import time


class Internet:
    def __init__(self, provider: str) -> None:
        self.provider = provider

    def connect(self) -> None:
        print(f'[{self.provider}] Connecting...')
        time.sleep(2)
        print(f'[{self.provider}] You are now connected...')


def test_connect() -> None:
    print("[Provider] You are now connected...")


def main() -> None:
    internet: Internet = Internet('Jio')
    # This is called monkey patching it replaces the original method with a new one without changing the original code
    # It is different from overriding as in overriding we change the method in the class itself but here we are changing the method outside the class
    internet.connect = test_connect  # type: ignore
    internet.connect()


if __name__ == '__main__':
    main()
