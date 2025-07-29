import sys
import unittest

sys.path.insert(1, "../LLM_Analogical_Reasoning")

from Code.grading_stats import grade_charitably, is_correct, is_scrambled


class TestGrading(unittest.TestCase):
    def test_correct(self):
        self.assertTrue(is_correct("A B C", "A B C"))
        self.assertTrue(is_correct("ABC", "A B C"))
        self.assertTrue(is_correct("", ""))
        self.assertTrue(is_correct("\n", "\n\n"))
        self.assertTrue(is_correct("\n \n", ""))
        self.assertTrue(is_correct(" A  B  C ", "A B C"))
        self.assertTrue(is_correct("\n\n A  B  C \n", "A B C"))
        self.assertTrue(is_correct(" AB\t C", "A B C"))
        self.assertTrue(is_correct("A B C\n\n This is just a guess.", "A B C"))

    def test_incorrect(self):
        self.assertFalse(is_correct("A B ", "A B C"))
        self.assertFalse(is_correct("a b c", "A B C"))
        self.assertFalse(is_correct("B A C", "A B C"))
        self.assertFalse(is_correct("A B C D", "A B C"))
        self.assertFalse(is_correct("\nA  D  B C\n", "A B C"))
        self.assertFalse(is_correct(" AB\n  C\t", "A B C"))
        self.assertFalse(is_correct("", "A B C"))

    def test_scrambled(self):
        self.assertTrue(is_scrambled("A B C", "A B C"))
        self.assertTrue(is_scrambled("A C B", "A B C"))
        self.assertTrue(is_scrambled("B A C", "A B C"))
        self.assertTrue(is_scrambled("BAC", "A B C"))

    def test_not_scrambled(self):
        self.assertFalse(is_scrambled("A B", "A B C"))
        self.assertFalse(is_scrambled("A B B", "A B C"))
        self.assertFalse(is_scrambled("A B B C", "A B C"))
        self.assertFalse(is_scrambled("a b c", "A B C"))

    def test_charitably_correct(self):
        self.assertTrue(grade_charitably("Q Z I", "Q Z I", []))
        self.assertTrue(grade_charitably("Q Z I", "Q Z I", [("I", "|")]))
        self.assertTrue(grade_charitably("Q Z |", "Q Z I", [("I", "|")]))
        self.assertTrue(grade_charitably("Q Z |", "Q Z I", [("|", "I")]))
        self.assertTrue(grade_charitably("Q Z L", "Q Z I", [("|", "I"), ("L", "I")]))
        self.assertTrue(grade_charitably("Q Z |", "Q Z I", [("|", "I"), ("L", "I")]))
        self.assertTrue(grade_charitably("I | I", "I I I", [("|", "I")]))
        self.assertTrue(grade_charitably("I | I", "| | |", [("|", "I")]))
        self.assertTrue(grade_charitably("q z i", "Q Z I", [], case_sensitive=False))
        self.assertTrue(grade_charitably("Q z i", "Q Z I", [], case_sensitive=False))
        self.assertTrue(grade_charitably("q Z i", "Q z i", [], case_sensitive=False))

    def test_charitably_incorrect(self):
        self.assertFalse(grade_charitably("Q Z X", "Q Z I", [("|", "I")]))
        self.assertFalse(grade_charitably("Q Z I I", "Q Z I", [("|", "I")]))
        self.assertFalse(grade_charitably("Q Z", "Q Z I", [("|", "I")]))
        self.assertFalse(grade_charitably("I I I I", "| | |", [("|", "I")]))
        self.assertFalse(
            grade_charitably("Q Z X", "Q Z I", [("|", "I")], case_sensitive=False)
        )
        self.assertFalse(grade_charitably("Z Q I", "Q Z I", [], case_sensitive=False))


if __name__ == "__main__":
    unittest.main()
