from typing import Dict

city_distances: Dict[str, Dict[str, int]] = {
    "Reykjavik": {"Reykjavik": 0, "Akureyri": 388},
    "Kopavogur": {"Reykjavik": 6, "Akureyri": 387},
    "Hafnarfjordur": {"Reykjavik": 12, "Akureyri": 391},
    "Reykjanesbaer": {"Reykjavik": 49, "Akureyri": 427},
    "Akureyri": {"Reykjavik": 388, "Akureyri": 0},
    "Gardabaer": {"Reykjavik": 9, "Akureyri": 389},
    "Mosfellsbaer": {"Reykjavik": 16, "Akureyri": 371},
    "Arborg": {"Reykjavik": 42, "Akureyri": 428},
    "Akranes": {"Reykjavik": 42, "Akureyri": 428},
    "Fjardabyggd": {"Reykjavik": 659, "Akureyri": 290},
    "Mulathing": {"Reykjavik": 603, "Akureyri": 216},
    "Seltjarnarnes": {"Reykjavik": 4, "Akureyri": 390}
}


def ans(city_name: str, city_distances: Dict[str, Dict[str, int]]) -> str:
    distances = city_distances[city_name]
    total_distance_to_reykjavik = distances["Reykjavik"]
    total_distance_to_akureyri = distances["Akureyri"]

    if total_distance_to_reykjavik <= total_distance_to_akureyri:
        return "Reykjavik"
    else:
        return "Akureyri"


def solve() -> None:
    data = input()
    print(ans(data, city_distances))


if __name__ == "__main__":
    solve()
