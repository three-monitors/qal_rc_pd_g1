from pathlib import Path
from datetime import datetime
import re


def parse_heartbeat_log(filename: Path) -> dict:
    """Парсить лог-файл і повертає словник з даними по кожному KEY"""
    heartbeats = {}

    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            # Парсимо рядок: шукаємо Timestamp та Key
            timestamp_match = re.search(r'Timestamp (\d{2}:\d{2}:\d{2})', line)
            key_match = re.search(r'Key (TSTFEED\d{4})', line)

            if timestamp_match and key_match:
                timestamp_str = timestamp_match.group(1)
                key = key_match.group(1)

                # Перетворюємо timestamp на datetime об'єкт
                timestamp = datetime.strptime(timestamp_str, "%H:%M:%S")

                if key not in heartbeats:
                    heartbeats[key] = []

                heartbeats[key].append(timestamp)

    return heartbeats


def analyze_heartbeats(heartbeats: dict) -> dict:
    """Аналізує інтервали між ударами та повертає детальний звіт"""
    report = {
        'summary': {},
        'issues': []
    }

    for key, timestamps in heartbeats.items():
        # Сортуємо timestamps
        timestamps.sort()

        warnings = 0
        errors = 0
        max_interval = 0

        # Обчислюємо інтервали між послідовними ударами
        for i in range(1, len(timestamps)):
            interval = (timestamps[i] - timestamps[i-1]).total_seconds()
            max_interval = max(max_interval, interval)

            if interval > 31 and interval < 33:
                warnings += 1
                report['issues'].append({
                    'key': key,
                    'timestamp': timestamps[i],
                    'interval': interval,
                    'level': 'WARNING'
                })
            elif interval > 33:
                errors += 1
                report['issues'].append({
                    'key': key,
                    'timestamp': timestamps[i],
                    'interval': interval,
                    'level': 'ERROR'
                })

        report['summary'][key] = {
            'total_records': len(timestamps),
            'warnings': warnings,
            'errors': errors,
            'max_interval': max_interval
        }

    return report


def log_report(report: dict, output_file: Path) -> None:
    """Логує детальний звіт у файл"""
    with open(output_file, mode="w", encoding="utf-8") as f:
        # Записуємо зведення
        f.write("=== ЗВЕДЕННЯ ПО ПРОЦЕСАХ ===\n")
        for key, stats in report['summary'].items():
            f.write(f"KEY {key}:\n")
            f.write(f"  Всього записів: {stats['total_records']}\n")
            f.write(f"  WARNING: {stats['warnings']}\n")
            f.write(f"  ERROR: {stats['errors']}\n")
            f.write(
                f"  Максимальний інтервал: {stats['max_interval']:.1f}s\n\n")

        # Записуємо деталі проблем
        f.write("=== ДЕТАЛІ ПРОБЛЕМ ===\n")
        for issue in report['issues']:
            timestamp_str = issue['timestamp'].strftime("%H:%M:%S")
            log_message = f"{issue['level']} - KEY {issue['key']} - {timestamp_str} - Interval: {issue['interval']:.1f}s"
            f.write(log_message + "\n")
            print(log_message)


def main():
    """Головна функція"""
    filename = Path(__file__).parent / "hblog.txt"
    output_file = Path(__file__).parent / "hb_test.log"

    print(f"Аналіз файлу: {filename}")

    # Парсимо лог
    heartbeats = parse_heartbeat_log(filename)

    print(f"Знайдено процесів: {len(heartbeats)}")
    for key, timestamps in heartbeats.items():
        print(f"  KEY {key}: {len(timestamps)} записів")

    # Аналізуємо інтервали
    report = analyze_heartbeats(heartbeats)

    total_warnings = sum(stats['warnings']
                         for stats in report['summary'].values())
    total_errors = sum(stats['errors'] for stats in report['summary'].values())

    print(f"\nЗагальна статистика:")
    print(f"  WARNING: {total_warnings}")
    print(f"  ERROR: {total_errors}")

    # Логуємо результати
    log_report(report, output_file)

    print(f"\nРезультати записано в: {output_file}")


if __name__ == "__main__":
    main()
