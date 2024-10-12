import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    """Парсим рядок з лог-файлу і повертаємо словник з розібраними компонентами."""
    parts = line.split(' ', 3)# Розбиваємо на 4 частини: дата, час, рівень, повідомлення
    if len(parts) < 4:
        return None # Якщо формат неправильний
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3]
    }


def loads_logs(file_path: str) -> list:
    """Завантажує логи з файлу та парсить їх."""
    logs = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                parsed = parse_log_line(line.strip())
                if parsed:
                    logs.append(parsed)
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрує логи за заданим рівнем логування."""
    return [log for log in logs if ['level'].lower() == level.lower()]

def count_logs_by_level(logs: list) -> dict:
     """Підраховує кількість записів за рівнем логування."""
     counts = defaultdict(int)
     for log in logs:
         counts[log['level']] +=1
     return dict(counts)

def display_log_counts(counts: dict):    
     #Виводить статистику по рівнях логування в табличному форматі.
     print("Рівень логування | Кількість")
     print("-----------------|----------")
     for level in ['INFO', 'DEBAG', 'ERROR', 'WARNING']:
        print(f"{level:<17} | {counts.get(level, 0)}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py /шлях/до/логфайлу.log [рівень]")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = loads_logs(log_file_path)

    # Підрахунок загальної статистики
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    # Фільтрація по рівню, якщо вказано
    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"Не знайдено логів для рівня '{level.upper}'.")

if __name__=="__main__":
    main()
                
    

