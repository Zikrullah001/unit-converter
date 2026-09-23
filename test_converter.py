from converter import celsius_to_fahrenheit, kilometers_to_miles

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0

def test_kilometers_to_miles():
    assert round(kilometers_to_miles(1), 2) == 0.62

if __name__ == "__main__":
    test_celsius_to_fahrenheit()
    test_kilometers_to_miles()
    print("All tests passed!")
