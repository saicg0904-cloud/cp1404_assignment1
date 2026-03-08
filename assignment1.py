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


def main():
    """Main function: program entry point and menu loop."""
    print(f"Travel Tracker 1.0 - by Qiuhao Wu")
    places = []  # Temporary empty list
    print(f"{len(places)} places loaded from {CSV_FILE}")
    print(MENU)
    while True:
        choice = input(">>> ").strip().upper()
        if choice == "Q":
            print(f"{len(places)} places saved to {CSV_FILE}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")
        print(MENU)


if __name__ == "__main__":
    main()