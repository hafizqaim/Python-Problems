def calculate_seconds(team_data):
    if not team_data:
        return []

    total_seconds = []
    time_strings = team_data.split(',')

    for time_range in time_strings:
        try:
            hours, mins, secs = map(int, time_range.strip().split('|'))
            try:
                if hours < 0 or mins < 0 or secs < 0:
                    print(f"Negative time values are not allowed: {time_range}")
            except ValueError:
                print(f"Invalid time format: {time_range}")
                continue
            seconds = hours * 3600 + mins * 60 + secs
            total_seconds.append(seconds)
        except ValueError:
            print(f"Invalid time format: {time_range}")
            continue

    return total_seconds

def seconds_to_time(seconds):
    try:
        if seconds < 0:
            raise ValueError("Negative seconds are not allowed")
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return f"{hours:02d}|{minutes:02d}|{seconds:02d}"
    except Exception as e:
        print(f"Error converting seconds to time: {e}")
        return "00|00|00"

def stats(team_data):
    if not isinstance(team_data, str):
        return "Error: Input must be a string."

    if not team_data:
        return ""

    times_in_seconds = calculate_seconds(team_data)

    if not times_in_seconds:
        return "Error: No valid race times found in input."

    range_in_seconds = max(times_in_seconds) - min(times_in_seconds)

    average_in_seconds = sum(times_in_seconds) // len(times_in_seconds)

    times_in_seconds.sort()
    n = len(times_in_seconds)
    if n % 2 == 1:
        median_in_seconds = times_in_seconds[n//2]
    else:
        median_in_seconds = (times_in_seconds[n//2 - 1] + times_in_seconds[n//2]) // 2
 
    range_time = seconds_to_time(range_in_seconds)
    average_time = seconds_to_time(average_in_seconds)
    median_time = seconds_to_time(median_in_seconds)

    return f"Range: {range_time} Average: {average_time} Median: {median_time}"

data = "02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41"
print(stats(data))
