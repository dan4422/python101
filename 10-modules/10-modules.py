def print_pokemon(poke):
    print(f"""
    Pokemon {poke["number"]}: {poke["name"]}
    Type/s: {poke["types"]}
    {poke["blurb"]}
    """)

# pokemon = [
#     {
#         "name": "bulbasaur",
#         "number": "001",
#         "types": ["grass","poison"],
#         "gender": "f",
#         "evolves_to": "TBD",
#         "blurb": "bulb lookin dude",
#         "height": 7,
#         "weight": 69,
#         "evolution_level": 16,
#         "evolves_to": ["ivysaur"],
#     },
#     {
#         "name": "eevee",
#         "number": "070",
#         "types": ["normal"],
#         "gender": "f",
#         "evolves_to": "TBD",
#         "blurb": "fox lookin thing",
#         "height": 7,
#         "weight": 69,
#         "evolution_level": 16,
#         "evolves_to": ["vaporeon","flareon","jolteon"]
#     },
# # ]

# print_pokemon(pokemon[1])
def print_breed(dog):
    print(f"""
    Dog breed is {dog["breed"]}
    Size: {dog["size"]}
    {dog["hobbies"]}
    """)

dog_breed = [
    {
        "breed": "chihuahua",
        "size": "small",
        "gender": ["male", "female"],
        "hobbies": "being crazy",
    },
    {
        "breed": "australian shepard",
        "size": "average",
        "gender": ["male", "female"],
        "hobbies": "energetic",
    },
    {
        "breed": "shiba inu",
        "size": "small",
        "gender": ["male", "female"],
        "hobbies": "going to the moon",
    },
]

print_breed(dog_breed[2])

