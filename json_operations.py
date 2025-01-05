import json
import sys

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error loading JSON file '{file_path}': {e}")
        sys.exit(1)

def save_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving JSON file '{file_path}': {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file.json> <output_file.json>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not input_file.endswith('.json'):
        print("Error: Input file must be a JSON file.")
        sys.exit(1)
    
    if not output_file.endswith('.json'):
        print("Error: Output file must be a JSON file.")
        sys.exit(1)
    
    try:
        data = load_json(input_file)
        print(f"Loaded data: {data}")
        save_json(data, output_file)
    except SystemExit:
        # If load_json() or save_json() called sys.exit(1),
        # this block catches it to prevent displaying the traceback.
        pass

if __name__ == "__main__":
    main()

