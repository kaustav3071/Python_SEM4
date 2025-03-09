# 1. Remove duplicates from tuple
def remove_duplicates(tup):
    return tuple(dict.fromkeys(tup))

# 2. Sort list of student tuples by marks
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])

# 3. Count frequency using Counter
from collections import Counter
def count_frequency(tup):
    return Counter(tup)

records = [(1, "Alice", 85), (2, "Bob", 92), (3, "Charlie", 78)]
def search_record(records, search_id):
    for record in records:
        if record[0] == search_id:
            return record


print(remove_duplicates((1, 2, 2, 3, 3, 3)))  # (1, 2, 3)
print(sorted_students)  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]
print(count_frequency((1, 2, 2, 3, 3, 3)))  # Counter({3: 3, 2: 2, 1: 1})
print(search_record(records, 2))  # (2, 'Bob', 92)