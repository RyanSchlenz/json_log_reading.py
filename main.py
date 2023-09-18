from scripts import *
from compare_files import *

def main():
   log_file_paths = ['LogAnalysis/logs/log_a.json', 'LogAnalysis/logs/log_b.json']

save_common_values_to_json(log_file_paths, output_file_path)

find_and_save_matching_entries(csv_file_path, json_file_path, output_file_path)

if __name__ == "__main__":
    main()
    
    
