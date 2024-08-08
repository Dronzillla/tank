import pytest
from unittest.mock import patch, mock_open
from datetime import date
import os

from project import (
    get_leader_from_leaderboard,
    record_result_to_leaderboard,
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


if __name__ == "__main__":
    pytest.main()
