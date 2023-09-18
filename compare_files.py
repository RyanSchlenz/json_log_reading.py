import csv
import json

def find_and_save_matching_entries(csv_file_path, json_file_path, output_file_path):
    # Initialize a list to store matching entries
    matching_entries = []

    # Read IP addresses from the CSV file and store them in a set
    csv_ip_addresses = set()
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            csv_ip_addresses.add(row['ip_address'])

    # Read and process the JSON file
    with open(json_file_path, 'r') as json_file:
        try:
            json_data = json.load(json_file)
            
            # Assuming the JSON data is a list of strings
            for entry in json_data:
                try:
                    entry_dict = json.loads(entry)  # Parse the JSON string into a dictionary
                    user_data = entry_dict.get('user')
                    if user_data:
                        ip_address = user_data.get('ip_address')
                        if ip_address and ip_address in csv_ip_addresses:
                            matching_entries.append(entry_dict)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except FileNotFoundError:
            print(f"File not found: {json_file_path}")

    # Write the matching entries to a new JSON file
    if matching_entries:
        with open(output_file_path, 'w') as output_file:
            json.dump(matching_entries, output_file, indent=4)
        print(f"Matching entries saved to {output_file_path}")
    else:
        print("No matching entries found.")

# Paths to CSV and JSON files
csv_file_path = '/Users/ryan/Desktop/JLogAnalysis/LogAnalysis/logs/log.csv'
json_file_path = '/Users/ryan/Desktop/JLogAnalysis/json_matches.json'
output_file_path = 'csv_json_matches.json'

# Call the function to find and save matching entries
find_and_save_matching_entries(csv_file_path, json_file_path, output_file_path)
