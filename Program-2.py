def generate_odd_numbers(a: int):
    if a < 1:
        return []
    return [i for i in range(1, 2 * a, 2)]
# Example usage:
for i in range(1, 5):
    print(f"input a = {i}, then output :", generate_odd_numbers(i))
