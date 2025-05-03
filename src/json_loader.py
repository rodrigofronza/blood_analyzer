"""A module to load JSON data from a file."""

import dataclasses
import json


@dataclasses.dataclass
class JsonLoader:
    """
    A class to load JSON data from a file.
    """

    @staticmethod
    def load(file_path: str) -> dict:
        """
        Loads the JSON data from the file.
        """

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
