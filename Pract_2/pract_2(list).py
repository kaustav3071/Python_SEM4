# 1. Generate prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_numbers(start, end):
    result = []
    for i in range(start, end+1):
        if is_prime(i):
            result.append(i)
    return result


# 2. Flatten nested list
def flatten_list(nested):
    flat = []
    for item in nested:
        if isinstance(item, list):
            flat.extend(flatten_list(item))
        else:
            flat.append(item)
    return flat


# 3. Second largest element
def second_largest(lst):
    if len(lst) < 2:
        return None
    largest = second = float('-inf')
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second


# 4. Task queue
class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self):
        if len(self.tasks) == 0:
            return None
        else:
            return self.tasks.pop(0)

    def process_next(self):
        return self.remove_task()


print(prime_numbers(1, 10))  # [2, 3, 5, 7]
print(flatten_list([1, [2, 3], [4, [5, 6]]]))  # [1, 2, 3, 4, 5, 6]
print(second_largest([1, 5, 2, 8, 3]))  # 5
queue = TaskQueue()
queue.add_task("Task1")
queue.add_task("Task2")
print(queue.process_next())  # Task1