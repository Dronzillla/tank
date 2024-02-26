import datetime


# Create a class object for a person
class Person:
    # A list of all persons
    all = []

    def __init__(self, name: str, score: int, date: datetime.date) -> None:
        self.name = name
        self.score = score
        self.date = date
        # Add object to a list
        Person.all.append(self)

    def __repr__(self):
        return f"Person('{self.name}', '{self.score}', '{self.date}')"

    @classmethod
    def get_maximum(cls) -> int:
        # Get maximum value and return it
        maximum = max(person.score for person in Person.all)
        return maximum

    @classmethod
    def get_max_person(cls) -> list:
        for person in Person.all:
            if person.score == cls.get_maximum():
                # return person information as a list
                return [person.name, person.score, person.date]


def main(): ...


if __name__ == "__main__":
    main()
