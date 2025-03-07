def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
even_numbers = filter_even_numbers(numbers)
print("Even numbers:", even_numbers)