import json
import sys

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error loading JSON file '{file_path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file.json>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    
    if not input_file.endswith('.json'):
        print("Error: Input file must be a JSON file.")
        sys.exit(1)
    
    try:
        data = load_json(input_file)
        print(f"Loaded data: {data}")
    except SystemExit:
        # If load_json() or any function called by it called sys.exit(1),
        # this block catches it to prevent displaying the traceback.
        pass

if __name__ == "__main__":
    main()

