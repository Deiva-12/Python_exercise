from log_entry import LogEntry
def parse_log_file(filepath: str) -> list[LogEntry]:
    error_logs = []
    with open("app.log",'r')as file:
        for line in file:
            print(line)
            
    #         # Find lines that contain the word "ERROR"
            if " - ERROR - " in line or "- CRITICAL -" in line:
                try:
                    # Split the line into parts based on the " - " delimiter
                    parts = line.strip().split(" - ", 2)
                    timestamp = parts[0]
                    level = parts[1]
                    message = parts[2]

                    # Create a LogEntry object and add it to our list
                    log_obj = LogEntry(timestamp, level, message)
                    error_logs.append(log_obj)
                except IndexError:
                    # Skip malformed lines
                    continue
    return error_logs


# --- Main Execution ---
error_entries = parse_log_file("app.log")
print("--- Extracted Error Log Objects ---")
for entry in error_entries:
    print(entry)
