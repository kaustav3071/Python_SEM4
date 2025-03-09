# 1. Word frequency
def word_frequency(text):
    words = text.lower().split()
    return {word: words.count(word) for word in set(words)}


# 2. Phonebook
class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def delete_contact(self, name):
        self.contacts.pop(name, None)

    def search_contact(self, name):
        return self.contacts.get(name)


# 3. Filter students by grade
def filter_students(students, threshold):
    return {name: grade for name, grade in students.items() if grade > threshold}


# 4. Tuple list to dictionary and back
def tuples_to_dict(tuple_list):
    return dict(tuple_list)


def dict_to_tuples(dictionary):
    return list(dictionary.items())


# Example usage
print(word_frequency("the quick brown fox the fox"))
phonebook = PhoneBook()
phonebook.add_contact("Alice", "123-456")
print(phonebook.search_contact("Alice"))  # 123-456
students = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(filter_students(students, 80))  # {'Alice': 85, 'Bob': 92}
tuple_list = [("a", 1), ("b", 2)]
print(tuples_to_dict(tuple_list))  # {'a': 1, 'b': 2}