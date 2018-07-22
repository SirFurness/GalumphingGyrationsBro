import random

adjectives = ["Really",
              "Galumphing",
              "Totally",
              "Undoubtedly",
              "Radically",
              "Absolutely",
              "Utterly",
              "Stupendously",
              ]
noun = ["Awesome",
        "Gyrations",
        "Tubular",
        "Rad",]
noun2 = ["bud",
         "buddy",
         "bro",
         "lil yeetus",
         "broski",
         "fam",]

def get(array):
    return array[random.randint(0, len(array)-1)]

if __name__ == "__main__":
    adjective = get(adjectives)
    noun = get(noun)
    noun2 = get(noun2)
    print(adjective + " " + noun + " " + noun2)
