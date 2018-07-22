import random

adjectives = ["Really",
              "Galumphing",
              "Totally",
              "Undoubtedly",
              "Radically",
              "Absolutely",
              "Utterly",
              ]
noun = ["Awesome",
        "Gyrations",
        "Tubular",
        "Rad",]
noun2 = []

def get(array):
    return array[random.randint(0, len(array))]

if __name__ == "__main__":
    adjective = get(adjectives)
    noun = get(noun)
    noun2 = get(noun2)
    print(adjective + " " + noun + " " + noun2)
