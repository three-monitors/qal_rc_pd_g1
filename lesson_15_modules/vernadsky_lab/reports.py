from vernadsky_lab.minerals import MINERAL_CATALOG
from vernadsky_lab.observations import get_observations


def summary():
    """Повертає загальне зведення про лабораторію"""
    mineral_count = len(MINERAL_CATALOG)
    observations = get_observations()
    observation_count = len(observations)

    if observation_count == 0:
        most_active = "Спостережень ще немає"
    else:
        researcher_counts = {}
        for entry in observations:
            researcher = entry["researcher"]
            researcher_counts[researcher] = researcher_counts.get(
                researcher, 0) + 1

        most_active_researcher = max(
            researcher_counts, key=researcher_counts.get)
        max_count = researcher_counts[most_active_researcher]
        most_active = f"{most_active_researcher} ({max_count} записи)"

    return f"Мінералів у каталозі: {mineral_count}\nСпостережень у журналі: {observation_count}\nНайактивніший дослідник: {most_active}"


def mineral_report(name):
    """Повертає детальний звіт по одному мінералу"""
    mineral = MINERAL_CATALOG.get(name)

    if mineral is None:
        return f"Мінерал '{name}' відсутній у каталозі"

    observations = get_observations(name)

    report = f"Формула: {mineral['formula']} | Твердість: {mineral['hardness']} | Походження: {mineral['origin']} | Відкрито: {mineral['discovered']}\nСпостереження:"

    if observations:
        for entry in observations:
            report += f"\n  [{entry['date']}] {entry['researcher']}: {entry['note']}"
    else:
        report += "\n  Спостережень ще немає"

    return report
