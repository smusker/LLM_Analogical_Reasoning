import random
import string
import sys
from enum import Enum
from typing import Callable

sys.path.insert(1, "../LLM_Analogical_Reasoning")

import Code.grounding_generation as gg
import Code.phase_2_domains as p2d

SEPARATOR = " => "
SYMBOL_SET = ["*", "!", "&", "^"]
FUNCS = [
    [gg.surround("[", "]"), gg.surround("(", ")")],
    [lambda g: "# " + g, lambda g: "$ " + g],
]


class AttributeType(Enum):
    NUMBER = 0
    CATEGORY = 1
    BOOLEAN_CATEGORY = 2


def attribute_type(attribute_name: str) -> AttributeType:
    """
    Takes an attribute name and returns the type of that attribute using the first character in conjunction with the marking scheme outlined within this function.
    """
    if attribute_name.startswith("#"):
        return AttributeType.NUMBER
    elif attribute_name.startswith("*"):
        return AttributeType.CATEGORY
    elif attribute_name.startswith("?"):
        return AttributeType.BOOLEAN_CATEGORY
    else:
        raise ValueError("Attribute doesn't begin with a recognized type character.")


def construct_grounding(
    attribute_vals: list[tuple[AttributeType, int]],
    default_num: int = 1,
) -> str:
    """
    Takes a list of pairs of attribute types and corresponding values and
    constructs a grounding using the values provided. If a number is not specified
    in attribute_vals, a default value (1) will be used (which can be modified with
    the optional parameters).
    """
    number = default_num
    categories = []

    for type, value in attribute_vals:
        if type == AttributeType.NUMBER:
            number = value
        elif type == AttributeType.CATEGORY:
            categories = [value] + categories
        elif type == AttributeType.BOOLEAN_CATEGORY:
            categories.append(value)

    if not categories:
        categories = [0]  # providing a default category for purely numeric groundings

    grounding = ""
    for i, c in enumerate(categories):
        if i == 0:
            grounding = " ".join([SYMBOL_SET[c]] * number)
        else:
            grounding = FUNCS[i - 1][c](grounding)
    return grounding


def generate_attribute_groundings(
    domain: dict[str, dict[str, int]],
    sample_size: int | None = None,
) -> list[tuple[str, str]]:
    """
    Generates a set of groundings for a given domain using their attributes.
    If sample_size is specified, a random sample of size sample_size will be
    selected to construct the groundings.
    """
    terms = list(domain.keys())
    attributes = list(domain[terms[0]].keys())
    detailed_attributes = [(attr, attribute_type(attr)) for attr in attributes]

    if sample_size:
        terms = random.sample(terms, sample_size)

    return [
        (
            term,
            construct_grounding(
                [(attr[1], domain[term][attr[0]]) for attr in detailed_attributes]
            ),
        )
        for term in terms
    ]


def arrange_attribute_groundings(
    pairs: list[tuple[str, str]],
    answer_unseen: bool = True,
    allow_repeats: bool = True,
) -> tuple[list[tuple[str, str]], str]:
    """
    Takes a list of term-grounding pairs from an attribute-based domain
    and produces up an order to be used for a task.
    If answer_unseen is set to True, the correct grounding for the queried term
    will not be included in the context. Otherwise, it is possible for another term
    with the same grounding as the queried term to be included.
    If allow_repeats is set to False, no groundings will be repeated in the context.
    Otherwise, multiple terms with the same grounding may be included.
    """
    randomized_pairs = random.sample(pairs, len(pairs))
    query, answer = randomized_pairs[0]
    output_pairs = []
    groundings_so_far = []
    for pair in randomized_pairs[1:]:
        if (answer_unseen and pair[1] == answer) or (
            not allow_repeats and pair[1] in groundings_so_far
        ):
            continue
        else:
            output_pairs.append(pair)
            groundings_so_far.append(pair[1])
    output_pairs.append((query, ""))
    return output_pairs, answer


def construct_relational_groundings(
    n: int,
    func: Callable[[str], str],
) -> list[tuple[str, str]]:
    """
    Generate groundings for a relational domain with n relational pairs of elements.
    func relates the groundings of related terms.
    """
    inputs = random.sample(list(string.ascii_uppercase), n)
    outputs = [func(x) for x in inputs]
    return list(zip(inputs, outputs))


def generate_relational_pairs(
    domain: list[tuple[str, str]], func: Callable[[str], str]
) -> list[tuple[str, str]]:
    """
    Generate pairs of terms and their corresponding groundings for terms
    in a domain with func relating groundings of related terms.
    """
    groundings = construct_relational_groundings(len(domain), func)
    return [
        (term, g)
        for terms, g_pair in zip(domain, groundings)
        for term, g in zip(terms, g_pair)
    ]


def arrange_relations(
    pairs: list[tuple[str, str]],
    preserve_intro: bool = False,
    only_candidates: bool = False,
) -> tuple[list[tuple[str, str]], str]:
    """
    Takes a list of term-grounding pairs from a relational domain and
    sets up an order to be used for a task.
    If preserve_intro is set to True, the one pair of related terms
    will be displayed in the first two lines. Otherwise, they will be
    randomly shuffled among the rest.
    If only_candidates is set to True, all terms other than the intro
    will be of the opposite "type" of the queried term, so their groundings
    will all be candidates for being mapped to the answer. Otherwise, the context
    beyond the intro will be randomly selected from both halves of the relational pairs.
    """
    pairs_of_pairs = [[pairs[i], pairs[i + 1]] for i in range(0, len(pairs), 2)]

    random.shuffle(pairs_of_pairs)  # randomize overall order
    random.shuffle(pairs_of_pairs[0])  # randomize order of intro

    index = random.choice([0, 1])
    key, query = pairs_of_pairs[1][index], pairs_of_pairs[1][1 - index]

    if preserve_intro:
        output_pairs = [key]
    else:
        output_pairs = [
            pairs_of_pairs[0][0],
            pairs_of_pairs[0][1],
            key,
        ]
    for pair_of_pairs in pairs_of_pairs[2:]:
        if only_candidates:
            output_pairs.append(pair_of_pairs[index])
        else:
            output_pairs.append(random.choice(pair_of_pairs))
    random.shuffle(output_pairs)

    if preserve_intro:
        output_pairs = [pairs_of_pairs[0][0], pairs_of_pairs[0][1]] + output_pairs
    output_pairs.append((query[0], ""))

    return output_pairs, query[1]


if __name__ == "__main__":
    print("-" * 30)
    for domain, answer_unseen, allow_repeats in zip(
        p2d.multi_attribute_domains[:4],
        [False, False, True, True],
        [False, True, False, True],
    ):
        tg_pairs, answer = arrange_attribute_groundings(
            generate_attribute_groundings(domain),
            answer_unseen=answer_unseen,
            allow_repeats=allow_repeats,
        )

        for t, g in tg_pairs:
            print(f"{t}{SEPARATOR}{g}")
        print("-" * 30)

    for domain, f, only_candidates in zip(
        p2d.relational_domains[:2],
        [gg.reduplicate, gg.surround("[", "]")],
        [True, False],
    ):
        tg_pairs, answer = arrange_relations(
            generate_relational_pairs(domain, f),
            preserve_intro=False,
            only_candidates=only_candidates,
        )

        for t, g in tg_pairs:
            print(f"{t}{SEPARATOR}{g}")
        print("-" * 30)
