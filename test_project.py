import pytest
from unittest.mock import patch
from datetime import date
import csv

from project import (
    get_leader_from_leaderboard,
    record_result_to_leaderboard,
    print_program_menu,
)
from tank_game import TankGame
from person import Person
from utils import Format


# Test functionality related to TankGame class
class TestTankGame:
    @pytest.fixture
    def game(self):
        return TankGame()

    # Initial setup
    def test_initialization(self, game):
        assert game.tank_loc_x == 2
        assert game.tank_loc_y == 1
        assert game.tank_direction == {
            "north": False,
            "south": True,
            "east": False,
            "west": False,
        }
        assert game.score == 100

    # Test tank movement
    def test_move_left(self, game):
        game.left()
        assert game.tank_loc_x == 1
        assert game.tank_direction["east"] == True

    def test_move_right(self, game):
        game.right()
        assert game.tank_loc_x == 3
        assert game.tank_direction["west"] == True

    def test_move_up(self, game):
        game.up()
        assert game.tank_loc_y == 0
        assert game.tank_direction["north"] == True

    def test_move_down(self, game):
        game.down()
        assert game.tank_loc_y == 2
        assert game.tank_direction["south"] == True

    # Shooting
    def test_shoot_hit(self, game):
        game.target_loc_x = game.tank_loc_x
        game.target_loc_y = game.tank_loc_y + 1  # Target is directly south
        game.shoot()
        assert game.tank_S_hit == 1
        assert game.score == 150

    def test_shoot_miss(self, game):
        game.target_loc_x = game.tank_loc_x + 2  # Target is far east
        game.shoot()
        assert game.tank_S_hit == 0
        assert game.score == 75

    def test_game_over(self, game):
        game.tank_S_made = game.S_max
        score = game.start_game()
        assert score == game.score


# Test functionality related to Person class
class TestPerson:
    def setup_method(self):
        # Ensure Person.all is empty before each test
        Person.all.clear()

    def test_person_creation(self):
        person = Person("Alice", 100, date.today())
        assert person.name == "Alice"
        assert person.score == 100
        assert person.date == date.today()

    def test_get_maximum(self):
        person1 = Person("Alice", 100, date.today())
        person2 = Person("Bob", 150, date.today())
        assert Person.get_maximum() == 150

    def test_get_max_score_person_info(self):
        person1 = Person("Alice", 100, date.today())
        person2 = Person("Bob", 150, date.today())
        assert Person.get_max_score_person_info() == ["Bob", 150, date.today()]


# Test functionality related to Format class
class TestFormat:
    def test_print_center(self, capsys):
        Format.print_center("Hello", 20)
        captured = capsys.readouterr()
        assert captured.out == ".......Hello........\n"

    def test_print_right(self, capsys):
        Format.print_right("Hello", 20)
        captured = capsys.readouterr()
        assert captured.out == "...............Hello\n"


# get_leader_from_leaderboard
@pytest.fixture
def leaderboard_file(tmp_path):
    data = [
        {"name": "Alice", "score": "100", "date": "2024-01-01"},
        {"name": "Bob", "score": "150", "date": "2024-01-02"},
        {"name": "Charlie", "score": "150", "date": "2024-01-01"},
    ]
    file = tmp_path / "leaderboard.csv"
    with open(file, mode="w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "score", "date"])
        writer.writeheader()
        writer.writerows(data)
    yield file


def test_get_leader_from_leaderboard(leaderboard_file):
    with patch.object(
        Person, "get_max_score_person_info", return_value=["Bob", "150", "2024-01-02"]
    ) as mock_method:
        leader = get_leader_from_leaderboard(leaderboard_file)
        assert leader == ["Bob", "150", "2024-01-02"]
        mock_method.assert_called_once()


# record_result_to_leaderboard
def test_record_result_to_leaderboard(tmp_path):
    filename = tmp_path / "leaderboard.csv"
    user = "Alice"
    score = 150

    # Test with a new file
    record_result_to_leaderboard(filename, user, score)
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        # print(rows)
        assert len(rows) == 1
        assert rows[0]["name"] == user
        assert rows[0]["score"] == str(score)
        assert rows[0]["date"] == str(date.today())


# print_program_menu
def test_print_program_menu():
    program_menu_width = 50
    leader = ["Alice", "200", "2024-01-01"]

    with patch("utils.Format.print_center") as mock_print_center:
        print_program_menu(program_menu_width, leader)

        # Check the calls to print_center
        expected_calls = [
            (("", program_menu_width),),
            (("", program_menu_width),),
            (("Welcome! This is a tank game.", program_menu_width),),
            (("'start' To start a new game.", program_menu_width),),
            (("'instructions' To see game instructions.", program_menu_width),),
            (("'exit' To exit from program.", program_menu_width),),
            (("", program_menu_width),),
            (("", program_menu_width),),
            (
                (
                    f"Current leader is '{leader[0]}'. Scored '{leader[1]}' in '{leader[2]}'!",
                    program_menu_width,
                ),
            ),
            (("", program_menu_width),),
            (("", program_menu_width),),
        ]
        actual_calls = mock_print_center.call_args_list
        assert len(actual_calls) == len(expected_calls)
        for actual_call, expected_call in zip(actual_calls, expected_calls):
            assert actual_call == expected_call


if __name__ == "__main__":
    pytest.main()
