import random

part1 = ["Really",
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
part2 = ["Awesome",
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
part3 = ["bud",
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
    part1 = get(part1)
    part2 = get(part2)
    part3 = get(part3)
    print(part1 + " " + part2 + " " + part3)
