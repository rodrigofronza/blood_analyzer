"""
Blood Analyzer Main Module
"""

from src.json_loader import JsonLoader


def main():
    """
    Main
    """
    print("Welcome to the Blood Analyzer script!!!")
    blood_data = JsonLoader.load("blood_analyzer/src/data/blood_data.json")
    print(f"Loaded blood data: {blood_data}")
    JsonLoader.print_my_love()


if __name__ == "__main__":
    main()
