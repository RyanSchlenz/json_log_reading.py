Scripts to compare json logs to find matches, then see if there is a match in a csv file based on IP addresses. 

p_generate_json_matches.py:
This script primarily deals with JSON log files.
It defines functions to open and process JSON log files, converting JSON objects into strings, and parsing specific data from these entries.
There's a function for comparing JSON log files and saving common entries to a new JSON file.
The script also includes a usage section that calls the functions to compare JSON log files and save common entries to a JSON file.

p_generate_csv_matches.py:

This script focuses on matching entries between a CSV file and a JSON file based on IP addresses.
It defines a class called EntryMatcher with methods to extract IP addresses from JSON entries, find matching entries, and save them to a new JSON file.
The script checks if the JSON file exists before processing it and handles potential errors during the process.

p_main.py:

This script imports the p_generate_csv_matches module, schedules the main function to run every 30 minutes, and continuously checks for pending tasks.
The main function invokes the entry matching process using the EntryMatcher class from the p_generate_csv_matches module and prints a success message.
