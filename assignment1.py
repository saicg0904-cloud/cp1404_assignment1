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


def main():
    """Main function: program entry point and menu loop."""
    print(f"Travel Tracker 1.0 - by Qiuhao Wu")
    places = load_places()  # Restore CSV loading
    print(f"{len(places)} places loaded from {CSV_FILE}")
    print(MENU)
    while True:
        choice = input(">>> ").strip().upper()
        if choice == "Q":
            save_places(places)  # Restore CSV saving
            print(f"{len(places)} places saved to {CSV_FILE}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")
        print(MENU)


if __name__ == "__main__":
    main()