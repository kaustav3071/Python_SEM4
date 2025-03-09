# Helper function for prime numbers (needed for task #3)
def prime_numbers(start, end):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [n for n in range(start, end + 1) if is_prime(n)]

# 1. Remove duplicates using set
def remove_duplicates_list(lst):
    return list(set(lst))

# 2. Symmetric difference of multiple sets
def symmetric_diff(sets_list):
    result = sets_list[0]
    for s in sets_list[1:]:
        result = result.symmetric_difference(s)
    return result

# 3. Intersection of even and prime numbers
evens = set(range(0, 20, 2))
primes = set(prime_numbers(1, 20))
even_primes = evens.intersection(primes)

# 4. Union of odd numbers and multiples of 9
odds = set(range(1, 20, 2))
nines = set(range(0, 20, 9))
odd_or_nines = odds.union(nines)

# 5. Difference of positive and negative numbers
positives = set(range(1, 10))
negatives = set(range(-9, 0))
positive_only = positives.difference(negatives)

# Example usage
print(remove_duplicates_list([1, 2, 2, 3, 3]))  # [1, 2, 3]
print(symmetric_diff([{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]))  # {1, 5}
print(even_primes)  # {2}
print(odd_or_nines)  # {0, 1, 3, 5, 7, 9, 11, 13, 15, 17, 18}
print(positive_only)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}