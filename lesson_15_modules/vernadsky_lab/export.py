import csv
import os
from vernadsky_lab.observations import get_observations


def to_csv(filename):
    """Експортує весь журнал спостережень у CSV файл"""
    observations = get_observations()

    if not observations:
        print("Немає спостережень для експорту")
        return

    try:
        # Створює шлях до папки vernadsky_lab
        script_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_dir, filename)

        with open(csv_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "researcher", "mineral", "note"])

            for entry in observations:
                writer.writerow([
                    entry["date"],
                    entry["researcher"],
                    entry["mineral"],
                    entry["note"]
                ])

        print(f"Спостереження експортовано в {csv_path}")

    except Exception as e:
        print(f"Помилка при експорті: {e}")
