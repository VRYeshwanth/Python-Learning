import os
import json

def search_json_files_by_date(date):
    # Validate date format
    if not validate_date_format(date):
        print("Invalid date format. Please use dd-mm-yyyy format.")
        return
    # Extract day, month, and year from the date
    day, month, year = date.split('-')
    # Construct the search pattern
    search_pattern = f"{day}-{month}-{year}.json"
    # Get the directory of the script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # List all files in the directory
    files = os.listdir(script_directory)
    # Search for JSON files matching the pattern
    json_files = [file for file in files if file.endswith('.json') and file == search_pattern]
    
    if json_files:
        print("Found JSON files matching the date:")
        for json_file in json_files:
            file_path = os.path.join(script_directory, json_file)
            print("\n")
            with open(file_path, 'r') as f:
                json_data = json.load(f)
                display_news(json_data)
    else:
        print("No JSON files found matching the date.")

def display_news(data):
    print("World News")
    a,b,c,d = 1,1,1,1
    for i in data["World News"]:
        print(f"{a}) {i}")
        a += 1
    print()
    print("National News")
    for i in data["National News"]:
        print(f"{b}) {i}")
        b += 1
    print()
    print("Sports News")
    for i in data["Sports News"]:
        print(f"{c}) {i}")
        c += 1
    print()
    print("Tech News")
    for i in data["Tech News"]:
        print(f"{d}) {i}")
        d += 1

def validate_date_format(date):
    # Validate date format (dd-mm-yyyy)
    try:
        day, month, year = date.split('-')
        if len(day) == 2 and len(month) == 2 and len(year) == 4:
            int(day)
            int(month)
            int(year)
            return True
    except ValueError:
        pass
    return False

if __name__ == "__main__":
    date = input("Enter the date in dd-mm-yyyy format: ")
    search_json_files_by_date(date)