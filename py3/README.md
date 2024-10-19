# JSON to CSV Converter

This Python project allows users to convert JSON data into CSV format. It provides options to either open an existing JSON file or create a new one, enter data, and save it as a CSV file. It also offers the choice to open the converted CSV file after completion.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example JSON Format](#example-json-format)
- [Contributing](#contributing)
- [License](#license)

## Features

- Convert existing JSON files to CSV.
- Create new JSON files, input data, and convert them to CSV.
- Automatic opening of the CSV file after conversion (optional).
- Easy-to-use terminal prompts.

## Requirements

- Python 3.x
- Modules: `json`, `csv`, `os` (all are part of the Python standard library)

## Installation

1. **Clone or download this repository**:
    ```bash
    git clone https://github.com/nikhilpachange/json-to-csv-converter.git
    cd json-to-csv-converter
    ```

2. **Ensure you have Python 3 installed**:
    - You can check if Python is installed by running:
      ```bash
      python --version
      ```
    - If you don’t have Python, download and install it from [python.org](https://www.python.org/).

3. **No additional libraries required** as the project uses Python's built-in libraries.

## Usage

1. **Run the script**:
    - Open your terminal (Command Prompt for Windows, Terminal for macOS/Linux).
    - Navigate to the directory where the script is located.
    - Run the script:
      ```bash
      python json_to_csv_converter.py
      ```

2. **Follow the prompts**:
    - Press `1` to select an existing JSON file or `2` to create a new one.
    - If you choose to create a new file, the program will open a text editor (Notepad) where you can input your JSON data.
    - After entering your JSON data, the program will ask for the name of the CSV file you'd like to create.
    - Once the conversion is complete, you will be asked if you'd like to open the CSV file.

## Example JSON Format

The JSON file should be structured as a list of dictionaries. Each dictionary represents a row in the CSV file.

Example:

```json
[
    {"name": "John", "age": 30, "city": "New York"},
    {"name": "Anna", "age": 22, "city": "London"},
    {"name": "Mike", "age": 32, "city": "Chicago"}
]
