import random

adjectives = ["Really",
              "Galumphingly",
              "Totally",
              "Undoubtedly",
              "Radically",
              "Absolutely",
              "Utterly",
              "Stupendously",
              "Extremely",
              "Uncomfortably",
              "Awfully",
              "Insanely",
              ]
noun = ["Awesome",
        "Gyrations",
        "Tubular",
        "Rad",
        "Remorseful",
        "Litty",
        "Interesting",
        "Funky",
        "Wild",
        "Organic",
        "Poppin",
        "Ridiculous",
        "Insane",
        "Extreme",
        ]
noun2 = ["bud",
         "buddy",
         "bro",
         "lil yeetus",
         "broski",
         "fam",
         "boi",
         "thiccy",
         "squadfam",
         "brother",
         "litfam",
         "budboy",
         "amigo",
         "brethren",
         "m'lord",
         "sire",
         ]

def get(array):
    return array[random.randint(0, len(array)-1)]

if __name__ == "__main__":
    adjective = get(adjectives)
    noun = get(noun)
    noun2 = get(noun2)
    print(adjective + " " + noun + " " + noun2)
