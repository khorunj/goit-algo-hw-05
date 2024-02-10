import sys

def parse_log_line(line: str) -> dict:
    date, time, level, *message = line.split(' ', 3)
    return {'date': date, 'time': time, 'level': level, 'message': ''.join(message).strip()}

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r') as logfile:
            lines = list(map(parse_log_line, logfile.readlines()))
        return lines
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda x: x['level'] == level.upper(), logs))

def count_logs_by_level(logs: list) -> dict:
    cntr = {}
    for log in logs:
        if log['level'] not in cntr.keys():
            cntr[log['level']] = 1
        else:
            cntr[log['level']] += 1
    return cntr

def display_log_counts(counts: dict):
    width = [20, 10]
    print(f"{'Рівень логування':<20} | Кількість")
    print(f'{"-" * 20}|{"-" * 10}')
    for level, count in counts.items():
        print(f"{level:<{width[0]}} | {count}")

def display_logs_details(logs: list):
    print("\nДеталі логів:")
    for log in logs:
        print(f"{log['level']} {log['date']} {log['time']} - {log['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py /path/to/logfile.log [level]")
        sys.exit(1)

    filename = sys.argv[1]
    logs = load_logs(file_path=filename)

    if len(sys.argv) == 3:
        level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, level)
        print(display_log_counts(count_logs_by_level(filtered_logs)))
        display_logs_details(filtered_logs)
    else:
        print(display_log_counts(count_logs_by_level(logs)))
