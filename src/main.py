import datetime
import logging
import config
import os

import generate_csv_matches
import generate_json_matches

def main():
    logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", filename='file_compare.log', level=logging.INFO)

    # Define input and output file paths here
    csv_file_path = config.CSV_FILE_PATH
    json_file_path = config.JSON_FILE_PATH
    output_file_path = config.OUTPUT_FILE_PATH

    # Call the function to create JSON output file
    logging.info("Create JSON File")
    generate_json_matches.create_json(config.LOG_FILE_PATHS, output_file_path)

    # Call the function to compare JSON and CSV data
    logging.info("Comparing JSON and CSV")
    entry_matcher = generate_csv_matches.EntryMatcher(csv_file_path, json_file_path, output_file_path)
    entry_matcher.find_and_save_matching_entries()

    # Print a message indicating that the script ran successfully
    logging.info(f"Success! {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Remove file process
    if os.path.exists(config.JSON_FILE_PATH):
        os.remove(config.JSON_FILE_PATH)

if __name__ == "__main__":
    main()
