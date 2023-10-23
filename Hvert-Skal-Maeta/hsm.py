"""Kattis Hvert-Skal-Maeta problem.
"""

from typing import Dict, Optional

__author__ = "Grant Nagy"
__date__ = "Oct 23, 2023"

# Define a dictionary to store city names and their distances to contest sites
city_distances = {
    "Reykjavik": {"Reykjavík": 0, "Akureyri": 388},
    "Kopavogur": {"Reykjavík": 6, "Akureyri": 387},
    "Hafnarfjorour": {"Reykjavík": 12, "Akureyri": 391},
    "Reykjanesbaer": {"Reykjavík": 49, "Akureyri": 427},
    "Akureyri": {"Reykjavík": 388, "Akureyri": 0},
    "Gardabaer": {"Reykjavík": 9, "Akureyri": 389},
    "Mosfellsbaer": {"Reykjavík": 16, "Akureyri": 371},
    "Arborg": {"Reykjavík": 42, "Akureyri": 428},
    "Akranes": {"Reykjavík": 42, "Akureyri": 428},
    "Fjardabyggd": {"Reykjavík": 659, "Akureyri": 290},
    "Mulaping": {"Reykjavík": 603, "Akureyri": 216},
    "Seltjarnarnes": {"Reykjavík": 4, "Akureyri": 390}
}


def answer(
    city_distances: Dict[str, Dict[str, int]],
    city_name: str
) -> Optional[str]:
    distance_to_reykjavik = city_distances[city_name]["Reykjavík"]
    distance_to_akureyri = city_distances[city_name]["Akureyri"]
    if distance_to_reykjavik < distance_to_akureyri:
        solution = "Reykjavík"
    elif distance_to_akureyri < distance_to_reykjavik:
        solution = "Akureyri"
    return solution


def solve() -> None:
    """_summary_
    """
    _ = input()
    data = input()
    print(answer(city_distances, data))
