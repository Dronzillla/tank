class Format:
    @staticmethod
    def print_center(words: str, chars: int) -> None:
        print(words.center(chars, "."))

    @staticmethod
    def print_right(words: str, chars: int) -> None:
        print(words.rjust(chars, "."))
