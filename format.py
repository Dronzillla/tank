class Format:
    @staticmethod
    def bc_print(astr: str, anumb: int) -> None:
        print(astr.center(anumb * 3 + 1, "."))

    @staticmethod
    def br_print(astr: str, anumb: int) -> None:
        print(astr.rjust(anumb * 3 + 1, "."))

    @staticmethod
    def bl_print(astr: str, anumb: int) -> None:
        print(astr.ljust(anumb * 3 + 1, "."))


def main(): ...


if __name__ == "__main__":
    main()
