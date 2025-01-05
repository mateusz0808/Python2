import json
import yaml
import sys
from lxml import etree

def parse_arguments():
    if len(sys.argv) != 3:
        print("Usage: python file_converter.py <input_file> <output_file>")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

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

def load_yaml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data
    except Exception as e:
        print(f"Error loading YAML file '{file_path}': {e}")
        sys.exit(1)

def save_yaml(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f, default_flow_style=False)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving YAML file '{file_path}': {e}")
        sys.exit(1)

def load_xml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = etree.parse(f)
        return etree.tostring(tree, pretty_print=True).decode()
    except Exception as e:
        print(f"Error loading XML file '{file_path}': {e}")
        sys.exit(1)

def save_xml(data, file_path):
    try:
        with open(file_path, 'wb') as f:
            f.write(data.encode())
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving XML file '{file_path}': {e}")
        sys.exit(1)

def main():
    input_file, output_file = parse_arguments()

    if input_file.endswith('.json'):
        data = load_json(input_file)
    elif input_file.endswith('.yaml') or input_file.endswith('.yml'):
        data = load_yaml(input_file)
    elif input_file.endswith('.xml'):
        data = load_xml(input_file)
    else:
        print("Unsupported input file format")
        sys.exit(1)

    if output_file.endswith('.json'):
        save_json(data, output_file)
    elif output_file.endswith('.yaml') or output_file.endswith('.yml'):
        save_yaml(data, output_file)
    elif output_file.endswith('.xml'):
        save_xml(data, output_file)
    else:
        print("Unsupported output file format")
        sys.exit(1)

if __name__ == "__main__":
    main()
