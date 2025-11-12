'''
Temperature Converter

This is a simple temprature conversion program. Users can input a temperature from the command line in F or C and program outputs converted value.

Original Author: Joseph Kaiser
Creation Date: 10/31/2025
'''

K = 273.15

# Drives match function for temperature_converter() function.
CONVERTERS = {
    ('c','c'): lambda t: t,
    ('f','f'): lambda t: t,
    ('k','k'): lambda t: t,
    ('c','f'): lambda t: (9.0/5.0)*t + 32.0,
    ('c','k'): lambda t: t + K,
    ('f','c'): lambda t: (5.0/9.0)*(t - 32.0),
    ('f','k'): lambda t: (5.0/9.0)*(t - 32.0) + K,
    ('k','c'): lambda t: t - K,
    ('k','f'): lambda t: (9.0/5.0)*(t - K) + 32.0,
}

def get_temp(prompt):
    while True:
        s = input(prompt).strip().lower()
        if s == 'q':
            return None
        try:
            return float(s)
        except ValueError:
            print("Please input a valid number or 'q' to quit.")

def get_unit(prompt):
    while True:
        s = input(prompt).strip().lower()
        if s == 'q':
            return None
        if s in ('c', 'f', 'k'):
            return s
        print("Please enter a valid temperature unit (C, F, K).")

# Match function below similar to if/elsif tree checking all temperature pairs for a match. 
# But is O(n) rather than O(n**2) like if/elsif format.
def convert_pairwise(temp: float, unit: str, target: str) -> float | None:
    func = CONVERTERS.get((unit.lower(), target.lower()), None)
    return func(temp) if func is not None else None

def main():
    print(
        "This program converts temperatures between Celsius, Fahrenheit, and Kelvin.\n"
        "Enter units as letters (C, F, K). Enter 'q' at any prompt to quit.\n"
    )
    while True:
        u = get_unit("Enter input unit (C, F, K) > ")
        if u is None:
            break

        a = get_temp("Enter temperature as a number > ")
        if a is None:
            break

        t = get_unit("Enter target unit (C, F, K) > ")
        if t is None:
            break

        # result = temperature_converter(a, u, t)
        import pdb; pdb.set_trace()
        result = convert_pairwise(a, u, t)
        if result is None:
            print("Conversion failed — invalid unit combination.")
        else:
            print(f"{a:.2f}{u.upper()} → {result:.2f}{t.upper()}")

if __name__ == "__main__":
    main()
