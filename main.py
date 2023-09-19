import generate_csv_matches

log_csv = 'log.csv'
json_matches = 'json_matches.json'
csv_matches = 'csv_json_matches.json'

def main():
    # Define input and output file paths here
    csv_file_path = log_csv
    json_file_path = json_matches
    output_file_path = csv_matches

    # Call the function to compare JSON and CSV data
    entry_matcher = generate_csv_matches.EntryMatcher(csv_file_path, json_file_path, output_file_path)
    entry_matcher.find_and_save_matching_entries()

if __name__ == "__main__":
    main()
