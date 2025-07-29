from typing import TypeAlias

AttributeDomain: TypeAlias = dict[str, dict[str, int | bool]]
RelationalDomain: TypeAlias = list[tuple[str, str]]

# *
# * Relation-Based
# *
relational_domains: list[RelationalDomain] = [
    # animal_youths
    [
        ("dog", "puppy"),
        ("cat", "kitten"),
        ("cow", "calf"),
        ("chicken", "chick"),
        ("pig", "piglet"),
    ],
    # coverings
    [
        ("hand", "glove"),
        ("head", "hat"),
        ("foot", "sock"),
        ("legs", "pants"),
        ("torso", "shirt"),
    ],
    # exact_opposites
    [
        ("yes", "no"),
        ("up", "down"),
        ("left", "right"),
        ("north", "south"),
        ("east", "west"),
    ],
    [
        ("hammer", "nail"),
        ("screwdriver", "screw"),
        ("wrench", "nut"),
        ("axe", "tree"),
        ("rake", "leaf"),
    ],
    # animal_adjectives
    # [
    #     ("dog", "canine"),
    #     ("cat", "feline"),
    #     ("cow", "bovine"),
    #     ("horse", "equine"),
    #     ("bird", "avian"),
    # ],
    # tool_applications
    # food_addition_pairs
    # [
    #     ("salt", "pepper"),
    #     ("ketchup", "mustard"),
    #     ("cream", "sugar"),
    #     ("fish", "chips"),
    #     ("peanut butter", "jelly"),
    # ],
]

# *
# * Multi-Attribute
# *
multi_attribute_domains: list[AttributeDomain] = [
    # general_shapes
    {
        "triangle": {"#dimensions": 2, "?has_curves": False},
        "square": {"#dimensions": 2, "?has_curves": False},
        "pentagon": {"#dimensions": 2, "?has_curves": False},
        "circle": {"#dimensions": 2, "?has_curves": True},
        "semicircle": {"#dimensions": 2, "?has_curves": True},
        "pyramid": {"#dimensions": 3, "?has_curves": False},
        "cube": {"#dimensions": 3, "?has_curves": False},
        "sphere": {"#dimensions": 3, "?has_curves": True},
        "cone": {"#dimensions": 3, "?has_curves": True},
    },
    # sight_and_sound
    {
        "eye": {"*modality": 0, "?produces": False},
        "camera": {"*modality": 0, "?produces": False},
        "projector": {"*modality": 0, "?produces": True},
        "screen": {"*modality": 0, "?produces": True},
        "ear": {"*modality": 1, "?produces": False},
        "microphone": {"*modality": 1, "?produces": False},
        "speaker": {"*modality": 1, "?produces": True},
        "headphones": {"*modality": 1, "?produces": True},
        "radio": {"*modality": 1, "?produces": True},
    },
    # games
    {
        "marathon": {"?indoors": False, "?teams": False},
        "tag": {"?indoors": False, "?teams": False},
        "golf": {"?indoors": False, "?teams": False},
        "skiing": {"?indoors": False, "?teams": False},
        "soccer": {"?indoors": False, "?teams": True},
        "football": {"?indoors": False, "?teams": True},
        "baseball": {"?indoors": False, "?teams": True},
        "poker": {"?indoors": True, "?teams": False},
        "chess": {"?indoors": True, "?teams": False},
        "boxing": {"?indoors": True, "?teams": False},
        "wrestling": {"?indoors": True, "?teams": False},
        "basketball": {"?indoors": True, "?teams": True},
        "hockey": {"?indoors": True, "?teams": True},
    },
    # family
    {
        "grandmother": {"#generation": 1, "*gender": 0},
        "grandfather": {"#generation": 1, "*gender": 1},
        "mother": {"#generation": 2, "*gender": 0},
        "father": {"#generation": 2, "*gender": 1},
        "sister": {"#generation": 3, "*gender": 0},
        "brother": {"#generation": 3, "*gender": 1},
    },
]

# *
# * Numeric Multi-Attribute
# *
numeric_multi_attribute_domains: list[AttributeDomain] = [
    # animals
    {
        "human": {"#legs": 2, "?eggs": False},
        "cat": {"#legs": 4, "?eggs": False},
        "dog": {"#legs": 4, "?eggs": False},
        "horse": {"#legs": 4, "?eggs": False},
        "chicken": {"#legs": 2, "?eggs": True},
        "ant": {"#legs": 6, "?eggs": True},
        "bee": {"#legs": 6, "?eggs": True},
        "spider": {"#legs": 8, "?eggs": True},
    },
    # vehicles
    {
        "unicycle": {"#wheels": 1, "?manually_powered": True},
        "bicycle": {"#wheels": 2, "?manually_powered": True},
        "motorcycle": {"#wheels": 2, "?manually_powered": False},
        "tricycle": {"#wheels": 3, "?manually_powered": True},
        "skateboard": {"#wheels": 4, "?manually_powered": True},
        "car": {"#wheels": 4, "?manually_powered": False},
    },
    # number of holes
    {
        "pants": {"#holes": 3, "?wearable": True},
        "t-shirt": {"#holes": 4, "?wearable": True},
        "headband": {"#holes": 1, "?wearable": True},  # context only
        "donut": {"#holes": 1, "?wearable": False},
        "power outlet": {"#holes": 3, "?wearable": False},  # context only
    },
    # units
    {
        "dime": {"#number": 10, "*category": 0},
        "quarter": {"#number": 4, "*category": 0},
        "dollar": {"#number": 1, "*category": 0},
        "day": {"#number": 7, "*category": 1},
        "week": {"#number": 1, "*category": 1},
        "inches": {"#number": 12, "*category": 2},
        "feet": {"#number": 1, "*category": 2},
    },
]

# *
# *  Numeric Attribute
# *
numeric_attribute_domains = [
    {
        term: {attr: domain[term][attr]}
        for term in domain.keys()
        for attr in domain[term].keys()
        if attr[0] == "#"
    }
    for domain in numeric_multi_attribute_domains
]

# *
# *  Categorial Attribute
# *
categorial_attribute_domains = [
    {
        term: {attr: domain[term][attr]}
        for term in domain.keys()
        for attr in domain[term].keys()
        if attr[0] in ["*", "?"]
    }
    for domain in numeric_multi_attribute_domains
]
