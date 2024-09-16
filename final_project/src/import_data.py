# Imports necessary libraries
import pandas as pd
import openpyxl

def import_data(file_path):
# Imports data from an Excel file and processes it into a DataFrame with an indexed column named 'Team Number'.
    # Loads the excel file into a pandas DataFrame, using the path provided
    df = pd.read_excel(file_path)

    # Resets the original index and adjusts it to start at 1
    df_reset = df.reset_index(drop=True)  # Reset the original index
    df_reset.index = df_reset.index + 1   # Start the index at 1
    df_reset.index.name = 'Team Number'   # Assign the name 'Team Number' to the index
    return df_reset

if __name__ == "__main__":
    # Define the file path
    file_path = r"c:\Users\barba\Dropbox\PC\Desktop\DOKUMENTE NEU SORTIERT\weiterbildung\2024_spring_pyladies\final_project\data\running_dinner_test_data.xlsx"

    # Call the import_data function and get the DataFrame
    df_reset = import_data(file_path)

    # Print the DataFrame to check its correctness
    print("This is the current data set we are working with:")
    print(df_reset)


