

import logging
from src.main_classes import GeodesicDistance
import src.sub_classes as sc
import yaml

# Logger
logger = logging.getLogger()

# Variables
bicimad_data_path = '../data/bicimad_clean.csv'
emt_data_path = '../data/emt_clean.csv'


# Functions
def get_station_info(transportation, station_id):
    """Receives a transportation method and a station ID, and returns
    information of the required station.

    Params:
        - transportation: str expected, transport method
        - station_id: int expected, station ID which the user wants to obtain info
    Returns:
        - station_info: dict, information of the requested station
    Raises:
        - TypeError if wrong data received
        - ValueError if wrong transportation received
    """

    logger.info('Starting the function...')

    # Evaluating inputs
    if not isinstance(transportation, str):
        logger.error(f'Wrong data type. Received {type(transportation)} instead of "str".')
        raise TypeError(f'Transportation must be a string, not {type(transportation)}')
    elif not isinstance(station_id, int):
        logger.error(f'Wrong data type. Received {type(station_id)} instead of "int".')
        raise TypeError(f'Station ID must be an integer, not {type(station_id)}')

    if transportation.lower() not in ['emt', 'bicimad']:
        logger.error(f'Received {transportation} instead EMT or BiciMAD')
        raise ValueError(f'Transportation {transportation} not found. Must be EMT or BiciMAD')

    # Functionality
    elif transportation.lower() == 'emt':
        emt_object = sc.Emt(emt_data_path)
        emt_data = emt_object.get_transport_data()

        station_object = sc.EmtStation(emt_data, station_id)
        station_info = station_object.get_full_info()

        logger.info('Data successfully returned')
        return station_info

    else:
        bicimad_object = sc.BiciMad(bicimad_data_path)
        bicimad_data = bicimad_object.get_transport_data()

        station_object = sc.BiciMadStation(bicimad_data, station_id)
        station_info = station_object.get_full_info()

        logger.info('Data successfully returned')
        return station_info


def get_distance(point_a, point_b):
    """Receives two coordinates by parameter, and returns the geodesic distance between them (in km).

    Params:
        - point_a: tuple or list expected, first coordinate
        - point_b: tuple or list expected, second coordinate
    Returns:
        - Formatted string indicating the distance between the two points
    Raises:
        - TypeError if unexpected inputs
    """
    # Evaluating inputs
    if type(point_a) not in (tuple, list) or type(point_b) not in (tuple,list):
        logger.error('Bad data from input.')
        raise TypeError('Unexpected input; required two coordinates in an iterable object')

    if len(point_a) != 2 or len(point_b) != 2:
        logger.error('Bad data from input.')
        raise TypeError('Each coordinate must have two floats: longitude and latitude.')

    if type(point_a[0]) != float or type(point_a[1]) != float or \
            type(point_b[0]) != float or type(point_b[1]) != float:
        logger.error('Error. Bad data received.')
        raise TypeError('Error. Both latitude and longitude must be float numbers.')

    # Functionality
    try:
        distance_km = round(GeodesicDistance(point_a, point_b).get_distance, 3)
        return f'Distance between {point_a} and {point_b}: {distance_km} km.'
    except Exception as e:
        logger.error('Unexpected error', e)
        return 'Unexpected error. Impossible to calculate distance.'


def read_config_file(file_name='config.yml', absolute_file_path=None):
    """Read yml config file to get parameters

    Params:
        - path: str expected, path where the yml is located (local)
        - file_name: str expected, default: 'config.yml', name of the yml file
    Return:
        - parsed_yml: dict, yml parameters
    Raises:
        - FileNotFoundError if 'file_name' not found
    """
    try:
        if absolute_file_path:
            config_file = absolute_file_path
        else:
            config_file = file_name

        with open(config_file, 'r') as stream:
            parsed_yml = yaml.safe_load(stream)
            return parsed_yml

    except FileNotFoundError as f:
        logger.error(f, 'File not found in provided path.')
        raise FileNotFoundError('Wrong path. File not found.')

