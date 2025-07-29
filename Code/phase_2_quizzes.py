import os
import random
import sys
from typing import Callable

sys.path.insert(1, "../LLM_Analogical_Reasoning")

import Code.grounding_generation as gg
import Code.phase_2_grounding as grounding
from Code.phase_2_refined import (
    categorial_attribute_domains,
    multi_attribute_domains,
    numeric_attribute_domains,
    numeric_multi_attribute_domains,
    relational_domains,
)
from Code.quiz_generation import write_list_to_csv

study_path = "quiz_files/phase_2/"

quizzes_per_category = 2

domains_list = [
    ("numeric_multi_attribute", numeric_multi_attribute_domains),
    ("multi_attribute", multi_attribute_domains),
    ("categorial", categorial_attribute_domains),
    ("numeric", numeric_attribute_domains),
    ("relational", relational_domains),
]

relational_funcs = [
    gg.surround("[", "]"),
    gg.change_count(2),
    lambda s: ". . " + s + " .",
    lambda s: "% " + s,
    lambda s: s + " # " + s,
    lambda s: s + " ; ;",
]


def generate_attribute_question(
    domain: dict[str, dict[str, int]], **kwargs
) -> tuple[str, str]:
    """Given an attribute-based domain, generates a question and answer."""

    question = ""
    tg_pairs, answer = grounding.arrange_attribute_groundings(
        grounding.generate_attribute_groundings(domain), **kwargs
    )

    for t, g in tg_pairs:
        question += f"{t}{grounding.SEPARATOR}{g}\n"
    return question[:-1], answer


def generate_relational_question(
    domain: list[tuple[str, str]], func: Callable[[str], str], **kwargs
) -> tuple[str, str]:
    """Given a relational domain, generates a question and answer."""

    question = ""
    tg_pairs, answer = grounding.arrange_relations(
        grounding.generate_relational_pairs(domain, func), **kwargs
    )
    for t, g in tg_pairs:
        question += f"{t}{grounding.SEPARATOR}{g}\n"
    return question, answer


for name, domains in domains_list:
    for i in range(quizzes_per_category):
        if name == "relational":
            questions, answers = list(
                zip(
                    *[
                        generate_relational_question(domain, func)
                        for domain, func in zip(
                            random.sample(domains, len(domains)),
                            random.sample(relational_funcs, len(relational_funcs)),
                        )
                    ]
                )
            )
        elif name == "categorial":
            questions, answers = list(
                zip(
                    *[
                        generate_attribute_question(domain, answer_unseen=False)
                        for domain in random.sample(domains, len(domains))
                    ]
                )
            )
        else:
            questions, answers = list(
                zip(
                    *[
                        generate_attribute_question(domain)
                        for domain in random.sample(domains, len(domains))
                    ]
                )
            )

        quiz_path = f"{study_path}{name}/{name}{i+1}/"
        os.makedirs(quiz_path)
        write_list_to_csv(list(questions), f"{quiz_path}{name}{i+1}questions.csv")
        write_list_to_csv(list(answers), f"{quiz_path}{name}{i+1}answers.csv")
