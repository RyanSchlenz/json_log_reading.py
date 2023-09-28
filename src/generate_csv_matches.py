import csv
import json

class EntryMatcher:
    def __init__(self, csv_file_path, json_file_path, output_file_path):
        self.csv_file_path = csv_file_path
        self.json_file_path = json_file_path
        self.output_file_path = output_file_path

    def extract_ip_addresses(self, json_str):
        try:
            entry_dict = json.loads(json_str)  # Parse the JSON string into a dictionary
            user_data = entry_dict.get('user')
            if user_data:
                ip_address = user_data.get('ip_address')
                return ip_address
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        return None

    def find_and_save_matching_entries(self):
        # Read IP addresses from the CSV file and store them in a set
        csv_ip_addresses = set()
        with open(self.csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                csv_ip_addresses.add(row['ip_address'])

        # Read and process the JSON file
        try:
            with open(self.json_file_path, 'w+') as json_file:
                json_result = json_file.read()

                # Initialize a list to store matching entries
                matching_entries = []

                for entry_str in json_result:
                    ip_address = self.extract_ip_addresses(entry_str)
                    if ip_address and ip_address in csv_ip_addresses:
                        matching_entries.append(entry_str)

                # Write the matching entries to a new JSON file
                if matching_entries:
                    with open(self.output_file_path, 'w+') as output_file:
                        output_file.write('\n'.join(matching_entries))
                        print(f"Matching entries saved to {self.output_file_path}")
                else:
                    print("No matching entries found.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except FileNotFoundError:
            print(f"File not found: {self.json_file_path}")

# Paths to CSV and JSON files
# csv_file_path = config.CSV_FILE_PATH
# json_file_path = config.JSON_FILE_PATH
# output_file_path = config.OUTPUT_FILE_PATH

# Check if the JSON file (json_matches) exists before processing
# if os.path.exists(json_file_path):
#     # Create an instance of EntryMatcher and call the function to find and save matching entries
#     entry_matcher = EntryMatcher(csv_file_path, json_file_path, output_file_path)
#     entry_matcher.find_and_save_matching_entries()
# else:
#     print(f"The file {json_file_path} does not exist.")
