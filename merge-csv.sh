# This AWK command processes multiple CSV files and ensures that only the first file retains its header, while subsequent files exclude their headers.

# awk 'NR==1 || FNR > 1' *.csv

# Breakdown:
# NR==1 → Ensures the very first row across all files is kept.
# FNR > 1 → Keeps all rows except the first row in each individual file.
# *.csv → Applies this logic to all CSV files in the current directory.
# Example Use Case:
# If you have multiple CSV files and want to merge them but avoid repeating headers from each file, this command will only keep the header from the first file and remove headers from subsequent files.

awk 'NR==1 || FNR > 1' *.csv
