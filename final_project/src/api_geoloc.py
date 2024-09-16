import os
import sys
print(sys.path)
from dotenv import load_dotenv
import requests

# Load the environment variables from the .env file
load_dotenv()

# Get the API key
API_KEY = os.getenv("API_KEY")
print(f"Loaded API key: {API_KEY}")  # Temporary check to ensure it's loading correctly

def get_coordinates(address):
    base_url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        'q': address,
        'key': API_KEY,
        'limit': 1,  # Limit to one result
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            coordinates = data['results'][0]['geometry']
            return coordinates['lat'], coordinates['lng']
        else:
            print(f"No results found for {address}")
            return None, None
    else:
        print(f"Error: Unable to fetch data for {address}")
        return None, None

def add_coordinates_to_dataframe(df):
    # Add new columns to store Latitude and Longitude
    df['Latitude'] = None
    df['Longitude'] = None

    # Loop through each address in the DataFrame and get the coordinates
    for index, row in df.iterrows():
        address = row['Address of Host']  # Change this if your column is named differently
        lat, lng = get_coordinates(address)
        df.at[index, 'Latitude'] = lat
        df.at[index, 'Longitude'] = lng

    return df
if __name__ == "__main__":
    # Test the get_coordinates function with a sample address
    address = "Mariahilferstraße 66, 1070 Wien"  # Example address, replace with any other address for testing
    lat, lng = get_coordinates(address)
    if lat and lng:
        print(f"Coordinates for '{address}': Latitude = {lat}, Longitude = {lng}")
    else:
        print(f"Could not retrieve coordinates for '{address}'")