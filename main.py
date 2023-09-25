import generate_csv_matches
import datetime
import logging
import config

log_csv = config.CSV_FILE_PATH
json_matches = config.JSON_FILE_PATH
csv_matches = config.OUTPUT_FILE_PATH

def main():
    logging.basicConfig(filename='log_file_name.log',level=logging.INFO)
    # Define input and output file paths here
    csv_file_path = log_csv
    json_file_path = json_matches
    output_file_path = csv_matches

    # Call the function to compare JSON and CSV data
    entry_matcher = generate_csv_matches.EntryMatcher(csv_file_path, json_file_path, output_file_path)
    entry_matcher.find_and_save_matching_entries()

   # Print a message indicating that the script ran successfully
    logging.info(f"Success! {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
