"""
CP1404/CP5632 Assignment 1: Travel Tracker 1.0
Student Name: Qiuhao Wu
Date: 2026-03-08
GitHub URL: https://github.com/saicg0904-cloud/cp1404_assignment1
Travel tracker program to manage visited/unvisited travel places with CSV I/O and menu interaction.
"""

import random

# Named constants (only allowed global variables)
VISITED = "v"
UNVISITED = "n"
CSV_FILE = "places.csv"
MENU = """Menu:
D - Display all places
R - Recommend a random place
A - Add a new place
M - Mark a place as visited
Q - Quit"""


def load_places():
    """
    Load places from CSV file at program start (only once).
    Returns: list of lists - raw place data with priority converted to integer
    """
    places = []
    try:
        with open(CSV_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                try:
                    name = parts[0].strip()
                    country = parts[1].strip()
                    priority = int(parts[2].strip())
                    status = parts[3].strip().lower()
                    places.append([name, country, priority, status])
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError:
        pass
    return places


def save_places(places):
    """
    Save places to CSV file (only once on program quit), overwrite existing content.
    Avoid extra blank line at the end of file.
    Args:
        places (list of lists): Current place data to save
    """
    lines = [f"{p[0]},{p[1]},{p[2]},{p[3]}" for p in places]
    with open(CSV_FILE, "w") as file:
        file.write("\n".join(lines))


def sort_places(places):
    """Sort places by visited status (unvisited first) then by priority (lower = higher)."""
    return sorted(places, key=lambda x: (x[3] == VISITED, x[2]))


def count_unvisited(places):
    """Count the number of unvisited places in the list."""
    return sum(1 for place in places if place[3] == UNVISITED)


def display_places(places):
    """Display all places in a neatly formatted, sorted list (matches sample output)."""
    if not places:
        print("No places tracked yet.")
        return
    sorted_places = sort_places(places)
    unvisited_count = count_unvisited(sorted_places)
    total_count = len(sorted_places)
    for index, place in enumerate(sorted_places, 1):
        name, country, priority, status = place
        marker = "*" if status == UNVISITED else ""
        print(f"{marker}{index}. {name} in {country} {priority}")
    print(
        f"{total_count} places tracked. "
        f"You still want to visit {unvisited_count} places."
    )


def get_valid_input(prompt, is_blank_allowed=False):
    """Generic input validation for non-numeric inputs (name/country)."""
    while True:
        user_input = input(prompt).strip()
        if user_input or is_blank_allowed:
            return user_input
        print("Input can not be blank")


def get_valid_number(prompt, min_value=1):
    """Generic input validation for numeric inputs (priority/place number)."""
    while True:
        try:
            number = int(input(prompt).strip())
            if number > min_value - 1:
                return number
            print(f"Number must be > {min_value - 1}")
        except ValueError:
            print("Invalid input; enter a valid number")


def add_place(places):
    """Add a new unvisited place to the in-memory list with full input validation."""
    name = get_valid_input("Name: ")
    country = get_valid_input("Country: ")
    priority = get_valid_number("Priority: ")
    places.append([name, country, priority, UNVISITED])
    print(f"{name} in {country} (priority {priority}) added to Travel Tracker.")


def recommend_place(places):
    """Recommend a random unvisited place, or print message if no unvisited places."""
    unvisited_places = [p for p in places if p[3] == UNVISITED]
    if not unvisited_places:
        print("No places left to visit!")
        return
    random_place = random.choice(unvisited_places)
    name, country = random_place[0], random_place[1]
    print("Not sure where to visit next?")
    print(f"How about... {name} in {country}?")


def mark_visited(places):
    """Mark a selected place as visited (cannot revert) with full input validation."""
    unvisited_count = count_unvisited(places)
    if unvisited_count == 0:
        print("No unvisited places")
        return
    display_places(places)
    total_places = len(places)
    place_number = get_valid_number(
        "Enter the number of a place to mark as visited\n>>> ", 1
    )
    while place_number > total_places:
        print("Invalid place number")
        place_number = get_valid_number(">>> ", 1)

    sorted_places = sort_places(places)
    selected_place = sorted_places[place_number - 1]

    if selected_place[3] == VISITED:
        print(f"You have already visited {selected_place[0]}")
        return

    # Exact match: locate by name + country + priority to avoid matching errors from duplicate data
    for place in places:
        if (place[0] == selected_place[0] and
            place[1] == selected_place[1] and
            place[2] == selected_place[2]):
            place[3] = VISITED
            break
    print(f"{selected_place[0]} in {selected_place[1]} visited!")


def main():
    """Main function: program entry point and menu loop."""
    print(f"Travel Tracker 1.0 - by Qiuhao Wu")
    places = load_places()
    print(f"{len(places)} places loaded from {CSV_FILE}")
    print(MENU)
    while True:
        choice = input(">>> ").strip().upper()
        if choice == "D":
            display_places(places)
        elif choice == "A":
            add_place(places)
        elif choice == "R":
            recommend_place(places)
        elif choice == "M":
            mark_visited(places)  # Add mark_visited function
        elif choice == "Q":
            save_places(places)
            print(f"{len(places)} places saved to {CSV_FILE}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")
        print(MENU)


if __name__ == "__main__":
    main()