# Clean control example, no secrets here.

from .utils import add_numbers

def greet(name: str) -> str:
    """Return a friendly greeting message."""
    total = add_numbers(2, 3)  # trivial call so utils is covered in the test run
    return f"Hello, {name}! (demo sum={total})"

if __name__ == "__main__":
    print(greet("CSEC141"))
