from typing import TypeAlias

AttributeDomain: TypeAlias = dict[str, dict[str, int | bool]]
RelationalDomain: TypeAlias = list[tuple[str, str]]

# *
# * Characteristic Attribute
# *
# These domains are meant to be straightforward, fundamental tests of conceptual understanding.
# The attributes of each concept are meant to be information that it is impossible or extremely unlikely
# for someone to not understand while understanding the actual concept. For instance, knowing what a triangle
# is practically requires that one know a triange has three sides.

characteristic_domains: list[AttributeDomain] = [
    # number_words
    {
        "one": {"#number": 1},
        "two": {"#number": 2},
        "three": {"#number": 3},
        "four": {"#number": 4},
        "five": {"#number": 5},
        "six": {"#number": 6},
        "seven": {"#number": 7},
        "eight": {"#number": 8},
    },
    # shape_sides
    {
        "triangle": {"#num_sides": 3},
        "square": {"#num_sides": 4},
        "rectangle": {"#num_sides": 4},
        "trapezoid": {"#num_sides": 4},
        "parallelogram": {"#num_sides": 4},
        "pentagon": {"#num_sides": 5},
        "hexagon": {"#num_sides": 6},
        "octagon": {"#num_sides": 8},
    },
    # ! units
    {
        "inch": {"*type": 0},
        "foot": {"*type": 0},
        "yard": {"*type": 0},
        "mile": {"*type": 0},
        "cup": {"*type": 1},
        "pint": {"*type": 1},
        "quart": {"*type": 1},
        "gallon": {"*type": 1},
        "second": {"*type": 2},
        "minute": {"*type": 2},
        "hour": {"*type": 2},
        "day": {"*type": 2},
        "week": {"*type": 2},
        "month": {"*type": 2},
    },
    # ! states_of_matter
    {
        "ice": {"*state": 0},
        "wood": {"*state": 0},
        "stone": {"*state": 0},
        "water": {"*state": 1},
        "milk": {"*state": 1},
        "oil": {"*state": 1},
        "steam": {"*state": 2},
        "air": {"*state": 2},
        "smoke": {"*state": 2},
    },
    # ! animal_products
    {
        "honey": {"?meat": False},
        "egg": {"?meat": False},
        "cheese": {"?meat": False},
        "steak": {"?meat": True},
        "ham": {"?meat": True},
        "salami": {"?meat": True},
    },
    # ! animal_environment
    {
        "eagle": {"?sealife": False},
        "dog": {"?sealife": False},
        "human": {"?sealife": False},
        "rat": {"?sealife": False},
        "octopus": {"?sealife": True},
        "whale": {"?sealife": True},
        "shark": {"?sealife": True},
        "jellyfish": {"?sealife": True},
    },
]

# *
# *  Non-Characteristic Attribute
# *
# The attributes in these domains are less direct than those above (hence "Non-Characteristic"),
# and are not analytically necessary for understanding the terms/concepts, but they are still likely
# to be familiar/known by a human who is aware of the concepts. For instance, one doesn't need to
# have an explicit count of the number of wheels on a car in order to have an understanding or even
# a mental image of a car. These attributes can thus be seen as almost "emergent" in that they aren't
# definitional but are strongly tied to their respective terms/concepts.

non_characteristic_domains: list[AttributeDomain] = [
    # ! animals_simple
    {
        "human": {"?eggs": False},
        "cat": {"?eggs": False},
        "dog": {"?eggs": False},
        "horse": {"?eggs": False},
        "chicken": {"?eggs": True},
        "ant": {"?eggs": True},
        "spider": {"?eggs": True},
    },
    # vehicles_simple
    {
        "unicycle": {"#wheels": 1},
        "bicycle": {"#wheels": 2},
        "motorcycle": {"#wheels": 2},
        "tricycle": {"#wheels": 3},
        "skateboard": {"#wheels": 4},
        "car": {"#wheels": 4},
    },
    # ! general_shapes_simple
    {
        "triangle": {"#dimensions": 2},
        "square": {"#dimensions": 2},
        "pentagon": {"#dimensions": 2},
        "circle": {"#dimensions": 2},
        "semicircle": {"#dimensions": 2},
        "pyramid": {"#dimensions": 3},
        "cube": {"#dimensions": 3},
        "sphere": {"#dimensions": 3},
        "cone": {"#dimensions": 3},
    },
    # ! sight_and_sound_simple
    {
        "eye": {"*modality": 0},
        "camera": {"*modality": 0},
        "projector": {"*modality": 0},
        "screen": {"*modality": 0},
        "ear": {"*modality": 1},
        "microphone": {"*modality": 1},
        "speaker": {"*modality": 1},
        "headphones": {"*modality": 1},
        "radio": {"*modality": 1},
    },
    # ! games_simple
    {
        "marathon": {"?teams": False},
        "tag": {"?teams": False},
        "golf": {"?teams": False},
        "skiing": {"?teams": False},
        "soccer": {"?teams": True},
        "football": {"?teams": True},
        "baseball": {"?teams": True},
        "poker": {"?teams": False},
        "chess": {"?teams": False},
        "boxing": {"?teams": False},
        "wrestling": {"?teams": False},
        "basketball": {"?teams": True},
        "hockey": {"?teams": True},
    },
]

# *
# * Multi-Attribute
# *
# These domains are extensions of the Non-Characteristic set above. By adding a second
# attribute/dimension, we make tasks involving these domains more difficult than the
# previous two, potentially revealing a level of complexity that one type of participant
# can handle but the other cannot. Additionally, the complexity added here is a *compositional*
# component, as one must tease apart the influence of the two factors to understand how to
# combine them when constructing the grounding of the queried term. Thus, this is also a test for
# compositional understanding within an analogical reasoning paradigm.

multi_attribute_domains: list[AttributeDomain] = [
    # animals_complex
    {
        "human": {"#legs": 2, "?eggs": False},
        "cat": {"#legs": 4, "?eggs": False},
        "dog": {"#legs": 4, "?eggs": False},
        "horse": {"#legs": 4, "?eggs": False},
        "chicken": {"#legs": 2, "?eggs": True},
        "ant": {"#legs": 6, "?eggs": True},
        "spider": {"#legs": 8, "?eggs": True},
    },
    # vehicles_complex
    {
        "unicycle": {"#wheels": 1, "?is_gaspowered": False},
        "bicycle": {"#wheels": 2, "?is_gaspowered": False},
        "motorcycle": {"#wheels": 2, "?is_gaspowered": True},
        "tricycle": {"#wheels": 3, "?is_gaspowered": False},
        "skateboard": {"#wheels": 4, "?is_gaspowered": False},
        "car": {"#wheels": 4, "?is_gaspowered": True},
    },
    # ! general_shapes_complex
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
    # ! sight_and_sound_complex
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
    # ! games_complex
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
]

# *
# * Relation-Based
# *
# These domains bear the most resemblance to Phase 1 domains out of all of Phase 2.
# Each domain is composed of a list of relational pairs, where each pair is an instance
# of the same relation. By extending these lists to be more than just two pairs,
# we remove the possibility of simply relying on the RHS, as the only consistent
# structure relating groundings to one another will be between the related pairs.
# Terms from separate pairs will be given groundings with no relation to one another (the
# only constraint will be that different random letters will be used). This condition
# provides a bridge between the two phases, as it makes minimal changes to Phase 1's
# design in order to test whether respondents/models are relying only on the RHS or
# using semantic information, whereas the other conditions in Phase 2 make more fundamental
# changes to the structure/nature of the task.

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
    # animal_adjectives
    [
        ("dog", "canine"),
        ("cat", "feline"),
        ("cow", "bovine"),
        ("horse", "equine"),
        ("bird", "avian"),
    ],
    # tool_applications
    [
        ("hammer", "nail"),
        ("screwdriver", "screw"),
        ("wrench", "nut"),
        ("axe", "tree"),
        ("rake", "leaf"),
    ],
    # food_addition_pairs
    [
        ("salt", "pepper"),
        ("ketchup", "mustard"),
        ("cream", "sugar"),
        ("fish", "chips"),
        ("peanut butter", "jelly"),
    ],
]
