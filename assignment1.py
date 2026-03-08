"""
CP1404 Assignment 1 - Travel Tracker
Student Name: Qiuhao Wu
GitHub URL: https://github.com/saicg9904-cloud/cp1404_assignment1
"""

import csv
import random

FILENAME = "places.csv"


def load_places():
    """
    Load places from CSV file.
    Returns:
        list: List of place lists [name, country, priority, visited]
              visited is boolean (True/False)
    """
    places = []
    try:
        with open(FILENAME, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                # Convert priority to int and visited to boolean
                row[2] = int(row[2])
                row[3] = row[3].lower() == 'true'
                places.append(row)
    except FileNotFoundError:
        # If file doesn't exist, return empty list (no error message per sample output)
        pass
    return places


def save_places(places):
    """
    Save places to CSV file.
    Args:
        places (list): List of place lists to save
    """
    with open(FILENAME, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for place in places:
            # Convert boolean visited back to string for CSV
            writer.writerow([place[0], place[1], place[2], str(place[3])])


def display_places(places):
    """
    Display the list of places in a neatly formatted, aligned way.
    Dynamically calculate column widths based on longest values (per assignment requirement).

    Args:
        places (list): List of place lists [name, country, priority, visited]
    """
    if not places:
        return  # No custom message - match sample output

    # Calculate max lengths for dynamic alignment
    max_name_length = max(len(place[0]) for place in places)
    max_country_length = max(len(place[1]) for place in places)

    # Sort: unvisited first, then by priority (ascending)
    sorted_places = sorted(places, key=lambda x: (x[3], x[2]))

    print("\nPlaces to visit:")
    for index, place in enumerate(sorted_places, 1):
        name, country, priority, visited = place
        marker = "*" if not visited else " "
        # Dynamic alignment with formatted strings
        print(f"{marker}{index}. {name:<{max_name_length}} in {country:<{max_country_length}} priority {priority}")


def add_place(places):
    """
    Add a new place to the list with input validation.
    Args:
        places (list): List of place lists to add to
    """
    print("\nAdd a new place:")

    # Validate name (non-empty)
    while True:
        name = input("Name: ").strip()
        if name:
            break
        print("Name cannot be empty.")

    # Validate country (non-empty)
    while True:
        country = input("Country: ").strip()
        if country:
            break
        print("Country cannot be empty.")

    # Validate priority (positive integer)
    while True:
        try:
            priority = int(input("Priority: ").strip())
            if priority > 0:
                break
            print("Priority must be a positive number.")
        except ValueError:
            print("Please enter a valid number for priority.")

    # Add new place (default to unvisited: False)
    places.append([name, country, priority, False])
    print(f"Added {name} in {country} (priority {priority}) to travel tracker.")


def recommend_place(places):
    """
    Recommend a random unvisited place.
    Args:
        places (list): List of place lists
    """
    # Filter unvisited places
    unvisited_places = [place for place in places if not place[3]]

    if not unvisited_places:
        print("\nNo places left to visit!")
        return

    # Randomly select one
    recommended = random.choice(unvisited_places)
    print(f"\nRecommended place to visit: {recommended[0]} in {recommended[1]} (priority {recommended[2]})")


def mark_visited(places):
    """
    Mark a place as visited by its display index (most precise matching).
    Args:
        places (list): List of place lists
    """
    if not places:
        print("\nNo places to mark as visited.")
        return

    # Display places first for user reference
    display_places(places)

    # Validate input and mark place
    while True:
        try:
            selected_index = int(input("\nEnter the number of the place to mark as visited: ").strip()) - 1  # Convert to 0-index
            if 0 <= selected_index < len(places):
                # Check if already visited
                if places[selected_index][3]:
                    print(f"You have already visited {places[selected_index][0]}!")
                else:
                    places[selected_index][3] = True
                    print(f"Marked {places[selected_index][0]} as visited.")
                break
            else:
                print(f"Please enter a number between 1 and {len(places)}.")
        except ValueError:
            print("Please enter a valid integer.")


def main():
    """Main function - run the travel tracker program."""
    print("Travel Tracker 1.0 - by Qiuhao Wu")
    places = load_places()
    print(f"Loaded {len(places)} places from {FILENAME}")

    # Main menu loop
    while True:
        print("\nMenu:")
        print("D - Display places")
        print("R - Recommend a random place")
        print("A - Add a new place")
        print("M - Mark a place as visited")
        print("Q - Quit")

        choice = input("Enter your choice: ").strip().upper()

        if choice == 'D':
            display_places(places)
        elif choice == 'R':
            recommend_place(places)
        elif choice == 'A':
            add_place(places)
        elif choice == 'M':
            mark_visited(places)
        elif choice == 'Q':
            save_places(places)
            print(f"\nSaved {len(places)} places to {FILENAME}")
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice. Please enter D, R, A, M or Q.")


if __name__ == "__main__":
    main()