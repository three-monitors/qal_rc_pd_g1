from vernadsky_lab.minerals import MINERAL_CATALOG


def hardest_minerals(n=3):
    """Повертає n найтвердіших мінералів"""
    sorted_minerals = sorted(
        MINERAL_CATALOG.items(),
        key=lambda x: x[1]["hardness"],
        reverse=True
    )
    return [name for name, _ in sorted_minerals[:n]]


def search_by_origin(origin_keyword):
    """Повертає мінерали за місцем знахідки"""
    origin_lower = origin_keyword.lower()
    matching_minerals = []

    for name, data in MINERAL_CATALOG.items():
        if origin_lower in data["origin"].lower():
            matching_minerals.append(name)

    return matching_minerals
