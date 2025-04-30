import json


class JsonLoader:
    """
    A class to load JSON data from a file.
    """

    def __init__():
        pass

    @staticmethod
    def load(file_path: str) -> dict:
        """
        Loads the JSON data from the file.
        """

        with open(file_path, "r") as file:
            data = json.load(file)
        return data
