import json
import os
import requests

from Model.Person import Person


CACHE_FILE_NAME = 'cache.json'    # Dataset JSON cache file name
API_URL = 'https://randomuser.me/api/'


class DataLoader:
    """
    Module for data management functionalities. It is intended to be used to load, store and process the datasets
    """

    @staticmethod
    def import_data(n_values=1000, load_cache=False) -> list:
        """
        Method to import the data. By default it loads the data from the RandomUser API service. If it is indicated,
        and the file exists, the data can be loaded from a cache file stored in a JSON format. This functionality
        is useful to avoid calling the API service too many times in a short period of time and to work offline.
        :param n_values: The amount of users to load
        :param load_cache: An optional parameter to indicate that it is preferred, if possible, to load the data from a
            cache file instead of from the API.
        :return: The list with the information of the requested number of users
        """

        data = []

        # It is checked if the data can be extracted from the cache and if it is desired
        if load_cache and os.path.exists(CACHE_FILE_NAME):
            # The data is loaded from the JSON file and truncated to the number of elements requested
            data = DataLoader.import_from_json()[:n_values]
            # If there is enough data it is returned. If not, it is completed with data from an API call
            if len(data) >= n_values:
                return DataLoader.import_from_json()[:n_values]

        # It is performed the API call for all the necessary remaining users
        response = requests.get(url=API_URL, params={'results': n_values - len(data)})
        response.raise_for_status()

        # The result of the request is added to the already loaded values
        data += response.json()["results"]

        # It is saved the new data structure in the cache JSON file
        DataLoader.save_json(data)
        return data

    @staticmethod
    def convert_to_people(data: list[dict]) -> list[Person]:
        """
        Method to convert the original raw data from the API to a list of Person class items
        :param data: Original raw dataset from the API
        :return: list of processed data
        """

        people = []
        for item in data:
            people.append(Person(item))

        return people

    @staticmethod
    def save_json(data: list[dict], filename=CACHE_FILE_NAME):
        """
        Method to save the dataset in a JSON file
        :param filename: Desired name for the file to store the data
        :param data: Dataset to store
        """

        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def import_from_json(filename=CACHE_FILE_NAME) -> list[dict]:
        """
        Method to import the dataset from a JSON file
        :param filename: Name file of the desired dataset to load
        :return: dataset from the JSON file
        """

        with open(filename) as f:
            return json.load(f)
