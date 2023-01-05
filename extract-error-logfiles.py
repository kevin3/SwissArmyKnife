import re
from datetime import datetime

# Compile a regular expression to extract the timestamp and log level from each log line
# matching lines like 2023-01-05 06:01:55.378 ERROR
log_pattern = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) (\w+)')

# Define the start and end times of the time range
start_time = datetime(2023, 1, 5, 6, 0, 0)
end_time = datetime(2023, 1, 5, 19, 0, 0)

# Open the log file
with open(log_filepath, 'r') as log_file:
    # Iterate over each line in the log file
    for line in log_file:
        # Extract the timestamp and log level from the log line
        log_match = log_pattern.search(line)
        if log_match:
            # Convert the timestamp to a datetime object
            timestamp = datetime.strptime(log_match.group(1), '%Y-%m-%d %H:%M:%S.%f')
            log_level = log_match.group(2)
            # Check if the timestamp and log level match the desired criteria
            if start_time <= timestamp <= end_time and log_level == 'ERROR':
                # If the timestamp and log level match the criteria, include the log line in the output
                print(line)
