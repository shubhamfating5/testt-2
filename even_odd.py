def check_even_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

# Example usage:
num = 5  # Change this number to test
result = check_even_odd(num)
print(f'The number {num} is {result}.')