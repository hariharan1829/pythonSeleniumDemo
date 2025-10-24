import pytest

message = "kill"

def test_check():
    assert message == "Kills"

def test_greet():
    a = 5
    b = 6
    assert a+5 == 11