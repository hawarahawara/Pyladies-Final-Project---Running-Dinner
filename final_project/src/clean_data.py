import pandas as pd

def clean_data(df):
    """
    Cleans the DataFrame by applying several transformations:
    1. Set missing dietary preferences to 'none'.
    2. Set missing addresses to 'missing'.
    3. Convert email addresses, dietary preferences, and addresses to lowercase.
    4. Strip leading and trailing spaces.
    5. Convert timestamp to datetime object (though this is not necessary as the timestemp will be disregarded)
    """
    # Fill missing dietary preferences with 'none' and make all lowercase
    df['Team Dietary Preferances'] = df['Team Dietary Preferances'].fillna('none').str.lower().str.strip()

    # Fill missing addresses with 'missing'
    df['Address of Host'] = df['Address of Host'].fillna('missing').str.lower().str.strip()

    # Make email addresses lowercase and strip whitespaces
    df['E-Mail-Adresse'] = df['E-Mail-Adresse'].str.lower().str.strip()

    # Convert 'Zeitstempel' to a datetime object
    df['Zeitstempel'] = pd.to_datetime(df['Zeitstempel'], format='%d.%m.%Y %H:%M:%S')

    return df

if __name__ == "__main__":
    # Example usage (for testing the cleaning function)
    # Import the data using the previous 'import_data' function from your import_data.py script
    file_path = r"c:\Users\barba\Dropbox\PC\Desktop\DOKUMENTE NEU SORTIERT\weiterbildung\2024_spring_pyladies\final_project\data\running_dinner_test_data.xlsx"
    
    # Call the import_data function to get the DataFrame
    df = import_data(file_path)
    
    # Clean the DataFrame using the clean_data function
    df_cleaned = clean_data(df)
    
    # Print the cleaned DataFrame to check its correctness
    print("This is the cleaned data set:")
    print(df_cleaned)