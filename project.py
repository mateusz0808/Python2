import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Program description')
    parser.add_argument('input_file', help='Path to input file')
    parser.add_argument('output_file', help='Path to output file')
    args = parser.parse_args()
    return args.input_file, args.output_file

def main():
    input_file, output_file = parse_arguments()
    # Tutaj możesz dalej operować na input_file i output_file
    print(f"Input file: {input_file}")
    print(f"Output file: {output_file}")

if __name__ == "__main__":
    main()
