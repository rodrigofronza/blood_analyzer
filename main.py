from src.json_loader import JsonLoader


def main():
    print("Welcome to the Blood Analyzer!")
    blood_data = JsonLoader.load("blood_analyzer/data/blood_data.json")
    print(f"Loaded blood data: {blood_data}")


if __name__ == "__main__":
    main()
