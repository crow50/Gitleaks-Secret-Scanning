from src.app import greet
from src.utils import add_numbers

def test_greet_contains_name_and_sum():
    msg = greet("Tester")
    assert "Hello, Tester!" in msg or "Hello, Tester" in msg
    assert "(demo sum=5)" in msg

def test_add_numbers():
    assert add_numbers(2, 3) == 5
