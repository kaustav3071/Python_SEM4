def add_pair(dictionary, key, value):
    dictionary[key] = value

def update_pair(dictionary, key, value):
    if key in dictionary:
        dictionary[key] = value

def delete_pair(dictionary, key):
    if key in dictionary:
        del dictionary[key]

def merge_dictionaries(dict1, dict2):
    dict1.update(dict2)

def display_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

# Example usage
data = {"name": "Kaustav", "age": 19}

add_pair(data, "city", "Nadiad")
update_pair(data, "age", 20)
delete_pair(data, "name")

extra_data = {"country": "India", "profession": "Student"}
merge_dictionaries(data, extra_data)

display_dictionary(data)
