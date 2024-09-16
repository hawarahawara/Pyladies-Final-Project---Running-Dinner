# Running Dinner Matching Program

## Overview
The Running Dinner Matching Program is designed to help coordinate and match teams for a "running dinner" event. The program matches teams based on dietary preferences (grouping vegan and vegetarian together) and geographic location. Each team will host one course and participate in the other courses, ensuring that no two teams meet twice.

## Program Functionality:
Data Import:
Imports a dataset from an Excel file containing team details (e.g., names, dietary preferences, locations).

Data Cleaning:
Cleans and processes the imported data, ensuring it's ready for use.

User Input:
Takes user input for the number of teams, number of teams per course, and the number of courses.
Validates the user input to ensure it matches the actual data in the imported dataset.

Geographic Matching:
Uses geographic coordinates of team locations to optimize the grouping of teams based on proximity.
(Pending due to an issue with the dotenv package for handling API keys.)

Team Matching:
(Planned) Matches teams based on dietary preferences and geographic proximity, ensuring no team meets another twice.

## Programming Steps and Current Status:
1. Import Data Function (import_data)
Status: Completed
Function: Imports team data from an Excel file and returns it as a pandas DataFrame.
Note: The data import function works as intended and is integrated into the program.

2. Clean Data Function (clean_data)
Status: Completed
Function: Cleans the imported dataset by standardizing the columns, removing unnecessary data, and making it ready for processing.
Note: The data cleaning step is functioning properly.

3. User Input and Validation (ask_user_inputs, validate_team_count)
Status: Completed
Function:
Prompts the user for inputs regarding the number of teams, teams per course, and number of courses.
Validates the user's input against the number of teams in the dataset.
Note: Both the input and validation functions work, including error handling for incorrect input.

4. Geolocation API Integration (get_coordinates)
Status: Open/Partially Completed
Function:
Retrieves geographic coordinates (latitude and longitude) based on team addresses using a geolocation API (OpenCage).
Issue: The dotenv package for loading the API key isn't being recognized, preventing the API from functioning.
Next Steps: Debug the environment setup for python-dotenv or try an alternative method to securely load API keys.

5. Team Matching Algorithm
Status: Open
Planned Function:
Matches teams based on both their dietary preferences and geographic proximity.
Ensures that no team meets another twice during the event.
Next Steps: Implement the matching algorithm after resolving the geographic API issue.

## Open Problems
1. Geolocation API Integration
Problem: The program is encountering an error when trying to import the dotenv package, which is necessary for securely loading the API key for the geolocation service.
Solution: Investigate why dotenv isn't being recognized in the environment, or explore alternatives such as using environment variables directly in the operating system.

2. Team Matching Algorithm
Pending: The logic for matching teams based on dietary preferences and geographic location has not been implemented yet. This step depends on the successful integration of the geolocation API.


3. Missing GUI for User Interaction
Planned but Not Implemented: A graphical user interface (GUI) was planned to make the program more user-friendly, allowing users to input team numbers, course details, and view results without needing to interact with the command line.

Next Steps: After the core functionality of the program is complete (geographic API integration and team matching), the GUI can be implemented to provide a more intuitive way for users to interact with the program.

(this readme was written with the help of AI)

## Program Status  
- Last updated on: **September 16, 2024**
- Time: **01:50 PM**
