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
              "Incredibly",
              "Ridiculously",
              "Like, Totally",
              "Like, Really",
              "Like, Utterly",
              
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
        "Saucy",
        "Thicc",
        "Juicy",
        "Radical",
        "Gnarly",
        "Grody",
        "Trippin'",
        "Mental",
        "Bodacious",
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
         "dude",
         "dude bro",
         "chum",
         "friendo",
         "buddy boy",
         ]

def get(array):
    return array[random.randint(0, len(array)-1)]

if __name__ == "__main__":
    adjective = get(adjectives)
    noun = get(noun)
    noun2 = get(noun2)
    print(adjective + " " + noun + " " + noun2)
