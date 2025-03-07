def find_largest_smallest(numbers):
    if not numbers:
        return None, None

    largest = smallest = numbers[0]

    for num in numbers[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
largest, smallest = find_largest_smallest(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
