import random

adjectives = ["Really"]
noun = []
noun2 = []

def get(array):
    return array[random.randint(0, len(array))]

if __name__ == "__main__":
    print(get(adjectives) + " " + get(noun) + " " + get(noun2))
