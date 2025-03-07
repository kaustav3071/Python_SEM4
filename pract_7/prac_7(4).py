import random as r

with open("basic.txt","r") as file:
    content = file.read().split()
    words = r.sample(content,5)
    print("The random 5 words are:")
    for word in words:
        print(word)

