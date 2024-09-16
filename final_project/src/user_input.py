def ask_user_inputs():
    # Ask the user for the number of teams, teams per course, and number of courses
    num_teams = int(input("Enter the number of teams: "))
    teams_per_course = int(input("How many teams should come together for a course (including the host): "))
    num_courses = int(input("Enter the number of courses: "))
    return num_teams, teams_per_course, num_courses

def validate_team_count(df, num_teams):
    """
    Validates if the number of teams provided by the user matches
    the number of teams in the DataFrame.
    """
    # Get the actual number of rows (teams) in the DataFrame
    actual_team_count = len(df)

    # Compare the actual number of teams with the user input
    while True:
        # Get user input
        num_teams, teams_per_course, num_courses = ask_user_inputs()

        # Validate the user input
        if validate_team_count(df_cleaned, num_teams):
            print("Team count is valid. Proceeding with matching...")
            break  # Break the loop if the team count is valid
        else:
            print("Please re-enter the correct number of teams.\n")
        
if __name__ == "__main__":
    # Test the ask_user_inputs function
    num_teams, teams_per_course, num_courses = ask_user_inputs()
    print(f"User Inputs: \nNumber of teams: {num_teams}\nTeams per course: {teams_per_course}\nNumber of courses: {num_courses}")
