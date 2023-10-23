"""HSM_test.py
Reykjavík && Akureyri
"""

import unittest
from hsm import answer, city_distances


class TestCold(unittest.TestCase):
    def test_answer1(self) -> None:
        data = 'Reykjavik'
        ans = answer(city_distances, data)
        expected = "Reykjavík"
        self.assertEqual(ans, expected)

    def test_answer2(self) -> None:
        self.assertEqual(answer(city_distances, 'Kopavogur'), 'Reykjavík')

    def test_answer3(self) -> None:
        self.assertEqual(answer(city_distances, 'Akureyri'), 'Akureyri')

    def test_answer4(self) -> None:
        self.assertEqual(answer(city_distances, 'Mulaping'), 'Akureyri')

    def test_answer5(self) -> None:
        self.assertEqual(answer(city_distances, 'Arborg'), 'Reykjavík')

    def test_answer6(self) -> None:
        self.assertEqual(answer(city_distances, 'Fjardabyggd'), 'Akureyri')
