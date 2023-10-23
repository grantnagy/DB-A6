import unittest
from hsm import ans, city_distances


class TestCold(unittest.TestCase):
    def test_answer1(self) -> None:
        self.assertEqual(
            ans('Reykjavik', city_distances),
            'Reykjavik'
        )

    def test_answer2(self) -> None:
        self.assertEqual(
            ans('Kopavogur', city_distances),
            'Reykjavik'
        )

    def test_answer3(self) -> None:
        self.assertEqual(
            ans('Akureyri', city_distances),
            'Akureyri'
        )

    def test_answer4(self) -> None:
        self.assertEqual(
            ans('Mulathing', city_distances),
            'Akureyri'
        )

    def test_answer5(self) -> None:
        self.assertEqual(
            ans('Arborg', city_distances),
            'Reykjavik'
        )

    def test_answer6(self) -> None:
        self.assertEqual(
            ans('Fjardabyggd', city_distances),
            'Akureyri'
        )


if __name__ == '__main':
    unittest.main()
