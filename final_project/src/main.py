# Imports necessary libraries and modules
import pandas as pd
import openpyxl
from import_data import import_data  # Import the import_data function
from clean_data import clean_data  # Import the clean_data function
from user_input import ask_user_inputs  # Import the ask_user_inputs function
from user_input import validate_team_count  # Import the validating function
from api_geoloc import get_coordinates  # Import the geolocation function

def main():
    # Get user input
    num_teams, teams_per_course, num_courses = ask_user_inputs()

    # Define the file path for import_data(file_path)
    file_path = r"c:\Users\barba\Dropbox\PC\Desktop\DOKUMENTE NEU SORTIERT\weiterbildung\2024_spring_pyladies\final_project\data\running_dinner_test_data.xlsx"

    # Call the import_data function and get the DataFrame
    df_reset = import_data(file_path)

    # Print the original DataFrame to check its correctness
    print("This is the current data set we are working with:")
    print(df_reset)

    # Clean the DataFrame using the clean_data function
    df_cleaned = clean_data(df_reset)

    # Print the cleaned DataFrame to check its correctness
    print("\nThis is the cleaned data set:")
    print(df_cleaned)

    # Validate user input for the number of teams
    if not validate_team_count(df_cleaned, num_teams):
        print("The number of teams does not match. Please restart the program with correct inputs.")
        return

    # Adding Geolocation Data
    print("\nFetching geolocation data for each team's host address...")

    # Create new columns for latitude and longitude
    df_cleaned['Latitude'] = None
    df_cleaned['Longitude'] = None

    # Iterate through the DataFrame and fetch coordinates for each address
    for index, row in df_cleaned.iterrows():
        address = row['Address of Host']
        if pd.notna(address):  # Ensure the address is not NaN
            lat, lng = get_coordinates(address)
            if lat and lng:
                df_cleaned.at[index, 'Latitude'] = lat
                df_cleaned.at[index, 'Longitude'] = lng
                print(f"Coordinates for '{address}': Latitude = {lat}, Longitude = {lng}")
            else:
                print(f"Could not retrieve coordinates for '{address}'")
        else:
            print(f"No valid address provided for team at index {index + 1}")

    # Print the final DataFrame with coordinates
    print("\nFinal dataset with geolocation data:")
    print(df_cleaned)

if __name__ == "__main__":
    main()