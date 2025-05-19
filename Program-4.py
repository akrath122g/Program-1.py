def count_multiples(numbers):
    multiples_count = {i: 0 for i in range(1, 10)}
    for number in numbers:
        for i in range(1, 10):
            if number % i == 0:
                multiples_count[i] += 1
    return multiples_count
# Example usage:
input_numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
output = count_multiples(input_numbers)
print(output)  # Output: {1: 11, 2: 8, 3: 4, 4: 4, 5: 3, 6: 2, 7: 0, 8: 1, 9: 1}
