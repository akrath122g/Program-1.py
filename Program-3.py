def generate_odd_numbers_condition(a: int):
    if a < 1:
        return []
    return [i for i in range(1, 2 * (a if a % 2 == 1 else a - 1), 2)]
# Example usage:
for i in range(1, 7):
    print(f"input a = {i}, then output :", generate_odd_numbers_condition(i))
