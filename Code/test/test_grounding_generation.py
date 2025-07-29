import sys
import unittest

sys.path.insert(1, "../LLM_Analogical_Reasoning")

from Code.grounding_generation import *


class TestGroundingTransformations(unittest.TestCase):
    def test_lower_case(self):
        self.assertEqual(lower_case("A B C"), "a b c")
        self.assertEqual(lower_case("X"), "x")
        with self.assertRaises(Exception):
            lower_case("1 2 3")
        with self.assertRaises(Exception):
            lower_case("a b c")

    def test_remove_first(self):
        self.assertEqual(remove_first("a b c"), "b c")
        self.assertEqual(remove_first("F F F"), "F F")
        with self.assertRaises(Exception):
            remove_first("X")

    def test_remove_last(self):
        self.assertEqual(remove_last("a b c"), "a b")
        self.assertEqual(remove_last("F F F"), "F F")
        with self.assertRaises(Exception):
            remove_last("X")

    def test_rotate(self):
        self.assertEqual(rotate("A B C"), "B C A")
        self.assertEqual(rotate("x y"), "y x")
        self.assertEqual(rotate("1 2 3 4"), "2 3 4 1")
        with self.assertRaises(Exception):
            rotate("X")

    def test_reduplicate(self):
        self.assertEqual(reduplicate("z"), "z z")
        self.assertEqual(reduplicate("A B"), "A B A B")
        self.assertEqual(reduplicate("0 0 0"), "0 0 0 0 0 0")

    def test_fine_grained_duplication(self):
        self.assertEqual(fine_grained_duplication("z"), "z z")
        self.assertEqual(fine_grained_duplication("A B"), "A A B B")
        self.assertEqual(fine_grained_duplication("4 5 6"), "4 4 5 5 6 6")

    def test_reverse(self):
        self.assertEqual(reverse("1 2"), "2 1")
        self.assertEqual(reverse("a b c"), "c b a")
        with self.assertRaises(Exception):
            reverse("x")
        with self.assertRaises(Exception):
            reverse("x a x")

    def test_extract_center(self):
        self.assertEqual(extract_center("x a x"), "a")
        self.assertEqual(extract_center("A B C D E"), "C")
        with self.assertRaises(Exception):
            extract_center("X")
        with self.assertRaises(Exception):
            extract_center("A B")
        with self.assertRaises(Exception):
            extract_center("A B B A")

    def test_replace(self):
        replacer1 = replace("A", "B")
        self.assertEqual(replacer1("A"), "B")
        self.assertEqual(replacer1("A A A"), "B B B")
        self.assertEqual(replacer1("X A X"), "X B X")
        replacer2 = replace("X X", "Y")
        self.assertEqual(replacer2("X X"), "Y")
        self.assertEqual(replacer2("X X X"), "Y X")
        self.assertEqual(replacer2("X X X X"), "Y Y")
        with self.assertRaises(ValueError):
            replacer1("X Y")
        with self.assertRaises(Exception):
            replacer2("Y")

    def test_change_count(self):
        count_changer1 = change_count(2)
        self.assertEqual(count_changer1("X"), "X X X")
        self.assertEqual(count_changer1("T T"), "T T T T")
        count_changer2 = change_count(-1)
        self.assertEqual(count_changer2("# #"), "#")
        self.assertEqual(count_changer2("4 4 4 4"), "4 4 4")
        self.assertEqual(count_changer1("a"), "a a a")
        with self.assertRaises(ValueError):
            count_changer1("X Y")
        with self.assertRaises(Exception):
            count_changer2("1")

    def test_is_valid_grounding(self):
        self.assertTrue(is_valid_grounding("A"))
        self.assertTrue(is_valid_grounding("1 2 3"))
        self.assertTrue(is_valid_grounding("x X x"))
        self.assertTrue(is_valid_grounding("t t 5 t t t"))
        self.assertTrue(is_valid_grounding("G H"))

        self.assertFalse(is_valid_grounding("A "))
        self.assertFalse(is_valid_grounding("789"))
        self.assertFalse(is_valid_grounding("test"))
        self.assertFalse(is_valid_grounding("x X Xx"))
        self.assertFalse(is_valid_grounding(""))

    def test_generate_groundings(self):
        output = generate_groundings("X", lower_case, reduplicate)
        expected = np.array([["X", "x"], ["X X", "x x"]])
        for pair in zip(output.flatten(), expected.flatten()):
            self.assertEqual(pair[0], pair[1])

        output = generate_groundings("C C C", lower_case, remove_last)
        expected = np.array([["C C C", "c c c"], ["C C", "c c"]])
        for pair in zip(output.flatten(), expected.flatten()):
            self.assertEqual(pair[0], pair[1])

        output = generate_groundings("A B C", lower_case, rotate)
        expected = np.array([["A B C", "a b c"], ["B C A", "b c a"]])
        for pair in zip(output.flatten(), expected.flatten()):
            self.assertEqual(pair[0], pair[1])

        with self.assertRaises(RuntimeError):
            generate_groundings("A B C", reverse, remove_last)
        with self.assertRaises(Exception):
            generate_groundings("X X X", lower_case, lower_case)
        with self.assertRaises(RuntimeError):
            generate_groundings("A B", reverse, rotate)


if __name__ == "__main__":
    unittest.main()
