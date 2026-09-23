import sys

def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

def kilometers_to_miles(km: float) -> float:
    return km * 0.621371

def main():
    if len(sys.argv) < 3:
        print("Usage: python converter.py <type> <value>")
        print("Types: temp (Celsius -> Fahrenheit), dist (Km -> Miles)")
        sys.exit(1)

    conv_type = sys.argv[1].lower()
    try:
        val = float(sys.argv[2])
    except ValueError:
        print("Error: Value must be a valid number.")
        sys.exit(1)

    if conv_type == "temp":
        res = celsius_to_fahrenheit(val)
        print(f"{val}°C = {res:.2f}°F")
    elif conv_type == "dist":
        res = kilometers_to_miles(val)
        print(f"{val} km = {res:.2f} miles")
    else:
        print(f"Unknown conversion type: '{conv_type}'")

if __name__ == "__main__":
    main()
