import sys
import json
import yaml
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
from lxml import etree

# Funkcje do ładowania i zapisywania plików
def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        raise Exception(f"Error loading JSON file '{file_path}': {e}")

def save_json(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {file_path}")
    except Exception as e:
        raise Exception(f"Error saving JSON file '{file_path}': {e}")

def load_yaml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data
    except Exception as e:
        raise Exception(f"Error loading YAML file '{file_path}': {e}")

def save_yaml(data, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.safe_dump(data, f, default_flow_style=False)
        print(f"Data saved to {file_path}")
    except Exception as e:
        raise Exception(f"Error saving YAML file '{file_path}': {e}")

def load_xml(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            tree = etree.parse(f)
        return etree.tostring(tree, pretty_print=True).decode()
    except Exception as e:
        raise Exception(f"Error loading XML file '{file_path}': {e}")

def save_xml(data, file_path):
    try:
        with open(file_path, 'wb') as f:
            f.write(data.encode())
        print(f"Data saved to {file_path}")
    except Exception as e:
        raise Exception(f"Error saving XML file '{file_path}': {e}")

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Select files for conversion")
        self.layout.addWidget(self.label)

        self.select_input_btn = QPushButton("Select Input File")
        self.select_input_btn.clicked.connect(self.select_input_file)
        self.layout.addWidget(self.select_input_btn)

        self.select_output_btn = QPushButton("Select Output File")
        self.select_output_btn.clicked.connect(self.select_output_file)
        self.layout.addWidget(self.select_output_btn)

        self.convert_btn = QPushButton("Convert")
        self.convert_btn.clicked.connect(self.convert_files)
        self.layout.addWidget(self.convert_btn)

        self.setLayout(self.layout)
        self.setWindowTitle('Data Converter')
        self.show()

    def select_input_file(self):
        self.input_file, _ = QFileDialog.getOpenFileName(self, 'Open file', '', "All Files (*)")
        self.label.setText(f"Selected input file: {self.input_file}")

    def select_output_file(self):
        self.output_file, _ = QFileDialog.getSaveFileName(self, 'Save file', '', "All Files (*)")
        self.label.setText(f"Selected output file: {self.output_file}")

    def convert_files(self):
        if not hasattr(self, 'input_file') or not hasattr(self, 'output_file'):
            self.label.setText("Please select both input and output files")
            return
        input_file = self.input_file
        output_file = self.output_file

        # Call conversion function
        try:
            if input_file.endswith('.json'):
                data = load_json(input_file)
            elif input_file.endswith('.yaml') or input_file.endswith('.yml'):
                data = load_yaml(input_file)
            elif input_file.endswith('.xml'):
                data = load_xml(input_file)
            else:
                self.label.setText("Unsupported input file format")
                return

            if output_file.endswith('.json'):
                save_json(data, output_file)
            elif output_file.endswith('.yaml') or output_file.endswith('.yml'):
                save_yaml(data, output_file)
            elif output_file.endswith('.xml'):
                save_xml(data, output_file)
            else:
                self.label.setText("Unsupported output file format")
                return

            self.label.setText("Conversion successful")
        except Exception as e:
            self.label.setText(f"Error during conversion: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = ConverterApp()
    sys.exit(app.exec_())

