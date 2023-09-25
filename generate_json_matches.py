import config
import json

log_file_paths = config.LOG_FILE_PATHS

# Open and read the JSON file
def openJsonLogFile(*paths):
    for path in paths:
        with open(path, 'r') as log_file:
            try:
                log_data = json.load(log_file)  # Load the entire JSON array
                for log_entry in log_data:
                    yield json.dumps(log_entry)  # Convert each JSON object to a string
            except json.JSONDecodeError:
                # Handle the case when the entire file is not valid JSON
                print(f"Invalid JSON in the file: {path}")




# parse the JSON file, store in dictionary 
def parseJsonLog(log_entry):
    r = {}  # Initialize an empty dictionary
    try:
        log_data = json.loads(log_entry)
        user_data = log_data.get("user", {})  # Access the "user" object
        
        # Accessing values from the dictionary
        r["name"] = user_data.get("name", "N/A")
        r["ip_address"] = user_data.get("ip_address", "N/A")
        r["UserId"] = user_data.get("UserId", "N/A")
        
        return r
    except json.JSONDecodeError:
        # Handle the case when the log entry is not valid JSON
        r["error"] = "Invalid JSON format"
        return r

# Function to compare JSON log files
def compare_json(*args):
    if len(args) < 2:
        return "At least two sets of data are required for comparison."

    common_values = set(args[0]).intersection(*args[1:])

    return list(common_values)

def save_common_values_to_json(log_file_paths, output_file_path):
    common_values = []
    for i, file_path1 in enumerate(log_file_paths):
        for file_path2 in log_file_paths[i + 1:]:
            data1 = list(openJsonLogFile(file_path1))
            data2 = list(openJsonLogFile(file_path2))

            common_values.extend(compare_json(data1, data2))

    # Save common values to a JSON file
    with open(output_file_path, 'w') as json_file:
        json.dump(common_values, json_file, indent=4)

# Usage
output_file_path = 'json_matches.json'
save_common_values_to_json(log_file_paths, output_file_path)
