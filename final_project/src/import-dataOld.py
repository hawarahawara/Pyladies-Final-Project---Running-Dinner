import pandas as pd
import os

def import_data(file_path):
    # Imports the data from a relative path into pandas
    try:
        # Read the Excel file into a DataFrame
        data = pd.read_excel(file_path)
        
        # Print out the first few rows to check if data is imported correctly
        print("Data imported successfully:")
        print(data.head())

        return data
    except Exception as e:
        print(f"Error importing data: {e}")
        return None

def main():
    # Get the directory where the current script is located
    script_dir = os.path.dirname(__file__)

    # Construct the relative path to the Excel file
    file_path = os.path.join(script_dir, '..', 'data', 'running_dinner_test_data.xlsx')

    # Import data from Excel
    data = import_data(file_path)

if __name__ == "__main__":
    main()