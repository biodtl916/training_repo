from nose.tools import *
from training.game import Room

def test_room():
    gold = Room("GoldRoom",
        """This room has gold in it""")
    assert_equal(gold.name, "GoldRoom")
